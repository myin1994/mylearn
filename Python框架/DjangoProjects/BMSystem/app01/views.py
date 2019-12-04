from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.urls import reverse
from app01 import models
from django.db import transaction
from mytools import mytools
from django.http import JsonResponse

from datetime import datetime, timedelta


# Create your views here.
class Login(View):
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        print(request.POST)
        obj = models.UserInfo.objects.filter(password=password, username=username)
        if obj:
            ret = redirect(reverse("app01:books"))
            # ret.set_cookie("login_status","success")
            # ret.set_signed_cookie("login_status","success","xxxooo")

            # request.session['login_status'] = "success"
            # request.session['login_status1'] = "success1"

            return ret
            # return redirect(reverse("app01:books"))
        else:
            # status = "密码错误请重新登录！"
            return HttpResponse("error")
            # return render(request, "login.html", {"status": status})


def login_sign(f):
    def inner(request):
        login_status = request.session.get("login_status")
        login_status2 = request.session.get("login_status1")
        # session_key = request.session.session_key
        # print("session_key",session_key)
        # login_status2 = request.COOKIES.get("sessionid")
        # print(request.session.keys())
        # print(request.session.values())
        # print(request.session.items())
        # login_status = request.COOKIES.get("login_status")
        # login_status = request.get_signed_cookie("login_status",salt="xxxooo")
        # print(login_status)
        # print(login_status2)
        if login_status != "success":
            return redirect("app01:login")
        else:
            ret = f(request)
            return ret

    return inner


# @method_decorator(login_sign,name='get')
class Books(View):
    # @method_decorator(login_sign)
    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        dic = dict()
        obj = models.Book.objects.all()
        for i in obj:
            # s = ""
            # for j in i.authors.all().values("name"):
            #     s += " " + (j.get("name"))
            # dic[i]=s
            dic[i] = " ".join([j.name for j in i.authors.all()])

        return render(request, "books.html", {"obj": obj, "dic": dic})

    def post(self, request):
        del_id = request.POST.get("del_id")
        ret_data = {"status": None}
        try:
            models.Book.objects.get(id=del_id).delete()
            ret_data["status"] = 1
            return JsonResponse(ret_data)
        except:
            return JsonResponse(ret_data)
        # return redirect(reverse("app01:books"))


from app01.myforms import *

class AddBooks(View):

    def get(self, request):
        obj = BookModelForm()
        print(obj.fields)
        return render(request, "add_book.html", {"obj": obj})

    def post(self, request):
        with transaction.atomic():
            print(request.POST)
            obj = BookModelForm(request.POST)
            if obj.is_valid():
                obj.save()
                return redirect(reverse("app01:books"))
            else:
                return render(request, "add_book.html", {"obj": obj})


# class AddBooks(View):
#
#     def get(self, request):
#         publish = models.Publish.objects.all()
#         author = models.Author.objects.all()
#         return render(request, "add_book.html", {"publish": publish,"author":author})
#
#     def post(self,request):
#         with transaction.atomic():
#             dic = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publishs_id")
#             # 先添加book表
#             lst = request.POST.getlist("author")
#             if lst:
#                 new_obj = models.Book.objects.create(**dic)
#                 # 再添加book——author表
#
#                 # id = models.Book.objects.last().id
#                 # models.Book.objects.get(id=id).authors.add(*lst)
#                 new_obj.authors.add(*lst)
#             else:
#                 return HttpResponse("error")
#
#         return redirect(reverse("app01:books"))


class EditBooks(View):

    def get(self, request):
        book_id = request.GET.get("book_id")
        obj = models.Book.objects.get(id=book_id)
        obj = BookModelForm(instance=obj)
        return render(request, "edit_book.html",
                      locals())

    def post(self, request):
        with transaction.atomic():
            book_id = request.POST.get("edit_id")
            new_obj = models.Book.objects.get(id=book_id)
            obj = BookModelForm(request.POST,instance=new_obj)
            if obj.is_valid():
                obj.save()
                return redirect(reverse("app01:books"))
            else:
                return render(request, "edit_book.html", {"obj": obj,"book_id":book_id})



        # with transaction.atomic():
        #     dic = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publishs_id")
        #     # 修改book表
        #     # new_obj = models.Book.objects.filter(id=request.POST.get("edit_id")).update(**dic)
        #     obj = models.Book.objects.filter(id=request.POST.get("edit_id"))
        #     obj.update(**dic)
        #     # 再更新book——author表
        #     lst = request.POST.getlist("author")
        #     # id = models.Book.objects.last().id
        #     # models.Book.objects.get(id=id).authors.set(lst)
        #     obj.first().authors.set(lst)
        # return redirect(reverse("app01:books"))


