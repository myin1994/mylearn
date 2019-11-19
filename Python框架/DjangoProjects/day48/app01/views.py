from django.shortcuts import render,HttpResponse,redirect
# from django.http import HttpResponse
from django.utils.decorators import method_decorator

# Create your views here.
def func(f):
    def foo(*args,**kwargs):
        print(11)
        ret = f(*args,**kwargs)
        print(22)
        return ret
    return foo

@func
def home(request):
    return HttpResponse("hello")

# def login(request):
#     if request.method == "GET":
#         return render(request,"login.html")
#     else:
#         username = request.POST.get("username")
#         password = request.POST.get("username")
#         if username == "111" and password == "222":
#             return redirect("/home/")
#         else:
#             return redirect("/login/")


from django.views import View


# @method_decorator(func,name="get")
class LoginViews(View):
    # @method_decorator(func)
    name = None
    def dispatch(self, request, *args, **kwargs):
        print(111)
        # print(request.META)
        ret = super().dispatch(request, *args, **kwargs)
        print(222)
        return ret

    # @classmethod
    # def func1(cls,f):
    #     def foo(*args, **kwargs):
    #         print(11)
    #         ret = f(*args, **kwargs)
    #         print(22)
    #         return ret
    #     return foo

    # @method_decorator(func)
    # cls.func1
    def get(self,request,n):
        print("接收参数",n)
        print("类变量name",self.name)
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "111" and password == "222":
            return redirect("/home/")
        else:
            return redirect("/login/")

import os
import uuid,hashlib
from day49 import settings
def get_unique_str():
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()
class Upload(View):
    def get(self,request):
        return render(request,"upload.html")

    def post(self,request):
        myfile = request.FILES.get('icon')
        print(myfile.name)
        filename = get_unique_str() + '.' + myfile.name.split('.')[-1]
        print(filename)

        # 文件路径
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        f = open(filepath, 'wb')
        for i in myfile.chunks():
            f.write(i)
        f.close()
        return HttpResponse('OK')