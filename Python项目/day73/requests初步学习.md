+ 初识

  requests库是Python语言编写，基于urllib，采用Apache2 Licensed开源协议的HTTP库。

  它相对于urllib更加方便，大大节约了代码量，完全满足了HTTP测试相关需求。

  + 安装

    ```shell
    pip install requests
    pip install -i https://pypi.doubanio.com/simple/ requests
    ```

  + 测试

    ```python
    import requests   # 回车不报错就算安装成功
    response = requests.get("https://www.baidu.com")
    print(response.status_code)  # 200
    ```

  + requests库的主要方法

    | 方法               | 描述                           |
    | ------------------ | ------------------------------ |
    | requests.request() | 构造一个请求，支持以下各种方法 |
    | requests.get()     | 获取html的主要方法             |
    | requests.head()    | 获取html头部信息的主要方法     |
    | requests.post()    | 向html网页提交post请求的方法   |
    | requests.put()     | 向html网页提交put请求的方法    |
    | requests.patch()   | 向html提交局部修改的请求       |
    | requests.delete()  | 向html提交删除请求             |
    | requests.Session() | session相关                    |



+ 请求接受的参数
  requests.request(method, url, **kwargs)类能够构造一个请求，支持不同的请求方式。

  ```python
  import requests
  
  response = requests.request(method='get', url='https://www.baidu.com')
  print(response.status_code)
  ```

  + 常用参数
    + method：请求方式
    + url：请求URL
    + **kwargs
      + params：字典或者字节序列，作为参数增加到url中，使用这个参数可以把一些键值对以`k1=v1&k2=v2`的模式增加到url中，get请求中用的较多。
      + data：字典、字节序列或者文件对象，重点作为向服务器提供或提交资源，作为请求的请求体，与params不同放在url上不同。它也可以接受一个字符串对象。
      + json：json格式的数据，可以向服务器提交json类型的数据。
      + headers：字典，定义请求的请求头，比如可以headers字典定义user agent。
      + cookies：字典或者CookieJar。
      + auth：元组，用来支持HTTP认证功能。
      + files：字典，用来向服务器传输文件。
      + timeout：指定超时时间。
      + proxies：字典，设置代理服务器。
      + allow_redirects：开关，是否允许对URL进行重定向，默认为True。
      + stream：开关，是否对获取内容进行立即下载，默认为False，也就是立即下载。这里需要说明的，stream一般应用于流式请求，比如说下载大文件，不可能一次请求就把整个文件都下载了，不现实，这种情况下，就要设置`stream=True`，requests无法将连接释放回连接池，除非下载完了所有数据，或者调用了response.close。
      + verify：开关，用于SSL证书认证，默认为True。
      + cert：用于设置保存本地SSL证书路径。
  + 流式请求，指的不是请求是流，而是请求返回的数据流，返回一点取一点，而普通的请求是返回完毕你再取内容。

+ 响应对象支持的属性

  ```python
  import requests
  
  response = requests.request(method='get', url='http://www.httpbin.org/get')
  ```

  当一个请求被发送后，会有一个response响应。requests同样为这个response赋予了相关方法

  + response：响应对象。
  + response.status_code：请求返回状态码。
  + response.text：字符串形式的响应内容。
  + response.json()：返回响应的是json类型的数据，如果响应的类型不是json，则抛出`ValueError`。
  + response.content：二进制的响应内容。
  + response.iter_content(chunk_size)：生成器，在`stream=True`的情况下，当遍历生成器时，以块的形式返回，也就是一块一块的遍历要下载的内容。避免了遇到大文件一次性的将内容读取到内存中的弊端，如果`stream=False`，全部数据作为一个块返回。chunk_size参数指定块大小。
  + response.iter_lines()：生成器，当`stream=True`时，迭代响应数据，每次一行，也就是一行一行的遍历要下载的内容。同样避免了大文件一次性写入到内存中的问题。当然，该方法不安全。至于为啥不安全，咱也不知道，咱也不敢问，主要是[官网](https://2.python-requests.org//zh_CN/latest/api.html)上没说！经查，如果多次调用该方法，iter_lines不保证重新进入时的安全性，因此可能会导致部分收到的数据丢失。
  + response.cookies：响应中的cookie信息。
  + response.cookies.get_dict()：以字典的形式返回cookies信息。
  + response.cookies.items()：以列表的形式返回cookies信息。
  + response.headers：响应头字典。取其中的指定key，`response.headers.get('Content-Type', '哎呀，没取到！')`
  + response.reqeust：请求类型。
  + response.url：请求的URL。
  + response.reason：响应HTTP状态的文本原因。
  + response.encoding：响应结果的编码方式。
  + response.encoding = “gbk”：修该响应编码方式，比如说响应结果的编码是utf-8，通过这么`response.encoding = “gbk”`指定为gbk。
  + response.apparent_encoding：根据响应字节流中去chardet库中匹配，返回编码方式，并不保证100%准确。
  + response.history：以列表的形式返回请求记录。列表内的请求以最老到最新排序。