# import requests
# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
  #访问网址
  url = 'http://www.baidu.com/link?url=T2eFz2MZ-RW_Fu8qCGI5-anz1ZAGOfbU0th5FYCHCGhnWJuUEwW__t46Ka7WYY6E'
  #这是代理IP
  proxy = {'http':'http://114.239.146.249:808'}
  #创建ProxyHandler
  proxy_support = request.ProxyHandler(proxy)
  #创建Opener
  opener = request.build_opener(proxy_support)
  #添加User Angent
  opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
  #安装OPener
  request.install_opener(opener)
  #使用自己安装好的Opener
  print(222)
  response = request.urlopen(url)
  #读取相应信息并解码
  html = response.read().decode("utf-8")
  #打印信息
  print(html)