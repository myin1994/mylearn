import requests
import re

# ret = requests.get("http://www.baidu.com") #,headers=None
# with open("百度.html","wb") as f:
#     f.write(ret.content)
# print(ret.text)

def bookre(path,read,rule,encode="utf-8"):
    with open(path,read,encoding=encode) as f:
        return re.findall(rule, f.read())

ret = requests.get("https://www.80txt.la/txtml_20132.html") #,headers=None

with open("001.html","wb") as f:
    f.write(ret.content)

book_lst = bookre("001.html","r",'href="(.*)">第',encode="utf-8")

for i in book_lst:
    ret = requests.get(i)
    path = f"第{book_lst.index(i)+1}章.txt"
    with open(path, "wb") as f:
        f.write(ret.content)
    content_lst = bookre(path,"r",'&nbsp;&nbsp;&nbsp;&nbsp;(.*)<br />',encode="utf-8")
    print(content_lst)
    # with open(path, "w") as f:
    #     f.write("".join(content_lst))

    break

# print(ret.text)
# book_lst =re.findall("^hr(.*)",ret.text)
# # book_lst =re.findall("<li><a rel='nofollow' href='(.*)",ret.text)
# print(book_lst)
# with open("百度.html","wb") as f:
#     f.write(ret.content)
# print(ret.text)