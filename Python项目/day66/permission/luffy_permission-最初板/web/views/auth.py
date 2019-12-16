from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from rbac import models

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username,password=password)
        if obj:
            #
            request.session["status"] = True
            per_obj = models.Permission.objects.filter(
                role__userinfo__username=username)

            #注入权限路径及对应父级路径id
            request.session["allowed_url"] = list(per_obj.values('url','parent_id').distinct())
            #筛选一级菜单对象并按权重降序排序
            menu_top = list(models.TopMenu.objects.filter(
                permission__role__userinfo__username=username).values().order_by('-weight').distinct())
            for menu_obj in menu_top:
                #根据一级菜单筛选二级菜单并按权重降序排序
                menu_obj['secondary_menu'] = list(models.Permission.objects.filter(
                    role__userinfo__username=username,menu_id=menu_obj.get('id')).values().order_by(
                    '-weight').distinct())
            request.session["menu"] = menu_top
            return redirect('web:home')
        else:
            return redirect('web:login')
