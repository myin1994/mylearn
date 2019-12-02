from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.urls import reverse
from shops import models
from django.db import transaction
from django.db.models import *
from mytools import mytools
from django.http import JsonResponse
import sys
import traceback
from datetime import datetime,timedelta
from shops.shoptools import *
from django.http import QueryDict
from django.db.utils import *

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        obj = models.UserInfo.objects.filter(password=password, username=username).first()
        if obj:
            request.session["status"] = "success"
            request.session["role"] = obj.role
            request.session["userid"] = obj.id
            return HttpResponse(obj.role)
        else:
            return HttpResponse("error")

class Logout(View):
    def get(self, request):
        request.session.flush()
        return render(request, "login.html")

class SignUp(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        try:
            models.UserInfo.objects.create(**dict_filter(request.POST,"用户名为空","username","password"))
            return HttpResponse("ok")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()  # 元组
            # print(exc_type, exc_value, exc_traceback)
            if type(exc_value) == NameError:
                return HttpResponse("blank")
            elif type(exc_value) == DataError:
                return HttpResponse("tolong")
            elif type(exc_value) == IntegrityError:
                return HttpResponse("Duplicate")
            else:
                print(exc_type, exc_value, exc_traceback)

class Goods(View):
    def get(self, request):
        goods = models.Goods.objects.all()
        return render(request, "goods.html",locals())

    def post(self,request):
        print(request.POST.get("edit_id"))

        try:
            if not request.POST.get("edit_id"):
                models.Goods.objects.create(**dict_filter(request.POST, "商品为空", "gname", "price"))
                return HttpResponse("ok")
            else:
                ret = models.Goods.objects.filter(id=request.POST.get("edit_id"))
                ret.update(**dict_filter(request.POST, "商品为空", "gname", "price"))
                return HttpResponse("edit-ok")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()  # 元组
            print(exc_type, exc_value, exc_traceback)
            traceback.print_tb(exc_traceback, limit=1)
            if type(exc_value) == NameError:
                return HttpResponse("blank")
            else:
                return HttpResponse("error")

    def delete(self,request):
        data = {"status":None}
        delete = QueryDict(request.body)
        try:
            models.Goods.objects.get(id=delete.get("del_id")).delete()
            data["status"] = 1
        except:
            pass
        return JsonResponse(data)


class UserGoods(View):
    def get(self, request):
        goods = models.Goods.objects.all()
        return render(request, "usergoods.html",locals())

    def post(self,request):
        uid = request.session["userid"]
        gid = request.POST.get("add_id")
        gnum_before = models.ShopCar.objects.filter(user_id=uid,mygoods_id=gid)
        if not gnum_before:
            gnumber = 1
        else:
            gnumber = gnum_before.first().gnumber+1
        models.ShopCar.objects.update_or_create(
            user_id=uid,
            mygoods_id=gid,
            defaults={
                "gnumber" : gnumber
            })
        return HttpResponse("OK")


class ShopCar(View):
    def get(self, request):
        uid = request.session["userid"]
        goods = models.Goods.objects.filter(shopcar__user_id=uid).values("shopcar__gnumber","gname","price","id")
        return render(request, "shopcar.html",locals())

    def delete(self,request):
        data = {"status":None}
        delete = QueryDict(request.body)
        try:
            models.ShopCar.objects.filter(user_id=request.session["userid"],mygoods_id=delete.get("del_id")).delete()
            data["status"] = 1
        except:
            pass
        return JsonResponse(data)

    @transaction.atomic
    def post(self,request):
        try:
            #结算
            # 添加订单表
            uid = request.session["userid"]
            allgoods = models.Goods.objects.filter(shopcar__user_id=uid).values("shopcar__gnumber", "gname", "price", "id")
            order_price = 0
            for i in allgoods:
                order_price += i["shopcar__gnumber"] * i["price"]
            if order_price == 0:
                raise NameError("购物车为空")
            # order_price = allgoods.aggregate(m=Sum(F("shopcar__gnumber")*F("price")))#只能进行整数运算
            ret = models.Order.objects.create(user_id=uid,order_price=order_price)
            # 添加订单商品表信息
            for i in allgoods:
                models.OrderGoods.objects.create(order1_id=ret.id,goods1_id=i["id"],goods_number=i["shopcar__gnumber"])
            # 删除用户购物车数据
            models.ShopCar.objects.filter(user_id=uid).delete()
            return HttpResponse("OK")
        except:
            # exc_type, exc_value, exc_traceback = sys.exc_info()  # 元组
            # print(exc_type, exc_value, exc_traceback)
            # traceback.print_tb(exc_traceback, limit=1)
            return HttpResponse("not OK")

class OrderList(View):
    def get(self, request):
        uid = request.session["userid"]
        orders = models.Order.objects.filter(user_id=uid)
        return render(request, "orderlist.html",locals())

class OrderDetails(View):
    def get(self, request):
        uid = request.session["userid"]
        order_id = request.GET.get("order_id")
        orders = models.OrderGoods.objects.filter(order1_id=order_id,order1__user_id=uid)
        orders = orders.values("goods1__gname","goods1__price","goods_number")
        print(orders)
        return render(request, "orderdetails.html",locals())

