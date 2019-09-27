# hashlib -- 摘要算法，加密算法

# 功能：加密，校验一致性


# 加密方式：md5,sha1,sha256,sha512

# 1.内容相同，密文一定相同
# 2.加密的密文是不可逆的 -- 但是md5已被破解
# 3.明文转换为字节，再从字节转换为密文

import hashlib
# s = "1234567"
# s1 = s.encode("utf-8")
# m = hashlib.md5()  #选择加密方式-初始化一个加密方式
# print(m)
# m.update(s1)     #将要加密的内容添加到m中
# print(m.hexdigest())  #进行加密

# 简单的加密
# s = "宝元isaolddriver"
# md5 = hashlib.md5()
# md5.update(s.encode("utf-8"))
# print(md5.hexdigest())

# 固定加盐
# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# md5 = hashlib.md5("oldboy".encode("utf-8"))
# md5.update(pwd.encode("utf-8"))
# print(md5.hexdigest())

# 动态加盐
# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# md5 = hashlib.md5(user.encode("utf-8"))
# md5.update(pwd.encode("utf-8"))
# print(md5.hexdigest())
# 731982a033a5cc815ac03c8504abb748
# 731982a033a5cc815ac03c8504abb748

# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# sha1 = hashlib.sha1(user.encode("utf-8"))
# sha1.update(pwd.encode("utf-8"))
# print(sha1.hexdigest())

# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# sha256 = hashlib.sha256(user.encode("utf-8"))
# sha256.update(pwd.encode("utf-8"))
# print(sha256.hexdigest())

# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# sha256 = hashlib.sha256(user.encode("gbk"))  #编码不影响结果，内容影响
# sha256.update(pwd.encode("gbk"))
# print(sha256.hexdigest())

# import hashlib
# user = input("user:")
# pwd = input("pwd:")
# sha512 = hashlib.sha512(user.encode("utf-8"))
# sha512.update(pwd.encode("utf-8"))
# print(sha512.hexdigest())

# 一致性：校验
s = '宝元 is a old driver'
print(s.split())
import hashlib
# 直接 update
md5obj = hashlib.md5()
for i in s.split():
    md5obj.update(i.encode("utf-8"))
print(md5obj.hexdigest())  #213a4a0e2f69ac56db1ff6295f468e7d


s1 = '宝元 is a old driver'
s1 = s1.replace(" ","")
md5 = hashlib.md5()
md5.update(s1.encode("utf-8"))
print(md5.hexdigest())