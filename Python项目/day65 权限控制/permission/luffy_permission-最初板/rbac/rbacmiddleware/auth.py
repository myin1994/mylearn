import re
import json
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse


class LoginAuth(MiddlewareMixin):
    white_list = [reverse('web:login'), '/admin/.*']

    def process_request(self, request):
        current_path = request.path
        for path in self.white_list:
            if re.match(f'^{path}$', current_path):
                return
        else:
            login_status = request.session.get("status")
            if login_status == "success":
                return None
            else:
                return redirect("web:login")


class UrlAuth(MiddlewareMixin):
    white_list = [reverse('web:login'), '/admin/.*']

    def process_request(self, request):
        current_path = request.path
        for path in self.white_list:
            if re.match(f'^{path}$', current_path):
                return
        else:
            allowed_url = request.session.get("allowed_url")
            setattr(request, 'allowed_url', allowed_url)
            for url in allowed_url:
                if re.match(f'^{url.get("roles__permissions__url")}$', current_path):
                    return
            else:
                return HttpResponse("莫得权限！")


