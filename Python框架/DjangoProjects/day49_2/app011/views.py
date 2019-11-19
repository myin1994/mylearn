from django.shortcuts import render

# Create your views here.
def home(request):
    num = 100
    s = "hello world"
    l1 = [11,22,33]
    d1 = {"name":"alex","number":123}
    class A:
        balance = 2000
        def __init__(self,xx):
            self.xx = xx
        def play(self):
            return "who?"

    a = A("oo")
    file_size = 1234567
    xx = ""
    import datetime
    time = datetime.datetime.now()
    h5 = "<a href='http://www.baidu.com'>百度<a>"
    n = 4
    return render(request,"home.html",{"num":num,
                                       "s":s,
                                       "l1":l1,
                                       "d1":d1,
                                       "a":a,
                                       "xx":xx,
                                       "time":time,
                                       "file_size":file_size,
                                       "h5":h5,
                                       "n":n})