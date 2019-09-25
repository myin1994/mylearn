def f1(func): #func = index
    def f2(*args,**kwargs):
        print("f1装饰开始")
        func(*args,**kwargs)
        print("f1装饰结束")
    return f2

def foo1(func):
    def foo2(*args,**kwargs):
        print("foo1装饰开始")
        func(*args,**kwargs)
        print("foo1装饰结束")
    return foo2
#多个装饰器装饰一个函数时，先执行离被装饰函数最近的装饰器
@foo1  # index = foo1(index)  index = foo1(f2) =foo2
@f1  #index = f1(index)   index = f2
def index():
    print("is index")
index()
# U型法执行