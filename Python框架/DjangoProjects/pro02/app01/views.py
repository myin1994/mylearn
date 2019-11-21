from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from app01 import models

# Create your views here.
class Login(View):
    def get(self,request):


        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        obj = models.UserInfo.objects.filter(password=password,username=username)
        if obj:
            return redirect(reverse("app01:books"))
        else:
            status = "密码错误请重新登录！"
            return render(request,"login.html",{"status":status})

class Books(View):
    def get(self,request):
        obj = models.Book.objects.all()
        menu_dic = {"login":"/login/","books":"/books/","go":3,"python1":1,"java1":2,"go1":3}
        return render(request,"books.html",{"menu_lst":menu_dic,"obj":obj})

    def post(self,request):
        try:
            title = request.POST.get("title")
            if not title:
                raise TypeError('空')
            price = request.POST.get("price")
            publish_date = request.POST.get("publish_date")
            publish = request.POST.get("publish")
            # if not request.POST.get("edit-book"):
            #     obj = models.Book(title=title,price=price,publish_date=publish_date,publish=publish)
            #     obj.save()
            # else:
            if not request.POST.get("edit-book"):
                new_id = models.Book.objects.last().id+1
            else:
                new_id = request.POST.get("edit-book")
            models.Book.objects.update_or_create(
                id=new_id,
                defaults={
                    'title':title,
                    'price': price,
                    'publish_date': publish_date,
                    'publish': publish,
                }
            )
        except Exception as e:
            try:
                models.Book.objects.filter(id=request.POST.get("del_id")).delete()
            except:
                pass
        return redirect(reverse("app01:books"))
