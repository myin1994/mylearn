# 异步爬虫

## 基于线程池

### Flask的基本使用

- 环境安装：pip install flask

- 创建一个py源文件

  ```python
  from flask import Flask,render_template
  from time import sleep
  #实例化一个app
  app = Flask(__name__)
  
  #创建视图函数&路由地址
  @app.route('/bobo')
  def index_1():
      sleep(2)
      return render_template('test.html')
  
  @app.route('/jay')
  def index_2():
      sleep(2)
      return render_template('test.html')
  
  @app.route('/tom')
  def index_3():
      sleep(2)
      return render_template('test.html')
  
  if __name__ == "__main__":
      #debug=True表示开启调试模式：服务器端代码被修改后按下保存键会自动重启服务
      app.run(debug=True)
  ```

- 官方文档：https://dormousehole.readthedocs.io/en/latest/

### 线程池使用

+ 使用方法

  + 引入模块  `from multiprocessing.dummy import Pool`
  + 添加线程 `map(callback,alist)`
    + 可以使用callback对alist中的每一个元素进行指定形式的异步操作

+ 示例

  ```python
  import requests
  import time
  
  from multiprocessing.dummy import Pool
  urls = [
          'http://127.0.0.1:5000/bobo',
          'http://127.0.0.1:5000/jay',
          'http://127.0.0.1:5000/tom'
      ]
  def get_request(url):
      page_text = requests.get(url=url).text
      return len(page_text)
  
  if __name__ == "__main__":
      start = time.time()
      pool = Pool(3) #3表示开启线程的数量
      #使用get_request作为回调函数，需要基于异步的形式对urls列表中的每一个列表元素进行操作
      #保证回调函数必须要有一个参数和返回值
      result_list = pool.map(get_request,urls)
      print(result_list)
      print('总耗时：', time.time() - start)
  ```

  

## 基于单线程+多任务的异步爬虫

### asyncio协程

+ 模块安装 `pip install asyncio`

+ 基本概念

  + 特殊的函数

    - 如果一个函数的定义被async修饰后，则该函数就变成了一个特殊的函数
    - 特殊之处
      - 该特殊的函数被调用后，函数内部的实现语句不会被立即执行
      - 该特殊函数被调用后会返回一个协程对象

  + 协程对象

    - 通过特殊函数的调用返回一个协程对象。

      ```python
      import asyncio
      import time
      
      async def get_request(url):
          print('正在请求的url：',url)
          time.sleep(2)
          print('请求结束：',url)
          return 'bobo'
      
      c = get_request('www.1.com') #c就是一个协程对象
      ```

    - 协程 == 特殊函数 == 一组指定的操作

    - 协程 == 一组指定的操作

  + 任务对象

    - 任务对象就是一个高级的协程对象。（任务对象就是对协程对象的进一步封装）

    - 任务 == 协程 == 特殊函数 == 一组指定操作

    - 任务 == 一组指定的操作

    - 如何创建一个任务对象

      - asyncio.ensure_future(协程对象)

        ```python
        import asyncio
        import time
        
        async def get_request(url):
            print('正在请求的url：',url)
            time.sleep(2)
            print('请求结束：',url)
            return 'bobo'
        
        c = get_request('www.1.com') #c就是一个协程对象
        task = asyncio.ensure_future(c) #任务对象就是对协程对象的进一步封装
        ```

    - 任务对象的高级之处

      - 可以给任务对象绑定回调

        - task.add_done_callback(task_callback)

          ```python
          import asyncio
          import time
          
          async def get_request(url):
              print('正在请求的url：',url)
              time.sleep(2)
              print('请求结束：',url)
              return 'bobo'
          
          #回调函数的封装
          #参数t：就是该回调函数的调用者（任务对象）
          def task_callback(t):
              print('i am task_callback(),参数t：',t)
              #result返回的就是特殊函数的返回值
              print('t.result()返回的是：',t.result())
          
          c = get_request('www.1.com') #c就是一个协程对象
          task = asyncio.ensure_future(c) #任务对象就是对协程对象的进一步封装
          task.add_done_callback(task_callback) #给task绑定一个回调函数
          ```

        - 回调函数的调用时机

          - 任务被执行结束后，才可以调用回调函数

        - 回调函数的参数只可以有一个

          - 表示的就是该回调函数的调用者（任务对象）

        - 使用回调函数的参数调用result()返回的就是任务对象表示的特殊函数return的结果

        - 注意：回调函数的执行是同步的（不会进行cpu切换）

  + 事件循环对象

    - 作用

      - 可以将多个任务对象注册/装载到事件循环对象中
      - 如果开启了事件循环后，则其内部注册/装载的任务对象表示的指定操作就会被基于异步的被执行

    - 创建方式

      - loop = asyncio.get_event_loop()

    - 注册且启动方式

      - loop.run_until_complete(task)

      ```python
      import asyncio
      import time
      
      async def get_request(url):
          print('正在请求的url：',url)
          time.sleep(2)
          print('请求结束：',url)
          return 'bobo'
      
      #回调函数的封装
      #参数t：就是该回调函数的调用者（任务对象）
      def task_callback(t):
          print('i am task_callback(),参数t：',t)
          #result返回的就是特殊函数的返回值
          print('t.result()返回的是：',t.result())
      
      c = get_request('www.1.com') #c就是一个协程对象
      task = asyncio.ensure_future(c) #任务对象就是对协程对象的进一步封装
      task.add_done_callback(task_callback) #给task绑定一个回调函数
      loop = asyncio.get_event_loop() #创建事件循环对象
      loop.run_until_complete(task) #将任务对象注册到事件循环中且开启事件循环
      ```

