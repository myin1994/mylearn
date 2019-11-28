from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse


class Login_sign(MiddlewareMixin):
    white_list = [reverse("app01:login"),'/admin/login/']
    def process_request(self,request):
        login_status = request.session.get("login_status")
        print(request.path)
        if login_status == "success" or request.path in self.white_list:
            return None
        else:
            return redirect("app01:login")
