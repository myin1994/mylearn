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

    + 将任务列表中的任务对象赋予可被挂起的权限。只有任务对象被赋予了可被挂起的权限后，该
      任务对象才可以被挂起
      - 挂起：将当前的任务对象交出cpu的使用权。

  + await关键字

    + 在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断整个异步效果
    + 在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰。await就可以保证
      阻塞操作在异步执行的过程中不会被跳过！

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

  + 是一个支持异步的网络请求模块（requests是一个不支持异步的模块？）
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

  - 一定要使用任务对象的回调函数实现数据解析
  - why
    - 多任务的架构中数据的爬取是封装在特殊函数中，我们一定要保证数据请求结束后，
      再实现数据解析。

+ 使用多任务的异步协程爬取数据实现套路：

  - 可以先使用requests模块将待请求数据对应的url封装到有个列表中（同步）
  - 可以使用aiohttp模式将列表中的url进行异步的请求和数据解析（异步）

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

- selenium的弊端：

  - 效率低

- 动作链ActionChains

  - 动作链：一系列连续的动作（滑动动作）

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

