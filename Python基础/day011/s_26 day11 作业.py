"""
s_26 day11 作业
"""

"""
1.请写出下列代码的执行结果：
"""

"""
例一：
def func1():
	print('in func1')

def func2():
	print('in func2')

ret = func1
ret() #in func1
ret1 = func2
ret1() #in func2
ret2 = ret
ret3 = ret2
ret2() #in func1
ret3() #in func1
执行结果：验证正确
in func1
in func2
in func1
in func1
"""

"""
例二：

def func1():
    print('in func1')

def func2():
    print('in func2')

def func3(x,y):
    x()
    print('in func3')
    y()
	
print(111) #111
func3(func2,func1) #in func2 in func3 in func1
print(222) #222
执行结果：验证正确
"""

"""
例三（选做题）：

def func1():
    print('in func1')

def func2(x):
    print('in func2')
    return x

def func3(y):
    print('in func3')
    return y

ret = func2(func1) #in func2   返回func1的内存地址
ret() #in func1
ret2 = func3(func2)  #in func3  返回func2的内存地址
ret3 = ret2(func1)  #in func2  返回func1的内存地址
ret3() #in func1
执行结果：验证正确
"""

"""
例四:

def func(arg):
    return arg.replace('alex', '****')

def run():
    msg = "Alex和大家都是好朋友"
    result = func(msg)
    print(result)

run() #Alex和大家都是好朋友
data = run()  #Alex和大家都是好朋友 返回None
print(data) #None
看代码写结果： 一开始忽略了run()在等号右边也会打印，其余正确
"""
# i = "123"
# i.replace()
"""
例五:

data_list = []

def func(arg):
    return data_list.insert(0, arg)

data = func('绕不死你')  #返回值为['绕不死你']----错误   应该是None
print(data) #None
print(data_list) #['绕不死你']
看代码写结果：忽略了列表操作的返回值是None
"""

"""
例六:
def func():
    print('你好呀')
    return '好你妹呀'

func_list = [func, func, func]

for item in func_list:
    val = item() #循环一次打印一个'你好呀'  然后返回值为 '好你妹呀'，共3次
    print(val) #'好你妹呀'
看代码写结果：验证正确
"""

"""
例七:
def func():
    print('你好呀')
    return '好你妹呀'

func_list = [func, func, func]

for i in range(len(func_list)):
    val = func_list[i]()
    print(val)
看代码写结果：结果同例六，验证正确
"""

"""
例八:
def func():
    return '大烧饼'

def bar():
    return '吃煎饼'

def base(a1, a2):
    return a1() + a2()

result = base(func, bar)
print(result) #大烧饼吃煎饼
看代码写结果：验证正确
"""

"""
例九:

def func():
    for item in range(10):
        pass
    	return item
func() #返回值为0
看代码写结果：没有打印结果为空，若打印func()结果应该为0，验证正确
"""

"""
例十:

def func():
    for item in range(10):
        pass
    	yield item #生成0 1 2 3 4 5 6 7 8 9
func()
看代码写结果：使用生成器产生0 1 2 3 4 5 6 7 8 9；验证正确
"""
# def func():
#     for item in range(10):
#         pass
#         yield item #生成0 1 2 3 4 5 6 7 8 9
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))

"""
例十一:
item = '老男孩'
def func():
    item = 'alex'
    def inner():
        print(item)
    for inner in range(10): #最后inner = 9
        pass
    inner() #数字不能调用函数，报错 TypeError: 'int' object is not callable
func()
看代码写结果：一开始忽略了for循环中的变量最后的返回值会在下方被使用
"""

"""
例十二:

l1 = []
def func(args):
    l1.append(args)
    return l1
print(func(1)) #[1]
print(func(2)) #[1,2]
print(func(3)) #[1,2,3]
看代码写结果：每次调用会增加l1中的元素，列表本身没有改变,验证正确
"""

