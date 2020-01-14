import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper

def f(n):
    if n == 1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

@cal_time
def feb(n):
    return f(n)

def fib_list(n):
    li = [1,1]
    for i in range(2,n+1):
        li.append(li[-1]+li[-2])
    return li

# print(feb(50))
# print(fib_list(99))

def feb3(n):
    a = 1
    b = 1
    c = 1
    for i in range(2,n+1):
        c = a + b
        a,b = b,c
    return c


# print(feb3(2))

# print(list(range(2,-1)))



