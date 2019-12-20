import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from rbac import models


class LoginAuth(MiddlewareMixin):
    white_list = [reverse('web:login'), '/admin/.*',reverse('web:home')]

    def process_request(self, request):
        """
        登录认证
        """
        current_path = request.path
        for path in self.white_list:
            if re.match(f'^{path}$', current_path):
                return
        else:
            if request.session.get("status"):
                return None
            else:
                return redirect("web:login")

class UrlAuth(MiddlewareMixin):
    white_list = [reverse('web:login'), '/admin/.*',reverse('web:home')]

    def process_request(self, request):
        """
        权限控制
        """
        current_path = request.path
        for path in self.white_list:
            if re.match(f'^{path}$', current_path):
                return
        else:
            allowed_url = request.session.get("allowed_url")

            setattr(request, 'button_url', request.session.get("button_url"))
            for url in allowed_url:
                if re.match(f'^{url.get("url")}$', current_path):
                    request.url_id = url.get('parent_id')
                    request.url_title = url.get('access_name')
                    return
            else:
                return HttpResponse("莫得权限！")

    def process_response(self, request, response):
        """
        权限注入
        """
        if request.path == self.white_list[0] and request.session.get("status"):
            username = request.POST.get('username')
            per_obj = models.Permission.objects.filter(
                role__userinfo__username=username)

            # 注入权限路径及对应父级路径id
            request.session["allowed_url"] = list(per_obj.values('url', 'parent_id', 'access_name').distinct())
            request.session["button_url"] = list(per_obj.values('url').distinct())
            # 筛选一级菜单对象并按权重降序排序
            menu_top = list(models.TopMenu.objects.filter(
                permission__role__userinfo__username=username).values().order_by('-weight').distinct())
            for menu_obj in menu_top:
                # 根据一级菜单筛选二级菜单并按权重降序排序
                menu_obj['secondary_menu'] = list(models.Permission.objects.filter(
                    role__userinfo__username=username, menu_id=menu_obj.get('id')).values().order_by(
                    '-weight').distinct())
            request.session["menu"] = menu_top
        return response