"""
例十三:

name = '宝元'
def func():
    global name
    name = '男神'
print(name) #宝元
func()
print(name) #男神
看代码写结果：第一次打印没有调用函数变量未改变，第二次修改了全局变量，变为男神--验证正确
"""

"""
例十四:

name = '宝元'
def func():
    print(name)
func() #宝元
看代码写结果：验证正确
"""

"""
例十五:(选做题)

name = '宝元'
def func():
    print(name) #UnboundLocalError: local variable 'name' referenced before assignment
    name = 'alex'
func()
看代码写结果：因为未声明修改全局变量报错

如果给一个变量分配一个值，则这个变量会被认为属于当前的代码块，会屏蔽外部代码块（全局）的相同名字的变量。
因为函数体中的代码中name = 'alex'，相当于给name分配了一个值，则编译器意识到name是一个局部变量，因为name在print后面被赋值，
则在之前调用的print(name)试图访问一个未被初始化的局部变量而失败。
解决方法：声明变量为global
"""

# name = '宝元'
# def func():
#     global name
#     print(name) #UnboundLocalError: local variable 'name' referenced before assignment
#     name = 'alex'
# func()

"""
例十六:

def func():
    count = 1
    def inner():
        nonlocal count
        count += 1
        print(count)
    print(count)
    inner()
    print(count)
func()
看代码写结果： 1   2 2  验证正确
"""

"""
例十七: (选做题)

def extendList(val,list=[]):
    list.append(val)
    return list

list1 = extendList(10)  #返回值为[10]
list2 = extendList(123,[])  #返回值为[123]
list3 = extendList('a') #返回值为["a"]

print('list1=%s'%list1) #list1=[10]
print('list2=%s'%list2) #list2=[123]
print('list3=%s'%list3) #list3=["a"]
看代码写结果：结果错误   正确结果[10,"a"]  [123]  [10,"a"]
通过查看调用函数是列表的地址变化，发现不覆盖默认值时每次列表的内存地址相同，所以造成两次结果被追加到同一列表下,猜想可变数据类型会有类似
的结果

默认陷阱（默认参数为可变数据类型）
相当于外部有一个列表绑定在函数上，使用默认值时会默认添加到绑定列表中
"""
# def extendList(val,list=[]):
#     list.append(val)
#     print(id(list))
#     print(list)
#     return list
#
# list1 = extendList(10)  #返回值为[10]
# print(list1)
# list2 = extendList(123,[])  #返回值为[123]
# print(list2)
# list3 = extendList('a') #返回值为["a"]
# print(list3)
# list4 = extendList(345,[])
# print(list4)
#
# print('list1=%s'%list1) #list1=[10]
# print('list2=%s'%list2) #list2=[123]
# print('list3=%s'%list3) #list3=["a"]

"""
例十八:

def extendList(val,list=[]):
    list.append(val)
    return list
print('list1=%s'% extendList(10))  #list1 = [10]  返回值后直接打印，结果不会受到影响
print('list2=%s'% extendList(123,[]))  #list2 = [123]
print('list3=%s'% extendList('a'))  #list1 = [10,"a"]
看代码写结果：第三个错误，在上题的基础上，没有变量接收返回值为什么列表也会同步修改呢
"""
# def extendList(val,list=[]):
#     list.append(val)
#     return list
# print('list1=%s'% extendList(10))  #list1 = [10]
# print('list2=%s'% extendList(123,[]))  #list2 = [123]
# print('list3=%s'% extendList('a'))  #list1 = [10,"a"]


"""
2.用你的理解解释一下什么是可迭代对象，什么是迭代器。

可迭代对象：可以按照顺序对其进行取值的对象，是数据本身，可以被直观的看到和操作(具备.iter()方法的对象)

迭代器：更像是产生数据的工厂，只能一个一个的进行取值，不知道内部数据的多少。（具备.iter()和.next()方法的对象）
"""

"""
3.使用while循环实现for循环的本质(面试题)
"""
# s = [1,2,3,4,5,6]
# d =iter(s)
# while True:
#     try:
#         print(next(d))
#     except StopIteration:
#         break


