+ 多任务操作

  + 添加多任务的方法---`asyncio.wait()`

    + 将任务列表中的任务对象赋予可被挂起的权限。只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起
      - 挂起：将当前的任务对象交出cpu的使用权。

  + await关键字

    + 在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断整个异步效果
    + 在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰。await就可以保证阻塞操作在异步执行的过程中不会被跳过！

  + 代码示例

    ```python
    import  time
    import requests
    import asyncio
    
    async def get_request(url):
        print('正在请求的url：',url)
        await asyncio.sleep(2)
        print('请求结束：',url)
        return 'bobo'
    urls = [
        'www.1.com',
        'www.2.com',
        'www.3.com'
    ]
    if __name__ == "__main__":
        start = time.time()
        tasks = [] #多任务列表
        #1.创建协程对象
        for url in urls:
            c = get_request(url)
            #2.创建任务对象
            task = asyncio.ensure_future(c)
            tasks.append(task)
    
        #3.创建事件循环对象
        loop = asyncio.get_event_loop()
        # loop.run_until_complete(tasks)
        #必须使用wait方法对tasks进行封装才可以
        loop.run_until_complete(asyncio.wait(tasks))
        print('总耗时：',time.time()-start)
    ```

### 结合aiohttp进行多任务异步爬虫

+ 模块介绍

  + 是一个支持异步的网络请求模块
  + 安装 `pip install aiohttp`

+ 使用

  + 1.写出一个大致的架构

    ```python
    async def get_request(url):
        #实例化好了一个请求对象
        with aiohttp.ClientSession() as sess:
            #调用get发起请求，返回一个响应对象
            #get/post(url,headers,params/data,proxy="http://ip:port")
            with sess.get(url=url) as response:
                #获取了字符串形式的响应数据
                page_text = response.text()
                return page_text
    ```

  + 2.补充细节

    - 在阻塞操作前加上await关键字
    - 在每一个with前加上async关键字

  + 完整代码

    ```python
    import requests
    import asyncio
    import time
    import aiohttp
    from lxml import etree
    urls = [
        'http://localhost:5000/bobo',
        'http://localhost:5000/tom',
        'http://localhost:5000/jay'
    ]
    
    async def get_request(url):
        #实例化好了一个请求对象
        async with aiohttp.ClientSession() as sess:
            #调用get发起请求，返回一个响应对象
            #get/post(url,headers,params/data,proxy="http://ip:port")
            async with await sess.get(url=url) as response:
                #text()获取了字符串形式的响应数据
                #read()获取byte类型的响应数据
                page_text = await response.text()
                return page_text
    
    #解析函数的封装
    def parse(t):
        #获取请求到页面源码数据
        page_text = t.result()
        tree = etree.HTML(page_text)
        parse_text = tree.xpath('//a[@id="feng"]/text()')[0]
        print(parse_text)
    
    if __name__ == "__main__":
        start = time.time()
        tasks = []
        for url in urls:
            c = get_request(url)
            task = asyncio.ensure_future(c)
            task.add_done_callback(parse)
            tasks.append(task)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        print('总耗时：',time.time()-start)
    ```

+ 多任务爬虫的数据解析

  多任务的架构中数据的爬取是封装在特殊函数中，我们一定要保证数据请求结束后，再使用任务对象的回调函数实现数据解析。

+ 使用多任务的异步协程爬取数据实现套路

  - 先使用requests模块将待请求数据对应的url封装到有个列表中（同步）
  - 再使用aiohttp模式将列表中的url进行异步的请求和数据解析（异步）

### 结合requests进行多任务异步爬虫

