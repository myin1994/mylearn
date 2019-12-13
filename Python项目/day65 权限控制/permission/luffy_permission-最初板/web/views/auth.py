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


class Login(View):
    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=username,password=password)
        if obj:
            request.session["status"] = "success"
            request.session["allowed_url"] = list(obj.values('roles__permissions__url'))
            return redirect('web:customer_list')
        else:
            return redirect('web:login')
