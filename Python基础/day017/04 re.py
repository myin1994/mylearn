import re
# s = "alex,meet,meva_j"
# print(re.findall("e",s)) #参数1：要查找的内，参数2：从哪查找
# print(re.findall("ee",s)) #参数1：要查找的内，参数2：从哪查找



# s = "alex,你 好met2,m_j@!"
# print(re.findall("\w",s))  #匹配非特殊符号(中文，字母，数字，下划线)
# print(re.findall("\W",s))  #匹配特殊符号

# print(re.findall("\s",s)) #匹配空格
# print(re.findall("\S",s)) #匹配非空格（包括特殊符号）

# print(re.findall("\d",s))  #数字
# print(re.findall("\D",s))  #非数字

# print(re.findall("\Aal",s))  #以xx开头
# print(re.findall("^a",s))  #匹配开头
#                                     配合使用
# print(re.findall("!\Z",s))  #以xx结尾
# print(re.findall("j@!$",s))  #以xx结尾

# print(re.findall("^al.*!$",s))

# 以什么开头，以什么结尾 Django中使用
# s = "你好e\teet\n"
# print(re.findall("\t",s))  #匹配\t
# print(re.findall("\n",s))  #匹配\t

# print(re.findall(".",s))  #任意字符(换行符除外)
#
# print(re.findall(".",s,re.DOTALL))  #任意字符(包括换行符)

# s = "1234!abcd-ABC@_"
# print(re.findall("[0-9]",s))  #[数字0-数字9]范围
# print(re.findall("[0-9a-zA-Z]",s))  #[数字0-数字9a-zA-Z]范围
# print(re.findall("[-!0-9@]",s))  #包含符号
# s = "a.le-1-3x,你  好e\teet29,mev3a_j@!"
# print(re.findall("[^0-9]",s))  #取反，不要0-9
# print(re.findall("[^a-z^1-9^A^!]",s))  #取反，不要0-9
# s = "1,3,5.6.7"
# print(re.findall("[.]",s))  #[] 中.失效
# print(re.findall("[^.]",s))  #[] 中.失效

# s = "a.le-1-3x,你  好e\teeet29,mev3a_j@!"
#
# print(re.findall("e*",s))  #贪婪匹配左边字符  *代表0-∞个e

# s = "1234e678eeee"
# print(re.findall("e*",s))  #匹配  *代表0-∞个e
#
# # s = "1234e678eeee"
# print(re.findall("e+",s))  #匹配  1-正无穷

# s = "1234e678eeee"
# print(re.findall("e?",s))  #?  0-1  非贪婪

# s = "123e4e67ee8eeeee"
# print(re.findall("e{2}",s))  #取x个
# print(re.findall("e{0,3}",s)) #从大到小的个数范围匹配

# s = "123aa4e678eeeev"
# print(re.findall("aa|e|v",s))  #找aa或e或v

# s = "1-2*(60+(-40.35/5)-(-4*3))"
#
# print(re.findall("\d+",s))
# print(re.findall("-?\d+\.\d+|-?\d+",s))




# print(re.findall("-\d+\.+\d+|\d+\.+\d+|-?\d+",s))
# #
# print(re.findall(r'-?\d+\.?\d*|\d*\.?\d+', "1-2*(60+(-40.35/5)-(-4*3))"))

# s = "1lealea23lsssea"
# print(re.findall("(e)",s))  #找e
# print(re.findall("l(e)a",s))  #找a或e
# print(re.findall("l(e)a|s(e)a|l(s)s",s))  #找a或e

# 练习
# s = 'alex_sb ale123_sb wu12sir_sb wusir_sb ritian_sb'
# print(re.findall(" ?(.+?)_sb",s))
#
# # print(re.findall("(.+)_sb",s))
# print(re.findall("\s?(.+?)_sb",s))
#
# s = "1-2*(60+(-40.35/5)-(-4*3))"
# print(re.findall("\d+",s))
# # \. ==转义成普通的小数点
# print(re.findall("\d+\.\d+|\d+",s))  #一个规则获取一种
# # 匹配所有的数字（包含小数包含负号）
# print(re.findall("-\d+\.\d+|-\d+|\d+",s))

