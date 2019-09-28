# 1.序列化
# json（重点）

# dumps loads 用于网络传输
# dump load 用于文件存储

# pickle
# dumps loads 用于网络传输
# dump load 用于文件存储

# json获取的是字符串,pickle获取的是特殊字节


# 将一些特殊数据,进行转换

# hashlib
# 加密:
# md5,sha1,sha256,sha512
# 字符串 -- 字节 -- 密文
# 加密不可逆
# import hashlib
# md5 = hashlib.md5("盐".encode("utf-8"))
# md5.update("加密内容".encode("utf-8"))
# print(md5.hexdigest())

# 加盐：
#     固态加盐
#     动态加盐

# collection
# 1.Counter统计成字典
# 2.有序字典 Orderdict
# 3.默认字典 defaultdict
# 4.双端队列 队列，栈
# 5.命名元组

# 软件开发规范
"""
-blog
--bin #启动文件存放位置
---start.py
--core #主逻辑
---src.py
--conf  #配置文件，静态文件
---setting
--lib #公共组件
---common
--db  #用户数据
---userinfo.txt
--log
---a.log
-README
"""