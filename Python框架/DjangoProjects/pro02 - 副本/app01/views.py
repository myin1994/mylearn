from django.shortcuts import render,redirect,HttpResponse
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
from mytools import mytools
class Books(View):

    def get(self,request):
        obj = models.Book.objects.all()
        menu_dic = {"login":"/login/","books":"/books/","go":3,"python1":1,"java1":2,"go1":3}
        return render(request,"books.html",{"menu_lst":menu_dic,"obj":obj})


    def post(self,request):
        print(request.POST)
        try:
            ret = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publish")
            # print(ret)
            if not request.POST.get("edit-book"):
                new_id = models.Book.objects.last().id+1
            else:
                new_id = request.POST.get("edit-book")
            models.Book.objects.update_or_create(
                id=new_id,
                defaults=ret
            )
        except Exception as e:
            try:
                models.Book.objects.filter(id=request.POST.get("del_id")).delete()
            except:
                pass
        return redirect("app01:books")

class Querys(View):
    def get(self,request,values=None,obj = models.Book.objects.all()):
        if values == None:
            values = {'title_query': '',
                      'price_compare': '1',
                      'price_query': "0",
                      'date_query_starts': '',
                      'date_query_ends': '',
                      'publish_query': ''}
        menu_dic = {"login":"/login/","books":"/books/","go":3,"python1":1,"java1":2,"go1":3}
        return render(request,"books.html",{"menu_lst":menu_dic,"obj":obj,"values":values})

    def post(self,request):
        ret = mytools.dict_filter(request.POST,
                             "title_query",
                             "price_compare",
                             "price_query",
                             "date_query_starts",
                             "date_query_ends",
                             "publish_query")
        obj = models.Book.objects.all()
        print(ret)
        if ret.get("title_query"):
            obj = obj.filter(title__icontains=ret.get("title_query"))
        if ret.get("price_query"):
            if ret.get("price_compare") =="1":
                obj = obj.filter(price__gt=ret.get("price_query"))
            if ret.get("price_compare") =="2":
                obj = obj.filter(price__gte=ret.get("price_query"))
            if ret.get("price_compare") =="3":
                obj = obj.filter(price__lt=ret.get("price_query"))
            if ret.get("price_compare") =="4":
                obj = obj.filter(price__lte=ret.get("price_query"))
            if ret.get("price_compare") =="5":
                obj = obj.filter(price=ret.get("price_query"))
        if ret.get("date_query_starts"):
            obj = obj.filter(publish_date__gte=ret.get("date_query_starts"))
        if ret.get("date_query_ends"):
            obj = obj.filter(publish_date__lte=ret.get("date_query_ends"))
        if ret.get("publish_query"):
            obj = obj.filter(publish__icontains=ret.get("publish_query"))
        return self.get(request,values=ret,obj=obj)

# def query(request):
    # ret = models.Book.objects.all()
    # ret = models.Book.objects.filter(title__contains="C++")
    # ret = models.Book.objects.get(id=3)
    # ret = models.Book.objects.exclude(id=3)
    # ret = models.Book.objects.order_by("-id")
    # ret = models.Book.objects.order_by("-id").reverse()
    # ret = models.Book.objects.count()
    # ret = models.Book.objects.first()
    # ret = models.Book.objects.last()
    # ret = models.Book.objects.filter(id=9).exists()
    # ret = models.Book.objects.values()
    # ret = models.Book.objects.values("title","price")
    # ret = models.Book.objects.values_list("title","price")
    # ret = models.Book.objects.values_list("price").distinct()
    # ret = models.Book.objects.filter(price__gt=200)
    # ret = models.Book.objects.filter(title__startswith="py",publish_date__year=2017,publish_date__month=8).values("title")
    # ret = models.Book.objects.filter(price__in=[50,100,150]).values("title","publish")
    # ret = models.Book.objects.filter(price__range=[100,200]).values("title","price")
    # ret = models.Book.objects.filter(publish="人民出版社").values("price").order_by("-price").distinct()
    # print(ret)
    # return HttpResponse("ko")