+ learn link：https://blog.csdn.net/J_Object/article/details/78880610?utm_source=blogxgwz7

+ 代码实现

  ```python
  import requests
  import asyncio
  import time
  from functools import partial
  urls = [
      'http://localhost:5000/bobo',
      'http://localhost:5000/tom',
      'http://localhost:5000/jay',
      'http://app.cnstock.com/api/waterfall?callback=jQuery191019474229271592014_1581644154107&colunm=qmt-smk_xt&page=4&num=10&showstock=0&_=1581644154111'
      ]
  
  headers = {
      "Referer": "http://stock.cnstock.com/xt"
  }
  async def get_request(url):
      loop = asyncio.get_event_loop()
      response = await loop.run_in_executor(None, partial(requests.get,url=url,headers=headers))#使用partial传递多个参数
      print(response.status_code)
      page_text = response.text
      return page_text
  
  #解析函数的封装
  def parse(t):
      #获取请求到页面源码数据
      page_text = t.result()
      print(page_text)
  
  if __name__ == "__main__":
      start = time.time()
      tasks = []
      for url in urls:
          c = get_request(url)
          task = asyncio.ensure_future(c)
          task.add_done_callback(parse)
          tasks.append(task)
      loop = asyncio.get_event_loop()
      loop.run_until_complete(asyncio.wait(tasks))
      print('总耗时：',time.time()-start)
  ```

  

# selenium

## 基础使用

- 概念：基于浏览器自动化的模块

- 自动化：可以通过代码指定一些列的行为动作，然后将其作用到浏览器中。

- pip install selenium

- selenium和爬虫之间的关联

  - 1.便捷的捕获到任意形式动态加载的数据（可见即可得）
  - 2.实现模拟登录

- 谷歌驱动下载：<http://chromedriver.storage.googleapis.com/index.html>

- 基本使用

  ```python
  from selenium import webdriver
  from time import sleep
  from lxml import etree
  
  #1.基于浏览器的驱动程序实例化一个浏览器对象
  bro = webdriver.Chrome(executable_path='./chromedriver')
  #对目的网站发起请求
  bro.get('https://www.jd.com/')
  #标签定位
  search_text = bro.find_element_by_xpath('//*[@id="key"]')
  search_text.send_keys('iphoneX') #向标签中录入数据
  
  btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
  btn.click()
  
  sleep(2)
  
  #在搜索结果页面进行滚轮向下滑动的操作（执行js操作：js注入）
  bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  sleep(2)
  bro.quit()
  ```

  ```python
  from selenium import webdriver
  from time import sleep
  
  # 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
  driver = webdriver.Chrome(r'./chromedriver')
  # 用get打开百度页面
  driver.get("http://www.baidu.com")
  # 查找页面的“设置”选项，并进行点击
  driver.find_elements_by_link_text('设置')[0].click()
  sleep(2)
  # # 打开设置后找到“搜索设置”选项，设置为每页显示50条
  driver.find_elements_by_link_text('搜索设置')[0].click()
  sleep(2)
  
  # 选中每页显示50条
  m = driver.find_element_by_id('nr')
  sleep(2)
  m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
  m.find_element_by_xpath('.//option[3]').click()
  sleep(2)
  
  # 点击保存设置
  driver.find_elements_by_class_name("prefpanelgo")[0].click()
  sleep(2)
  
  # 处理弹出的警告页面   确定accept() 和 取消dismiss()
  driver.switch_to_alert().accept()
  sleep(2)
  # 找到百度的输入框，并输入 美女
  driver.find_element_by_id('kw').send_keys('美女')
  sleep(2)
  # 点击搜索按钮
  driver.find_element_by_id('su').click()
  sleep(2)
  # 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
  driver.find_element_by_xpath('//*[@id="1"]/div[1]/a[1]/img').click()
  sleep(3)
  
  # 关闭浏览器
  driver.quit()
  ```

- 如何捕获动态加载的数据

  - 药监总局为例：<http://125.35.6.84:81/xk/>
  - 前三页所有企业名称爬取

  ```python
  url = 'http://125.35.6.84:81/xk/'
  bro = webdriver.Chrome(executable_path='./chromedriver')
  bro.get(url)
  page_text_list = []#每一页的页面源码数据
  sleep(1)
  #捕获到当前页面对应的页面源码数据
  page_text = bro.page_source #当前页面全部加载完毕后对应的所有的数据
  page_text_list.append(page_text)
  
  #点击下一页
  for i in range(2):
      next_page = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
      next_page.click()
      sleep(1)
      page_text_list.append(bro.page_source)
  for page_text in page_text_list:
      tree = etree.HTML(page_text)
      li_list = tree.xpath('//*[@id="gzlist"]/li')
      for li in li_list:
          name = li.xpath('./dl/@title')[0]
          print(name)
  sleep(2)
  bro.quit()
  ```

