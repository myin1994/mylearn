import os
import requests
from bs4 import BeautifulSoup
BASE_DIR = os.getcwd()

def make_path(url,target_path='picture'):
    dir_path = os.path.join(BASE_DIR, target_path)
    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)

    response = requests.get(url=url)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    div_obj = soup.find(name='div', attrs={'class': 'lb_box'})
    img_list = div_obj.find_all_next(name='dt')
    dic = {}
    for i in img_list:
        dir_name = i.find(name='img').get("alt").replace(" ", "-")
        dir_href = i.find(name='a').get("href")
        dic[dir_name] = dir_href
    return dic

def download_img(lst,name,dirname):
    for img in lst:
        img_url = img.get("src").replace("113x113",'740x-')
        img_content = requests.get(img_url).content
        file_name = img_url.rsplit('/', 1)[-1]
        file_path = os.path.join(BASE_DIR, dirname, name, file_name)
        try:
            with open(file_path, 'wb') as f:
                f.write(img_content)
                print(file_path, '爬取完毕')
        except OSError:
            print(file_path, '爬取失败')

def request_img(url,dirname):
    dic = make_path(url,dirname)
    for name, img_url in dic.items():
        dir_path = os.path.join(BASE_DIR, dirname, name)
        os.mkdir(dir_path)
        response2 = requests.get(url=img_url)
        text2 = response2.text
        soup2 = BeautifulSoup(text2, 'html.parser')
        div_obj2 = soup2.find(name='div', attrs={'class': 'overview'})
        if not div_obj2:
            continue
        img_list2 = div_obj2.find_all(name='img')
        download_img(img_list2, name,dirname)

if __name__ == '__main__':
    url = 'http://www.yesky.com/c/6_20491.shtml'
    request_img(url,'picture3')