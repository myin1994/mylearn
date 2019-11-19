from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    """

    :param request: 类似envrion,封装所有请求相关信息--->对象
    :return:
    """
    print(request.path)
    return render(request,"home.html")

# def books(request,year,month):
#     print(year,month)
#
#     return HttpResponse(f"{year}年{month}月书籍")

def books(request,*args,**kwargs):
    year = kwargs["year"]
    month = kwargs["month"]
    print(year,month)

    return HttpResponse(f"{year}年{month}月书籍")


def login(request):
    """

    :param request: 类似envrion,封装所有请求相关信息--->对象
    :return:
    """
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(type(request.POST))
    print(request.body)
    return render(request,"login.html")

# def login(request):
#     """
#
#     :param request: 类似envrion,封装所有请求相关信息--->对象
#     :return:
#     """
#     if request.method == "GET":
#         return render(request, "login.html")
#     else:
#         print(request.POST)
#         uname = request.POST.get("username")
#         pwd = request.POST.get("password")
#         if uname == "name" and pwd == "222":
#             return HttpResponse("登录成功")
#         else:
#             return HttpResponse("登录失败")
