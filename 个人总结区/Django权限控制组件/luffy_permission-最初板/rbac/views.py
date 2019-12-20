from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from django.views import View
from django.urls import reverse

from django.db.models import *

# Create your views here.
from rbac.rbacforms.myforms import *

# Create your views here.
# 添加编辑视图（可追加url）
class AddOrEdit(View):
    def get_obj(self, request, form_id=None):
        id = form_id
        if not id:
            id = 1
        dic = {
            reverse('rbac:role_edit', args=(id,)): [models.Role, RoleModelForm],
            reverse('rbac:role_add'): [models.Role, RoleModelForm],
            reverse('rbac:menu_edit', args=(id,)): [models.TopMenu, TopMenuModelForm],
            reverse('rbac:menu_add'): [models.TopMenu, TopMenuModelForm],
            reverse('rbac:access_edit', args=(id,)): [models.Permission, PermissionModelForm],
            reverse('rbac:access_add'): [models.Permission, PermissionModelForm],
        }

        obj_list = dic.get(request.path)[0].objects.filter(id=form_id)
        if request.method == 'GET':
            modelform_obj = dic.get(request.path)[1](request, instance=obj_list.first())
        else:
            modelform_obj = dic.get(request.path)[1](request, request.POST, instance=obj_list.first())
        return obj_list, modelform_obj

    def get(self, request, form_id=None):
        obj_list, modelform_obj = self.get_obj(request, form_id)
        return render(request, 'access_manage/add_or_edit.html', locals())

    def post(self, request, form_id=None):
        obj_list, modelform_obj = self.get_obj(request, form_id)
        if modelform_obj.is_valid():
            modelform_obj.save()
            return redirect(request.GET.get("next_url"))
        else:
            return render(request, 'access_manage/add_or_edit.html', locals())

class RoleList(View):
    def get(self,request):
        if request.GET.get("delobj"):
            self.delobj(request.GET.get("delobj"))
            return redirect('rbac:role_list')
        role_list = models.Role.objects.all()
        return render(request,"access_manage/role_list.html",{"role_list":role_list})

    def delobj(self,obj_id):
        models.Role.objects.filter(id=obj_id).delete()

#用于排序的类
class SortList:
    """
    对菜单进行排序，全非菜单非子权限的置顶，
    然后二级菜单-子权限一一对应
    """
    def __init__(self,lst):
        self.lst = lst

    def get_null(self):
        for i in self.lst:
            if not i.get('menu_id') and not i.get("parent_id"):
                yield i

    def get_menu(self):
        for i in self.lst:
            if i.get('menu_id'):
                yield i

    def get_child(self):
        data = list(self.get_menu())
        for i in data.copy():
            child = []
            for j in self.lst:
                if j.get("parent_id") == i["id"]:
                    child.append(j)
            data[data.index(i):data.index(i)+1] = [i] + child
        return data

    def get_sorted(self):
        return list(self.get_null())+self.get_child()


class MenuList(View):
    def get(self,request):
        if request.GET.get("delmenuobj"):
            self.delmenuobj(request.GET.get("delmenuobj"))
            return redirect('rbac:menu_list')
        if request.GET.get("delaccessobj"):
            self.delaccessobj(request.GET.get("delaccessobj"))
            return redirect('rbac:menu_list')
        if request.GET.get("access_to_del"):
            self.access_to_del(request.GET.get("access_to_del"))
            return redirect('rbac:access_list')
        menu_list = models.TopMenu.objects.all()
        access_list = models.Permission.objects.all()

        menu_id = request.GET.get('menu_id',0)
        if menu_id:
            access_list = access_list.filter(Q(menu_id=menu_id)|Q(parent__menu_id=menu_id))
        access_list = access_list.values('menu_id',
                                         'parent_id','access_name','url','url_name','parent__access_name','id')
        access_list = SortList(access_list).get_sorted()
        return render(request,"access_manage/menu_list.html",{"menu_list":menu_list,
                                                              "access_list":access_list,
                                                              "menu_id":int(menu_id)})

    def delmenuobj(self,obj_id):
        models.TopMenu.objects.filter(id=obj_id).delete()

    def delaccessobj(self,obj_id):
        models.Permission.objects.filter(id=obj_id).delete()

    def access_to_del(self,obj_id):
        models.Permission.objects.filter(id=obj_id).delete()

from django.forms import modelformset_factory,formset_factory



from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import RegexURLResolver, RegexURLPattern
from collections import OrderedDict



def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    for item in urlpatterns:
        # 获取当前路径
        cur_url = item.regex.pattern.strip("^$")
        if isinstance(item, RegexURLPattern):
            if pre_namespace:
                if not item.name:
                    raise Exception('URL路由中必须设置name属性')
                url_ordered_dict[f"{pre_namespace}:{item.name}"] = {"url_name":f"{pre_namespace}:{item.name}","url":pre_url + cur_url}
            else:
                url_ordered_dict[f"{item.name}"] = {"url_name":f"{item.name}","url":pre_url + cur_url}
        else:
            namespace = item.namespace
            recursion_urls(namespace, pre_url + cur_url, item.url_patterns, url_ordered_dict)