# class EditBooks(View):
#
#     def get(self, request):
#         publish = models.Publish.objects.all()
#         author = models.Author.objects.all()
#         book_id = request.GET.get("book_id")
#
#         obj = models.Book.objects.get(id=book_id)
#         obj2 = models.Book.objects.filter(id=book_id).values("authors__id")
#         author_lst = []
#         for i in obj2:
#             author_lst.append(i["authors__id"])
#
#         return render(request, "edit_book.html",
#                       {"publish": publish, "author": author, "obj": obj, "author_lst": author_lst,
#                        "book_id": book_id})
#
#     def post(self, request):
#         with transaction.atomic():
#             dic = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publishs_id")
#             # 修改book表
#             # new_obj = models.Book.objects.filter(id=request.POST.get("edit_id")).update(**dic)
#             obj = models.Book.objects.filter(id=request.POST.get("edit_id"))
#             obj.update(**dic)
#             # 再更新book——author表
#             lst = request.POST.getlist("author")
#             # id = models.Book.objects.last().id
#             # models.Book.objects.get(id=id).authors.set(lst)
#             obj.first().authors.set(lst)
#         return redirect(reverse("app01:books"))


def upload(request):
    if request.method == "GET":
        return render(request, "upload.html")
    else:
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES.get('file_obj')
        print(file_obj)
        with open(file_obj.name, "wb") as f:
            for i in file_obj.chunks():
                f.write(i)
        return HttpResponse("OK")


def upload_file_write(file_obj, mode="wb"):
    with open(file_obj.name, mode=mode) as f:
        for i in file_obj.chunks():
            f.write(i)


def ajaxupload(request):
    if request.method == "GET":
        return render(request, "ajaxupload.html")
    else:
        print(request.POST)
        print("ajax")
        print(request.POST.get("name"))
        print(request.FILES)
        file_obj = request.FILES.get('file_obj')
        print(file_obj)
        upload_file_write(file_obj)
        return HttpResponse("OK")


import json


def data(request):
    if request.method == "GET":
        return render(request, 'xxx.html')
    else:
        # t = time.localtime(time.time())
        # d1 = {'name':'myname','age':datetime.datetime.now(),"time":t}
        d1 = {'name': 'myname', 'age': 18}
        print(request.POST)
        # dic1 = request.POST.get("dic1[name]")
        # dic2 = request.POST.get("dic1[age]")
        # dic3 = request.POST.get("age")
        # dic4 = request.POST.getlist("lst[]")
        dic = request.POST.get("dic1")
        print(type(json.loads(dic)), json.loads(dic))
        print(type(json.loads(dic)["age"]), json.loads(dic)["age"])
        # print(type(dic1),dic1)
        # print(type(dic2),dic2)
        # print(type(dic3),dic3)
        # print(type(dic4),dic4)
        # print(datetime.datetime.now())
        # print(d1)
        # d1 = [1,2,3,4,"22","你好"]
        # d1_str = json.dumps(d1,ensure_ascii=False)
        # print(1)
        # l1 = ["aa",'bb','cc','你好']
        # return JsonResponse(d1,safe=False)
        # return JsonResponse(l1,safe=False)
        # return HttpResponse(d1_str)
        return HttpResponse("ok")
        # return HttpResponse(d1_str,content_type="application/json")


# def index(request):
#     print("app01 中的 index视图")
#     # raise ValueError('出错啦1')
#     def render():
#         print("in index/render")
#         # raise ValueError('出错啦2') #至于render函数中报错了，那么会先执行process_template_response方法，然后执行process_exception方法，如果是在render方法外面报错了，那么就不会执行这个process_template_response方法了。
#         # return HttpResponse("O98K") #返回的将是这个新的对象
#     rep = HttpResponse("OK")
#     rep.render = render
#     return rep




# class LoginForm(forms.Form):
#     username = forms.CharField(
#         min_length=8,
#         label="用户名",
#         initial="张三",
#         error_messages={
#             "required": "不能为空",
#             "invalid": "格式错误",
#             "min_length": "用户名最短8位"
#         }
#     )
#     password = forms.CharField(min_length=6, label="密码")


class LoginForm(forms.Form):
    ...
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )

def form(request):
    obj = LoginForm()
    # if request.method == 'POST':
    #     obj = LoginForm(data=request.POST)
    #     if obj.is_valid():
    #         return HttpResponse("注册成功")
    return render(request, 'form验证.html', locals())
