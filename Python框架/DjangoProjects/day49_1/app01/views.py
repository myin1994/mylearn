from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # num = 10
    num = 'hello'
    l1 = [11,22,33,44]
    d1 = {"name":"alex","age":88,"hobby":["dream","sleep","play"],"xx":""}
    return render(request,"home.html",locals())
    # return render(request,"home.html",{"l1":l1,"d1":d1})

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        if uname == "123" and pwd == "123":
            return HttpResponse("OK")
        else:
            return HttpResponse("GUN")

def base(request):
    return render(request,"base.html")

def menu01(request):
    return render(request,"menu01.html")

def test(request):
    return render(request,"test.html")

def tags(request):
    name = "alex"
    return render(request,"tags.html",locals())

def left_lead(request):
    # l1 = ["客户管理", "销售管理", 'xxoo']
    l1 = [[1,"客户管理"], [2,"销售管理"], [3,'xxoo']]
    l2 = [[4,"客户管理2"], [5,"销售管理2"], [6,'xxooxx']]
    return render(request,"left-lead.html",{"l1":l1,"l2":l2})