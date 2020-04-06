# scrapy爬虫框架常用settings配置

## 降低log级别

当进行通用爬取时，一般您所注意的仅仅是爬取的速率以及遇到的错误。 Scrapy使用 INFO log级别来报告这些信息。为了减少CPU使用率(及记录log存储的要求), 在生产环境中进行通用爬取时您不应该使用 DEBUG log级别。 不过在开发的时候使用 DEBUG 应该还能接受。

```
setting.py文件中设置LOG_LEVEL = 'INFO'
```

#### 日志管理

> LOG_ENABLED 默认: True，启用logging

> LOG_ENCODING 默认: ‘utf-8’，logging使用的编码

> LOG_FILE 默认: None，在当前目录里创建logging输出文件的文件名，例如：LOG_FILE = ‘log.txt’配置了这个文件，就不会在控制台输出日志了

> LOG_LEVEL 默认: ‘DEBUG’，log的最低级别，会打印大量的日志信息，如果我们不想看到太多的日志，可以提高log等级共五级：

> CRITICAL - 严重错误

> ERROR - 一般错误

> WARNING - 警告信息

> INFO - 一般信息

> DEBUG - 调试信息

> LOG_STDOUT 默认: False 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。例如，执行 print(“hello”) ，其将会显示到日志文件中

## 增加并发

**并发是指同时处理的request的数量。其有全局限制和局部(每个网站)的限制。Scrapy默认的全局并发限制对同时爬取大量网站的情况并不适用，因此您需要增加这个值。 增加多少取决于您的爬虫能占用多少CPU。 一般开始可以设置为 100 。不过最好的方式是做一些测试，获得Scrapy进程占取CPU与并发数的关系。 为了优化性能，您应该选择一个能使CPU占用率在80%-90%的并发数**

```
在setting.py文件中写上CONCURRENT_REQUESTS = 100，scrapy中默认的并发数是32
```

## 禁止重试

**对失败的HTTP请求进行重试会减慢爬取的效率，尤其是当站点响应很慢(甚至失败)时， 访问这样的站点会造成超时并重试多次。这是不必要的，同时也占用了爬虫爬取其他站点的能力。**

```
RETRY_ENABLED = False
```

## 减少下载超时

**如果您对一个非常慢的连接进行爬取(一般对通用爬虫来说并不重要)， 减小下载超时能让卡住的连接能被快速的放弃并解放处理其他站点的能力。**

```
DOWNLOAD_TIMEOUT = 15,其中15是设置的下载超时时间
```

## 禁止cookies

**除非您 真的 需要，否则请禁止cookies。在进行通用爬取时cookies并不需要， (搜索引擎则忽略cookies)。禁止cookies能减少CPU使用率及Scrapy爬虫在内存中记录的踪迹，提高性能。**

```
`COOKIES_ENABLED = False`
```



## 禁止重定向

**除非您对跟进重定向感兴趣，否则请考虑关闭重定向。 当进行通用爬取时，一般的做法是保存重定向的地址，并在之后的爬取进行解析。 这保证了每批爬取的request数目在一定的数量， 否则重定向循环可能会导致爬虫在某个站点耗费过多资源。**

```
REDIRECT_ENABLED = False
```

 

## 设置下载延迟

**单位秒，支持小数，一般都是随机范围：0.5DOWNLOAD_DELAY 到 1.5DOWNLOAD_DELAY 之间**

```
DOWMLOAD_DELY=3,设置延迟下载可以避免被发现
```

 

## 暂停和恢复爬虫

**初学者最头疼的事情就是没有处理好异常，当爬虫爬到一半的时候突然因为错误而中断了，但是这时又不能从中断的地方开始继续爬，顿时感觉心里日了狗，但是这里有一个方法可以暂时的存储你爬的状态，当爬虫中断的时候继续打开后依然可以从中断的地方爬，不过虽说持久化可以有效的处理，但是要注意的是当使用cookie临时的模拟登录状态的时候要注意cookie的有效期**

**只需要在setting.py中JOB_DIR=file_name其中填的是你的文件目录，注意这里的目录不允许共享，只能存储单独的一个spdire的运行状态，如果你不想在从中断的地方开始运行，只需要将这个文件夹删除即可**


**当然还有其他的放法：scrapy crawl somespider -s JOBDIR=crawls/somespider-1，这个是在终端启动爬虫的时候调用的，可以通过ctr+c中断，恢复还是输入上面的命令**

 

## 不遵守robots.txt

```
ROBOTSTXT_OBEY = Ture，是否遵守 robots.txt，一般修改为False
```

 

## 配置请求头

