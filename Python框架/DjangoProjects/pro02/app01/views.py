from django.shortcuts import render,redirect
from django.views import View
import pymysql

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get("login_name")
        password = request.POST.get("login_password")
        conn = pymysql.connect(host="127.0.0.1", user="root", password="77963333", database="day36")
        cur = conn.cursor()
        sql = "select * from userinfo where username = %s and password =%s"
        ret = cur.execute(sql, (username, password))
        if ret:
            return redirect("/books/")
        else:
            status = "密码错误请重新登录！"
            return render(request,"login.html",{"status":status})

class Books(View):
    def get(self,request):
        return render(request,"books.html")
