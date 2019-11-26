from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse
from app01 import models
from django.db import transaction
from mytools import mytools

# Create your views here.
class Login(View):
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        obj = models.UserInfo.objects.filter(password=password, username=username)
        if obj:
            return redirect(reverse("app01:books"))
        else:
            status = "密码错误请重新登录！"
            return render(request, "login.html", {"status": status})

class Books(View):

    def get(self, request):
        dic = dict()
        obj = models.Book.objects.all()
        for i in obj:
            s = ""
            for j in i.authors.all().values("name"):
                s += " " + (j.get("name"))
            dic[i]=s
        return render(request, "books.html", {"obj": obj,"dic":dic})

    def post(self,request):
        del_id = request.POST.get("del_id")
        models.Book.objects.get(id=del_id).delete()
        return redirect(reverse("app01:books"))


class AddBooks(View):

    def get(self, request):
        publish = models.Publish.objects.all()
        author = models.Author.objects.all()
        return render(request, "add_book.html", {"publish": publish,"author":author})

    def post(self,request):

        with transaction.atomic():
            dic = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publishs_id")
            # 先添加book表
            models.Book.objects.create(**dic)
            # 再添加book——author表
            lst = request.POST.getlist("author")
            id = models.Book.objects.last().id
            models.Book.objects.get(id=id).authors.add(*lst)
        return redirect(reverse("app01:books"))

class EditBooks(View):

    def get(self, request):
        publish = models.Publish.objects.all()
        author = models.Author.objects.all()
        book_id = request.GET.get("book_id")

        obj = models.Book.objects.get(id=book_id)
        obj2 = models.Book.objects.filter(id=book_id).values("authors__id")
        author_lst = []
        for i in obj2:
            author_lst.append(i["authors__id"])

        return render(request, "edit_book.html", {"publish": publish,"author":author,"obj":obj,"author_lst":author_lst,
                                                  "book_id":book_id})

    def post(self,request):

        with transaction.atomic():
            dic = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publishs_id")
            # 修改book表
            models.Book.objects.filter(id=request.POST.get("edit_id")).update(**dic)
            # 再更新book——author表
            lst = request.POST.getlist("author")
            id = models.Book.objects.last().id
            models.Book.objects.get(id=id).authors.set(lst)
        return redirect(reverse("app01:books"))