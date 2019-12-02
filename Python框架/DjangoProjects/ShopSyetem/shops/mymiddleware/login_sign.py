from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse


class Login_sign(MiddlewareMixin):
    white_list = [reverse("shops:login"),reverse("shops:signup")]
    def process_request(self,request):
        login_status = request.session.get("status")
        if login_status == "success" or request.path in self.white_list:
            return None
        else:
            return redirect("shops:login")

    def process_response(self, request, response):
        if request.path == reverse("shops:goods") and request.session.get("role") != 1:
            return redirect("shops:login")
        elif request.path == reverse("shops:usergoods") and request.session.get("role") != 0:
            return redirect("shops:login")
        return response
