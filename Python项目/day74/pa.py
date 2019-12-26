"""
http://www.yesky.com/c/6_20491.shtml

pip install beautifulsoup4
"""
import os
import requests
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()
url = 'http://www.yesky.com/c/6_20491.shtml'
response = requests.get(url=url)
text = response.text
# print(text)
soup = BeautifulSoup(text, 'html.parser')
div_obj = soup.find(name='div', attrs={'class': 'lb_box'})
img_list = div_obj.find_all_next(name='dt')
dic = {}
# print(img_list)
for i in img_list:
    dir_name = i.find(name='img').get("alt").replace(" ","-")
    dir_href = i.find(name='a').get("href")
    dic[dir_name] = dir_href
# print(dic)

for k,v in dic.items():
    dir_path = os.path.join(BASE_DIR, 'img', k)
    os.mkdir(dir_path)
    response2 = requests.get(url=v)
    # response2.encoding = 'ISO-8859-1'
    text2 = response2.text
    soup2 = BeautifulSoup(text2, 'html.parser')
    div_obj2 = soup2.find(name='div', attrs={'class': 'overview'})
    # print(div_obj2)
    img_list2 = div_obj2.find_all(name='img')
    # print(img_list2)
    for img in img_list2:
        img_url = img.get("src")
        img_content = requests.get(img_url).content
        file_name = img_url.rsplit('/',1)[-1]
        file_path = os.path.join(BASE_DIR, 'img',k,file_name)
        print(file_path)
        try:
            with open(file_path,'wb') as f:
                f.write(img_content)
                print(file_name,'爬取完毕')
        except OSError:
            print(file_name,'爬取失败')








# for img in img_list:
#     img_url = img.get("src")
#     img_content = requests.get(img_url).content
#
#     file_name = img_url.rsplit('/',1)[-1]
#     file_path = os.path.join(BASE_DIR, 'img',file_name)
#     try:
#         with open(file_path,'wb') as f:
#             f.write(img_content)
#             print(file_name,'爬取完毕')
#     except OSError:
#         print(file_name,'爬取失败')