- selenium的弊端：效率低

- 动作链ActionChains：一系列连续的动作（滑动动作）

  ```python
  from selenium.webdriver import ActionChains #动作链
  
  url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
  bro = webdriver.Chrome(executable_path='./chromedriver')
  bro.get(url)
  sleep(1)
  #如果通过find系列的函数进行标签定位，如果标签是存在于iframe下面，则会定位失败
  #解决方案：使用switch_to即可
  bro.switch_to.frame('iframeResult')
  div_tag = bro.find_element_by_xpath('//*[@id="draggable"]')
  
  #对div_tag进行滑动操作
  action = ActionChains(bro)
  action.click_and_hold(div_tag)#点击且长按
  
  for i in range(6):
      #perform让动作链立即执行
      action.move_by_offset(10,15).perform()
      sleep(0.5)
  bro.quit()
  ```

  

## selenium规避检测

+ 有的网站会检测请求是否为selenium发起，如果是的话则让该次请求失败

+ 规避检测的方法：

  - selenium接管chrome浏览器

+ 实现步骤

  - 1.必须将你电脑中安装的谷歌浏览器的驱动程序所在的目录找到。且将目录添加到环境变量中。

  - 2.打开cmd，在命令行中输入命令：

    - chrome.exe --remote-debugging-port=9222 --user-data-dir="一个空文件夹的目录"
    - 指定执行结束后，会打开你本机安装好的谷歌浏览器。

  - 3.执行如下代码：可以使用下属代码接管步骤2打开的真实的浏览器

    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
     
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    #本机安装好谷歌的驱动程序路径
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=chrome_options)
    print(driver.title)
    ```

    

## 无头浏览器（无可视化界面的浏览器）

- 谷歌无头浏览器（推荐）

- phantomJs

- 代码实现

  ```python
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  import time
   
  # 创建一个参数对象，用来控制chrome以无界面模式打开
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
   
  # 创建浏览器对象
  browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
   
  # 上网
  url = 'https://www.baidu.com/'
  browser.get(url)
  time.sleep(3)
  #截图
  browser.save_screenshot('baidu.png')
  print(browser.page_source)
  browser.quit()
  ```

## 案例

### 12306模拟登录

+ url:<https://kyfw.12306.cn/otn/login/init>

+ 分析：主要是对验证码的处理

  - 基于selenium实现。
  - 需要使用selenium将登录页面打开
  - 我们即将实现的模拟登录页面和验证码图片一定是一一匹配
    - 验证码每次请求都会发生变化
  - 如何保证我们捕获的验证码和当次登录是一一匹配？
    - 将当前selenium打开的登录页面中的验证码图片裁剪下来即可。
    - 然后使用大码平台获取结果坐标

+ 代码实现

  + 引入环境及工具

    ```python
    #!/usr/bin/env python
    # coding:utf-8
    
    import requests
    from hashlib import md5
    
    class Chaojiying_Client(object):
    
        def __init__(self, username, password, soft_id):
            self.username = username
            password =  password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }
    
        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
            return r.json()
    
        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()
    
    def tranformImgCode(imgPath,imgType):
        chaojiying = Chaojiying_Client('prcrmb', '1994429zm', '904147')
        im = open(imgPath, 'rb').read()
        return chaojiying.PostPic(im,imgType)['pic_str']
    
    
    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from time import sleep
    from PIL import Image
    import re
    ```

  + 主逻辑

    ```python
    bro = webdriver.Chrome(executable_path='./chromedriver')
    bro.get('https://kyfw.12306.cn/otn/login/init')
    sleep(2)
    bro.maximize_window()
    sleep(2)
    #将当次登录对应的验证码图片进行裁剪
    bro.save_screenshot('main.png')#当前登录页面对应的完整图片
    #定位到了验证码图片对应的标签
    img_tag = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
    #裁剪出验证码图片
    x, y = img_tag.location.values()#img_tag表示的图片在当前页面中左下角坐标
    x = x *1.25 #windows下按照具体情况进行同比例缩放
    y = y *1.25
    h, w = img_tag.size.values() #验证码图片的尺寸
    h = h * 1.25
    w = w * 1.25
    #基于location和size制定出裁剪的范围
    rangle = (x,y,x+w,y+h)
    #根据rangle表示的裁剪范围进行图片的裁剪
    #基于图片进行裁剪：pip install PIL/Pillow
    i = Image.open('./main.png')
    frame = i.crop(rangle)
    frame.save('./code.png')
    #识别验证码图片
    #result是返回需要点击的坐标
    result = tranformImgCode('./code.png',9004)
    print(result)
    #61,71|118,137==>[[61,71],[118,137]]
    all_list = [re.findall("\d+",i) for i in result.split("|")]
    all_list = [[int(i[0])/1.25,int(i[1])/1.25] for i in all_list] #windows下按照具体情况进行同比例缩放
    for xy in all_list:
        x = xy[0]
        y = xy[1]
        ActionChains(bro).move_to_element_with_offset(img_tag,x,y).click().perform()
        sleep(1)
    print(all_list)
    bro.find_element_by_id('username').send_keys('bobo123')
    sleep(1)
    bro.find_element_by_id('password').send_keys('123456')
    sleep(1)
    bro.find_element_by_id('loginSub').click()
    sleep(2)
    bro.quit()
    ```

    

### 12306余票检测

```python
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
city = {
        '北京北': 'VAP',
        '北京东': 'BOP',
        '北京': 'BJP',
        '北京南': 'VNP',
        '北京西': 'BXP',
        '广州南': 'IZQ',
        '重庆北': 'CUW',
        '重庆': 'CQW',
        '重庆南': 'CRW',
        '广州东': 'GGQ',
        '上海': 'SHH',
        '上海南': 'SNH',
        '上海虹桥': 'AOH',
        "乌鲁木齐":"WAR",
}

