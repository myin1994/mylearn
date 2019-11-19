from django.shortcuts import render,HttpResponse
import pymysql
# Create your views here.

def login(request):
    username = request.POST.get("login_name")
    password = request.POST.get("login_password")
    if username and password:
        conn = pymysql.connect(host="127.0.0.1", user="root", password="77963333", database="day36")
        cur = conn.cursor()
        sql = "select * from userinfo where username = %s and password =%s"
        ret = cur.execute(sql, (username, password))
        if ret:
            print(111)
            return render(request,"login_success.html")
        else:
            return HttpResponse("密码错误，请重新输入！")
    else:
        return render(request,"login.html")