# s = "http://blog.csdn.net/make164492212@163.com/article/details/51656638" #匹配所有邮箱
# print(re.findall("/(ma.+com)/",s))
# print(re.findall("\w+@\d+\.com",s))

# s = """
# 时间就是1995-04-27,2005-04-27
# 1999-04-27 老男孩教育创始人
# 老男孩老师 alex 1980-04-27:1980-04-27
# 2018-12-08
# """
# print(re.findall("\d{4}-\d{2}-\d{2}",s))
# print(re.findall("\d+-\d+-\d+",s))


# print(re.findall("\d+-\d+-\d+",s))
# print(re.findall("\d+-\d+-\d+:\d+-\d+-\d+",s))
# print(re.findall("x (\S+)\n",s))

# s ="ddd12.33,22.3,ffff4.6,ggg222"
# print(re.findall("\d+\.+\d+",s))

# 匹配qq号：腾讯从10000开始：
# s = "222222,33333,4444,5555555,9999,999999"
# print(re.findall("\d{5,11}",s))
#
# print(re.findall("\d{5,11}",s))

s1 = '''
<div id="cnblogs_post_body" class="blogpost-body"><h3><span style="font-family: 楷体;">python基础篇</span></h3>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6847032.html" target="_blank">python 基础知识</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6627631.html" target="_blank">python 初始python</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/articles/7087609.html" target="_blank">python 字符编码</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6752157.html" target="_blank">python 类型及变量</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6847663.html" target="_blank">python 字符串详解</a></strong></span></p>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6850347.html" target="_blank">python 列表详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6850496.html" target="_blank">python 数字元祖</a></strong></span></p>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6851820.html" target="_blank">python 字典详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6852131.html" target="_blank">python 集合详解</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087614.html" target="_blank">python 数据类型</a>&nbsp;</strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6752169.html" target="_blank">python文件操作</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/8149209.html" target="_blank">python 闭包</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6705714.html" target="_blank">python 函数详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087616.html" target="_blank">python 函数、装饰器、内置函数</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087629.html" target="_blank">python 迭代器 生成器</a>&nbsp;&nbsp;</strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6757215.html" target="_blank">python匿名函数、内置函数</a></strong></span></p>
</div>
'''
# 1,找到所有的span标签的内容
# print(re.findall("<span.*?>(.*)</span>",s1))
# print(re.findall('href="(.*\.html)',s1))
# 2,找到所有a标签对应的url
# print(re.findall('<a href="(.*?)".*?</a>',s1))

# print(re.findall('href="(.+)" ',s1))
# print(re.findall('href="(?:.+)" ',s1))
# print(re.findall('href="(?:.+?)"',s1))


# 常用方法
# search:从字符串任意位置进行匹配，查找到一个就停止

# 什么是贪婪匹配：+  *
# 什么是非贪婪  ?
# 控制贪婪 +?

# search  和 match的区别
# s1 = "alexmeet"
# print(re.findall("e",s1))
# print(re.search("e",s1).group())

# match  从字符串开始位置进行匹配，找不到返回None
# s1 = "alexmeet"
# print(re.match("e",s1))
# print(re.match("a",s1).group())

# split  分割，定义一批分隔符
# print(re.split('[ ：:,;；，]','alex wusir,日天，太白;女神;肖锋：吴超'))


# sub 替换
# print(re.sub('barry', 'meet', 'barry是最好的讲师，barry就是一个普通老师，请不要将barry当男神对待。'))


# compile 定义匹配规则
# boj = re.compile("\d{2}")
# print(boj.findall("dddd222ddfff"))

# finditer
# a = re.finditer("e","meet,alex")
# print(next(a).group())
# print(next(a).group())
# print(next(a).group())
# print(next(a).group())


# 给分组取名字
# ret = re.search("<\w+>\w+</\w+>","<h1>hello</h1>").group()
# print(ret)
# ret = re.search("<(?P<tag_name>\w+)>\w+</\w+>","<h1>hello</h1>")
# print(ret.group("tag_name"))
# print(ret.group())