session = requests.Session()
t = input('enter a time:(yyyy-mm-dd):')
start = input('enter a start city:')
start = city[start]
end = input('enter a end city:')
end = city[end]
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
session.get(url=url)
params = {
    'leftTicketDTO.train_date': t,
    'leftTicketDTO.from_station': start,
    'leftTicketDTO.to_station': end,
    'purpose_codes': 'ADULT'
}
url = 'https://kyfw.12306.cn/otn/leftTicket/query'
json_data_list = session.get(url=url,headers=headers,params=params).json()['data']['result']
for s in json_data_list:
    print(s)
    

"""
enter a time:(yyyy-mm-dd):2020-04-24
enter a start city:北京西
enter a end city:乌鲁木齐
OgpOKePFaIjq4JeKlrzGQYuo%2FNQ9IGBT60pOey84b65LmERid5BrugNc5Li4PfZQU6tHM5Sx8t2A%0AVfgPML3fb%2Fnw4cy6rlTO59v10zpy3c0dA826Lgfgv3EGzLgqMJPp5WIl8ASgBlqJ9cQCUifvB3ad%0ADIsa48V%2BT6llCFT%2F0Twf8c%2FcL0UskOyl2jvRmJxFA0V7sf38B96sTTuMydQUZAxqY6jLn4FlaP3a%0Ai4v81hVkYQnaa9%2FRl0kopLA2XOajWxMacbpS%2FLmzpzxDygxKSJBI%2BXNOLNru7%2FoaIV9JUsqzJZoq%0A07qAG344Kx%2BI6%2BLF|预订|2400000Z690S|Z69|BXP|WAR|BXP|WAR|10:00|16:47|30:47|Y|eeRCyC%2F6EjF3PP9KoPD9V5EKgf6pRtorhMls9NXFBd3Ew2asV6G3jXGLL8U%3D|20200424|3|P4|01|20|0|0||||19|||无||有|有|||||10401030|1413|1|0|||||||||
kmrJdlx7XXleamfpUC3Vlbj3AeTkEqidnSKEwZ8pd5mPcKlD8iw2DUP4JO8NtZzvyz6keEjihPrx%0AMutL95TonNq%2F4jnZl1xxjG5h11GjmiHAdYkwCXOlybftAbRKvX%2B747X0BmS%2B5NAhcCiSJVg4Smu8%0ADXpp4%2FYNGZz21tXGTLA8oQuix1cN7wU7hmuhR5EL12tNonPYE%2FnEIVJO0i3XQOjADfN8v2Ri1bpO%0ACeH%2FYl9ZnYkp%2F00hLAwIur%2B0H%2Fcrm9bTFqupkuFtN0vn%2FsKKpkFRiyqH51e5qJPSkkcFeNWF76Oy%0AAgOQ3w%3D%3D|预订|240000Z1790K|Z179|BXP|WAR|BXP|WAR|21:04|10:55|37:51|Y|uDOA4FNZyGE3qYiqIxYSUeuz5eVfI24JnfTryd2a4XYZE%2FLI|20200424|3|P4|01|20|0|0||||17|||||有|有|||||104030|143|0|0|||||||||
"""
```

