from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from django.views import View
from django.utils.decorators import method_decorator
from django.urls import reverse
from rbac import models
from django.db import transaction
from django.db.models import *
from django.db.utils import *
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

class MenuList(View):
    def get(self,request):
        if request.GET.get("delmenuobj"):
            self.delmenuobj(request.GET.get("delmenuobj"))
            return redirect('rbac:menu_list')
        if request.GET.get("delaccessobj"):
            self.delaccessobj(request.GET.get("delaccessobj"))
            return redirect('rbac:menu_list')
        menu_list = models.TopMenu.objects.all()
        access_list = models.Permission.objects.all()
        menu_id = request.GET.get('menu_id',0)
        if menu_id:
            access_list = access_list.filter(Q(menu_id=menu_id)|Q(parent__menu_id=menu_id))
        return render(request,"access_manage/menu_list.html",{"menu_list":menu_list,
                                                              "access_list":access_list,
                                                              "menu_id":int(menu_id)})

    def delmenuobj(self,obj_id):
        models.TopMenu.objects.filter(id=obj_id).delete()

    def delaccessobj(self,obj_id):
        models.Permission.objects.filter(id=obj_id).delete()

from django.forms import modelformset_factory
class AccessList(View):
    def get(self, request):
        access_list = modelformset_factory(models.Permission, AccessModelForm, extra=0)
        return render(request, 'access_manage/access_list.html', locals())

    def post(self, request):
        access_list = modelformset_factory(models.Permission, AccessModelForm, extra=0)
        access_list = access_list(request.POST)
        if access_list.is_valid():
            access_list.save()
            return redirect(request.path)

        else:
            return render(request, 'access_manage/access_list.html', locals())
