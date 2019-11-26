from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse
from app01 import models
from django.db.models import *

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


from mytools import mytools


class Books(View):

    def get(self, request):
        obj = models.Book.objects.all()
        menu_dic = {"login": "/login/", "books": "/books/", "go": 3, "python1": 1, "java1": 2, "go1": 3}
        return render(request, "books.html", {"menu_lst": menu_dic, "obj": obj})

    def post(self, request):
        print(request.POST)
        try:
            ret = mytools.dict_filter(request.POST, "title", "price", "publish_date", "publish")
            # print(ret)
            if not request.POST.get("edit-book"):
                new_id = models.Book.objects.last().id + 1
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
    def get(self, request, values=None, obj=models.Book.objects.all()):
        if values == None:
            values = {'title_query': '',
                      'price_compare': '1',
                      'price_query': "0",
                      'date_query_starts': '',
                      'date_query_ends': '',
                      'publish_query': ''}
        menu_dic = {"login": "/login/", "books": "/books/", "go": 3, "python1": 1, "java1": 2, "go1": 3}
        return render(request, "books.html", {"menu_lst": menu_dic, "obj": obj, "values": values})

    def post(self, request):
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
            if ret.get("price_compare") == "1":
                obj = obj.filter(price__gt=ret.get("price_query"))
            if ret.get("price_compare") == "2":
                obj = obj.filter(price__gte=ret.get("price_query"))
            if ret.get("price_compare") == "3":
                obj = obj.filter(price__lt=ret.get("price_query"))
            if ret.get("price_compare") == "4":
                obj = obj.filter(price__lte=ret.get("price_query"))
            if ret.get("price_compare") == "5":
                obj = obj.filter(price=ret.get("price_query"))
        if ret.get("date_query_starts"):
            obj = obj.filter(publish_date__gte=ret.get("date_query_starts"))
        if ret.get("date_query_ends"):
            obj = obj.filter(publish_date__lte=ret.get("date_query_ends"))
        if ret.get("publish_query"):
            obj = obj.filter(publish__icontains=ret.get("publish_query"))
        return self.get(request, values=ret, obj=obj)


def query(request):
    # models.AuthorDetail.objects.create(birthday="1994-04-09",telephone="17600976019",addr="北京")
    # models.AuthorDetail.objects.create(birthday="1994-05-09",telephone="17600976018",addr="南京")
    # models.Authors.objects.create(name="张三",age=19,au_detail=models.AuthorDetail.objects.get(id=1))
    # models.Authors.objects.create(name="李四",age=19,au_detail_id=2)

    # models.AuthorDetail.objects.create(birthday="2994-04-09", telephone="17600446019", addr="西天")
    # models.Authors.objects.create(name="王五", age=21, au_detail_id=models.AuthorDetail.objects.get(id=3).id)
    # book_obj = models.Book.objects.get(id=2)
    # author1 = models.Authors.objects.get(id=1)
    # author2 = models.Authors.objects.get(id=2)
    # book_obj.author.add(1,2)
    # book_obj = models.Book.objects.get(id=2)
    # book_obj.author.remove(1)

    # obj = models.Book.objects.get(id=3)
    # obj.author.clear()
    # obj.author.set(["1","4"])

    # obj = models.AuthorDetail.objects.get(id=1)
    # obj.authors.name = "张三2"

    # obj = models.Publishs.objects.filter(name__startswith="南京").first()
    # print(obj.book_set.filter(id=3).delete())


    # ret = models.Authors.objects.filter(name="张三").values("au_detail__addr")
    # print(ret)
    # ret = models.AuthorDetail.objects.filter(authors__name="张三").values("addr")
    # print(ret)


    # ret = models.Book.objects.filter(title="C++").values("publish__name")
    # print(ret)
    # ret = models.Publishs.objects.filter(book__title="C++").values("name")
    # print(ret)

    # ret = models.Book.objects.filter(title="D++").values("author__name")
    # print(ret)
    # ret = models.Authors.objects.filter(book__title="D++").values("name")
    # print(ret)

    # ret = models.Book.objects.filter(author__age=19).values("title")
    # print(ret)

    # ret = models.Book.objects.values("publish_id").annotate(m=Max("price"))
    # ret = models.Publishs.objects.annotate(m=Max("book__price")).values("m","book__title")

    # ret = models.Book.objects.values("publish_id").annotate(m=Max("price"))
    ret = models.Publishs.objects.order_by("-book__price").values("id","book__title").annotate(m=Max("book__price"))
    print(ret)

    return HttpResponse("ko")
