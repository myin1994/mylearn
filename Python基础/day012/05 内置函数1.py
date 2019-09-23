# 内置函数：python帮助我们写了很多功能以供使用，避免重复
# all() #判断元素是否都为True
# print(all([1,2,3,4]))
# print(all([1,2,3,4,0]))

# any() #判断元素是否有一个为True
# print(any([1,2,4,0,5])) #True
# print(any([0,0,0,0,0])) #False

# print(bytes("你好",encoding="utf-8"))  #字符串转换字节
# print("你好".encode("utf-8"))

# callable()  #判断是否可调用
# print(callable(str))

# print(chr(116))  #根据当前编码 ---unicde 查看编码对应的内容
# print(ord("t"))  #查看内存对应的编码  单字符

# print(complex(20))  #复数
# print(type(complex(20)))  #复数

# print(divmod(20,3))   #返回元组(商，余数)

# msg ="1  + 2 -3  + 2**2 + 3%2 +3*2 + 3/2 +4//3"
# print(eval(msg))

# msg ="print('你好')" #禁用
# eval(msg)
#
# msg = """
# print(1)
# """
# print(exec(msg))

# print(frozenset({1,2,3,4,5})) #冻结集合
#
# dic = frozenset({3,4,5})
# print(dic)

# print(hash("你好"))
# print(hash(123))
# print((1,2))
# print(hash([12,3])) #报错

# help()  查看注释
# help(str.count)
# help(list)

# 进制转换
# print(oct(10)) #十进制转换8进制
# print(hex(30))  #十进制转换16进制
# print(int("0x1e",16))
# print(int(0x1e))

# print(pow(3,2)) #求幂 9

# repr()
# s = "123"
# s1 = 123
# print(repr(s))  #显示数据类型
# print(repr(s1))
#
# print(round(5.6))  #保留小数位，默认取整>0.5向上取
# print(round(5.4))
# print(round(5.51))
# print(round(1.5))

#重点内容
# abs()  #绝对值

# s = "你好"
# s1 = format(s,">20")  #居右
# s2 = format(s,"<20")  #居左
# s3 = format(s,"^20")  #居中
# print(s1)
# print(s2)
# print(s3)

# s = 18
# print(format(s,"08b"))  #bin
# print(format(s,"08o"))  #oct
# print(format(s,"08x"))  #hex
# print(format(s,"08d"))  #int

# enumerate()

# sum() #求和
print(sum([1,2,3,4,5],10))   #高阶函数,可设置起始值，默认为0

# dir(list)  #查看当前对象都有什么方法
# print(dir(str))












