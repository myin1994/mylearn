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
            if request.session.get("status"):
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
            for url in allowed_url:
                if re.match(f'^{url.get("url")}$', current_path):
                    request.url_id = url.get('parent_id')
                    return
            else:
                return HttpResponse("莫得权限！")