def get_all_url_dict(ignore_namespace_list=None):
    """
        获取路由中
        :return:
        """
    ignore_list = ignore_namespace_list or []  # 短路操作 ['admin',]
    url_ordered_dict = OrderedDict()  # 有序字典,最终要使用的字典数据

    #通过路径获取文件对象（项目urls）
    md = import_string(settings.ROOT_URLCONF)
    urlpatterns = []

    # 通过项目路由获取路径解析对象
    #解析对象-RegexURLResolver
    #可执行对象-RegexURLPattern
    for item in md.urlpatterns:
        if isinstance(item, RegexURLResolver) and item.namespace in ignore_list:
            #跳过忽略列表中的解析器
            continue
        urlpatterns.append(item)

    recursion_urls(None, "/", urlpatterns, url_ordered_dict)
    return url_ordered_dict

#批量操作权限
class AccessList(View):


    def get(self, request):

        #更新用
        AccessSet = modelformset_factory(models.Permission, AccessModelForm, extra=0)

        #添加用
        AccessSetAdd = formset_factory(AccessModelForm, extra=0)

        # 获取数据库中现有的所有权限数据
        permissions = models.Permission.objects.all()

        # 获取项目的路由系统中所有URL
        router_dict = get_all_url_dict(ignore_namespace_list=['admin'])

        # 数据库中的所有权限的别名
        permissions_name_set = set([i.url_name for i in permissions])

        # 路由系统中的所有权限的别名
        router_name_set = set(router_dict.keys())

        # 新增差集（路由有，数据库没有）
        add_name_set = router_name_set - permissions_name_set
        # 通过initial设置对应字段初始值
        access_list_to_add = AccessSetAdd(initial=[row for name, row in router_dict.items() if name in add_name_set])

        # 待删除差集（数据库有，路由没有）
        del_name_set = permissions_name_set - router_name_set
        access_list_to_del = AccessSet(queryset=models.Permission.objects.filter(url_name__in=del_name_set))

        #更新交集（数据库及路由同时存在的部分）
        update_name_set = permissions_name_set & router_name_set
        access_list_to_update = AccessSet(queryset=models.Permission.objects.filter(url_name__in=update_name_set))

        return render(request, 'access_manage/access_list.html', locals())

    def post(self, request):
        # 更新用
        AccessSet = modelformset_factory(models.Permission, AccessModelForm, extra=0)

        # 添加用
        AccessSetAdd = formset_factory(AccessModelForm, extra=0)
        post_type = request.GET.get('type')  # add
        if post_type == 'add':
            add_formset = AccessSetAdd(request.POST)
            if add_formset.is_valid():
                permission_obj_list = [models.Permission(**i) for i in add_formset.cleaned_data]
                models.Permission.objects.bulk_create(permission_obj_list)
                return redirect('rbac:access_list')

        if post_type == 'update':
            update_formset = AccessSet(request.POST)
            if update_formset.is_valid():
                update_formset.save()
                return redirect('rbac:access_list')
        else:
            return redirect('rbac:access_list')


class AccessDistribute(View):
    def get(self,request,p_uid=0,p_rid=0):
        uid = request.GET.get('uid') or p_uid or 0
        rid = request.GET.get('rid') or p_rid or 0
        # 获取所有用户
        user_list = models.UserInfo.objects.all()

        # 获取所有角色信息
        role_list = models.Role.objects.all()

        # 获取当前选择用户的角色信息id
        user_has_roles_list = [item.id for item in role_list.filter(userinfo__id=uid)]


        # 获取当前用户及对应角色所有权限id
        # if uid
        role_has_access_list = [item.id for item in models.Permission.objects.filter(
            Q(role__userinfo__id=uid)|Q(role__id=rid))]
        menu_top = list(models.TopMenu.objects.filter().values().order_by('-weight').distinct())
        for menu_obj in menu_top:
            # 根据一级菜单筛选二级菜单并按权重降序排序
            menu_obj['secondary_menu'] = list(models.Permission.objects.filter(menu_id=menu_obj.get('id')).values().order_by(
                '-weight').distinct())
            for third_obj in menu_obj['secondary_menu']:
                third_obj['third_menu'] = list(models.Permission.objects.filter(parent_id=third_obj.get('id')).values().order_by(
                    '-weight').distinct())
        # all_menu_list = menu_top
        return render(request,'access_manage/distribute_access.html',locals())

    def post(self,request):
        uid = request.GET.get('uid')
        rid = request.GET.get('rid')
        roles_to_update = request.POST.getlist('roles')
        access_to_update = request.POST.getlist('permissions')
        if uid and roles_to_update:
            user = models.UserInfo.objects.filter(id=uid).first()
            if not user:
                return HttpResponse('用户不存在')
            user.roles.set(roles_to_update)

        if rid and access_to_update:
            role = models.Role.objects.filter(id=rid).first()
            if not role:
                return HttpResponse('角色不存在')
            role.permissions.set(access_to_update)

        return self.get(request,uid,rid)

def test(request):
    return HttpResponse("test")