**在settings中取消注释即可**
**DEFAULT_REQUEST_HEADERS ： 设置默认的请求headers**

```
DEFAULT_REQUEST_HEADERS={{
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent':'......'   #在这里配置你的请求头
}}
```

 

# setting文件别的字段介绍

 

```python
SPIDER_MIDDLEWARES：爬虫中间层
DOWNLOADER_MIDDLEWARES：下载中间层

# pipeline里面可以配置多个，每一个spider都会调用所有配置的pipeline，后面配置的数字表示调用的优先级，数字越小，调用越早
ITEM_PIPELINES = {'项目名.pipelines.PipeLine类名': 300,}

# 开发模式时，启用缓存，可以提高调试效率。同样的请求，如果缓存当中有保存内容的话，不会去进行网络请求，直接从缓存中返回。**部署时一定要注释掉！！！**
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 并发（下面都是默认值）
CONCURRENT_ITEMS = 100 #  并发处理 items 的最大数量
CONCURRENT_REQUESTS_PER_DOMAIN = 8 # 并发下载任何单域的最大数量
CONCURRENT_REQUESTS_PER_IP = 0 # 并发每个IP请求的最大数量
CONCURRENT_REQUESTS_PER_IP 不为0时，这个延时是针对每个IP，而不是每个域
```

 

## pipelines的使用


**必须在settings中，添加**

```python
ITEM_PIPELINES = {
    'first_scrapy.pipelines.FirstScrapyPipeline': 300, # 优先级，数字越小，
                                                    优先级越高，越早调用范围 0-1000
}
```


**对象如下：**

```python
class FirstScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
```


**process_item**

```python
process_item(self, item, spider)： 处理item的方法， 必须有的！！！

参数：
item (Item object or a dict) ： 获取到的item
spider (Spider object) ： 获取到item的spider
返回    一个dict或者item
```


**open_spider**

```python
open_spider(self, spider) ： 当spider启动时，调用这个方法
参数：
spider (Spider object) – 启动的spider
```


**close_spider**

```python
close_spider(self, spider)： 当spider关闭时，调用这个方法
参数：
spider (Spider object) – 关闭的spider
```


**from_crawler**

```python
@classmethod
from_crawler(cls, crawler)
参数：
crawler (Crawler object) – 使用这个pipe的爬虫crawler`
```

 

#### 以下为pipelines文件，根据需要添加方法


[pipelines.py](http://pipelines.py/)

```python
# pipelines.py
from pymongo import MongoClient


class FirstScrapyPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        crawler()

    def open_spider(self, spider):
        self.client = MongoClient("***.***.***.**", 27017)
        # 数据库名admin
        self.db = self.client.test
        self.db.authenticate('user', password')
        self.my_set = self.db.my_set

    def process_item(self, item, spider):
        try:
            self.my_set.save(item["info"])
        except Exception as e:
            print(e)
        return item

    def close_spider(self, spider):
        self.client.close()
```

 

## 运行爬虫文件

##### 运行单个爬虫

```python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 18:07
# @Author  : 甄超锋
# @Email   : 4535@sohu.com
# @File    : run.py
# @Software: PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl lvdunspider".split())
```

##### 运行多个爬虫

```python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 18:07
# @Author  : 甄超锋
# @Email   : 4535@sohu.com
# @File    : run.py
# @Software: PyCharm

from LvdunSpider.spiders.lvdunspider import LvdunspiderSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider
process.crawl(LvdunspiderSpider)

# 启动爬虫，会阻塞，直到爬取完成
process.start()
```

 

## scrapy使用随机User-Agent


**使用python模块 fake-useragent 生成user-agent**

**安装：**

```python
pip install fake-useragent
```

**简单使用：**

```python
from fake_useragent import UserAgent
ua = UserAgent()
#ie浏览器的user agent
print(ua.ie)

#opera浏览器
print(ua.opera)

#chrome浏览器
print(ua.chrome)

#firefox浏览器
print(ua.firefox)

#safri浏览器
print(ua.safari)

#最常用的方式
#写爬虫最实用的是可以随意变换user-agent，
print(ua.random)
```

**在middleware中使用**

```python
import random
from scrapy import signals
from fake_useragent import UserAgent

class RandomUserAgentMiddleware(object):

    def __init__(self):
        self.agent = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.agent.random)
```

**在settings.py中启用**

**在 ‘DOWNLOADER_MIDDLEWARES’ 项中启用中间件**

```python
DOWNLOADER_MIDDLEWARES = {
   'LvdunSpider.middlewares.RandomUserAgentMiddleware': 543,
}
```

