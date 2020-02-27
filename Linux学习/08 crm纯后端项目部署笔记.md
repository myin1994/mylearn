# crm纯后端项目部署笔记

## 相关需求

- nginx，提供反向代理功能，将80端口的请求，转发给django的8000
- uwsgi+django 启动后端进程，和800端口，处理用户的动态逻辑，登录，注册，查询等curd操作
- mariadb（mysql数据库），进行数据导出、导入操作
- 虚拟环境的创建
- supervisor进程管理工具  ，防止uwsig突然崩溃，supervisor能够自动启动uwsgi

## 安装mariadb（mysql）

centos7下由于mysql已经收费了，因此有开源组织，创建了一个myslq分支，完全一模一样的mariadb数据库

+ 安装命令

  ```
  yum install mariadb-server  mariadb  -y
  ```

+ mariadb数据库的相关命令

  ```
  systemctl start mariadb  #启动MariaDB
  
  systemctl stop mariadb  #停止MariaDB
  
  systemctl restart mariadb  #重启MariaDB
  
  systemctl enable mariadb  #设置开机启动
  ```

+ 初始化mysql

  ```
  在确认 MariaDB 数据库软件程序安装完毕并成功启动后请不要立即使用。为了确保数据 库的安全性和正常运转，需要先对数据库程序进行初始化操作。这个初始化操作涉及下面 5 个 步骤。
  ➢ 设置 root 管理员在数据库中的密码值(注意，该密码并非 root 管理员在系统中的密 码，这里的密码值默认应该为空，可直接按回车键)。
  ➢ 设置 root 管理员在数据库中的专有密码。
  ➢ 随后删除匿名账户，并使用 root 管理员从远程登录数据库，以确保数据库上运行的业
  务的安全性。
  ➢ 删除默认的测试数据库，取消测试数据库的一系列访问权限。
  ➢ 刷新授权列表，让初始化的设定立即生效。
  
  确保mariadb服务器启动后，执行命令初始化
  mysql_secure_installation
  ```

  ![image-20200208160558578]($%7Basserts%7D/image-20200208160558578.png)

## uwsgi+django的后台启动

+ 为什么使用uwsgi

  + python manage.py runserver 其实是调用wsgiref这个python内置的wsgi 服务器，性能很低，能够运行处一个socket服务端，便于程序员调试django程序，它是单线程，单进程，性能很低
  + 在linux服务器线上，主流的部署形式是uwsgi对django进行启动，支持多进程，多线程，以及各种优化并发性更好，因为uwsgi是C写的一个基于uwsgi协议运行的高性能 Web服务器

+ 启动步骤

  1. 创建一个新的虚拟环境

     ```
     [root@s26linux s26crm]# virtualenv --no-site-packages --python=python3  venv_crm
     ```

  2. 激活虚拟环境

     ```
     [root@s26linux bin]# pwd
     /s26crm/venv_crm/bin
     [root@s26linux bin]# ls
     activate       activate.ps1      easy_install      pip3    python3        wheel
     activate.csh   activate_this.py  easy_install-3.6  pip3.6  python3.6
     activate.fish  activate.xsh      pip               python  python-config
     [root@s26linux bin]#
     [root@s26linux bin]# source ./activate
     (venv_crm) [root@s26linux bin]#
     ```

  3. 安装uwsgi工具

     ```
     (venv_crm) [root@s26linux bin]# pip3 install -i https://pypi.douban.com/simple uwsgi
     ```

  4. 上传代码到linux

     ```
     用xshell连接上linux之后，安装lrzsz工具，yum install lrzsz -y  
     就可以使用 rz命令，接收windows中的资料了(crm了)
     
     linux传输使用scp
     yumac: ~ yuchao$scp  Downloads/课后管理系统.zip root@192.168.178.134:/s26crm/
     root@192.168.178.134's password:
     课后管理系统.z 100%   19MB  59.0MB/s   00:00
     ```

  5. 解压缩crm代码

     ```
     unzip  课后管理系统.zip
     ```

  6. 解决crm运行所需的依赖环境

     + 方法1：导出windows中，python解释器下所有的模块信息

       ```
       pip3 freeze >  requirements.txt
       在linux中安装此文件即可
       pip3 install -r requirements.txt  
       ```

     + 方法2：笨办法，根据报错一个一个解决

       ```
       pip3 install -i https://pypi.douban.com/simple  django==1.11.9
       pip3 install -i https://pypi.douban.com/simple  pymysql
       pip3 install -i https://pypi.douban.com/simple  django-multiselectfield
       ```

  7. 启动mariadb数据库，修改settings.py配置文件

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'school_management_system',
             'PASSWORD':'chaoge666',
             'USER':'root',
             'PORT':3306,
             'HOST':'127.0.0.1',
         }
     }
     ```

  8. 导出windows的源数据库文件

     ```
     #cmd下导出命令 --all-databases 导出所有数据库的参数 ，指定对应数据库及表进行导出即可
     mysqldump -uroot -p  --all-databases  >  alldb.sql
     ```

  9. 在linux机器上，导入此sql文件

     ```
     导入命令如下
     先登录mysql数据库
     mysql -uroot -p
     在数据库交互的终端下,使用如下命令，导入sql数据库，表
     MariaDB [(none)]> source  /s26crm/alldb.sql;
     ```

  10. 再次调试crm是否能运行

      ```
      (venv_crm) [root@s26linux login]# python3 manage.py runserver 0.0.0.0:8000
      ```

  11. 使用uwsgi及uwsgi的配置文件，启动django支持多进程的启动方式

      1. 在settings同级目录下手动创建一个uwsgi的配置文件

         ```
         touch  uwsgi.ini
         ```

      2. 写入配置内容

         ```ini
         [uwsgi]
         # Django-related settings
         # the base directory (full path)
         # 填入你crm项目的第一层绝对路径
         chdir           = /s26crm/login
         # Django's wsgi file
         # 这个wsgi.py文件，在第二层的crm目录下
         module          = login.wsgi
         # the virtualenv (full path)
         # 填写虚拟环境的绝对路径
         home            = /s26crm/venv_crm
         # process-related settings
         # master
         master          = true
         # maximum number of worker processes
         # 定义uwsgi的工作进程数，优化公式是 2*cpu_核数+1 
         processes       = 3
         # the socket (use the full path to be safe
         # 这个socket参数是把你的crm启动在一个基于uwsgi协议的socket链接上，用户无法直接访问了
         # 启动在socket链接上，就只能用nginx通过uwsgi协议反向代理，用户无法直接访问了
         # 保护后端进程的安全，以及高性能 
         # 这个socket也就是crm启动的地址和端口 
         socket          = 0.0.0.0:8000
         
         # ... with appropriate permissions - may be needed
         # chmod-socket    = 664
         # clear environment on exit
         vacuum          = true
         ```

  12. 使用uwsgi命令，指定uwsgi.ini配置文件，启动crm程序

      ```shell
      # 注意找到这个uwsgi.ini的路径 再执行如下命令
      # 注意，此时不能通过对应ip+端口进行访问了，需要配置nginx代理
      uwsgi --ini  uwsgi.ini
      ```

## 配置nginx反向代理，请求转发给uwsgi+django

1. 修改nginx.conf，location中改为反向代理的参数，如下

   ```nginx
   server {
           #定义网站端口的参数
           listen       80;
           # 填写网站域名的参数
           server_name  www.s26pythonav.com;
           #此时这个nginx作用是反向代理
           # 请求转发给 uwsgi
           location / {
           # proxy_pass 转发的是http请求
           # 这里要用基于uwsgi协议的转发参数
           uwsgi_pass  0.0.0.0:8000;
           include uwsgi_params;
   }
   }
   ```

2. 平滑重启nginx

   ```
   nginx -s reload
   ```

3. 此时会发现crm项目丢失了静态文件，js，css等，是因为uwsig默认不解析静态文件，需要统一收集一下，交给nginx去返回给用户浏览器

   1. 用命令收集crm项目所有的静态文件,在settings中添加如下参数

      ```python
      #这个参数，是统一收集所有的静态文件，放入一个文件夹
      STATIC_ROOT='/s26crm/mystatic'
      ```

   2. 执行命令--在项目一级目录下

      ```
      (venv_crm) [root@s26linux login]# python3  manage.py collectstatic
      ```

4. 收集好了crm的所有静态文件之后，交给nginx去返回，再次修改nginx.conf为如下配置，添加一个静态文件处理的 locaiton

   ```nginx
   location / {
           # proxy_pass 转发的是http请求
           # 这里要用基于uwsgi协议的转发参数
           uwsgi_pass  0.0.0.0:8000;
           include uwsgi_params;
   			}
   			
   			# http://192.168.178.134/static/auth/js/jquery.min.js
   			# http://192.168.178.134/static/auth/js/common.js
   			# http://192.168.178.134/static/auth/css/style.css
   			
   			#  我就可以在nginx这里，做一个路径别名
   			# 当所有的请求是 以 192.168.178.134/static 开头的时候
   		
           location  /static {
           	# 我就做一个别名，让nginx去 /s26crm/mystatic 这个目录下去找，一定能找着了
   					alias /s26crm/mystatic;
   
   				}
   ```

5. 重启nginx，让静态文件，页面生效

   ```
   nginx -s reload
   ```

6. 再次启动uwsgi+django的后台

   ```
   (venv_crm) [root@s26linux login]# uwsgi --ini uwsgi.ini
   ```

   

## supervisor进程管理工具

+ 使用supervisor管理uwsig进程步骤

  1. 安装supervisor工具

     ```
     yum install supervisor -y 
     ```

  2. 生成supervisor配置文件，定义管理crm的任务

     ```
     (venv_crm) [root@s26linux login]# echo_supervisord_conf >  /etc/supervisord.conf
     ```

  3. 修改配置文件，在最底行，输入如下内容，supervisor其实也就是帮助用户执行命令而已

     ```ini
     vim /etc/supervisord.conf
     #加入如下内容 
     # 这个program，就你管理任务的一个名字而已，随便叫什么，自己能够看的懂就好
     [program:s26nbcrm]
     command=/s26crm/venv_crm/bin/uwsgi --ini  /s26crm/login/uwsgi.ini    ; 程序启动命令
     autostart=true       ; 在supervisord启动的时候也自动启动
     startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
     autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
     
     stopasgroup=true     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
     killasgroup=true     ;默认为false，向进程组发送kill信号，包括子进程
     ```

  4. 用命令启动supervisor

     ```
     (venv_crm) [root@s26linux login]# supervisord -c /etc/supervisord.conf 
     ```

  5. 使用管理任务的命令

     ```
     (venv_crm) [root@s26linux login]# supervisorctl -c /etc/supervisord.conf
     ```

  6. supervisor的管理基本命令

     ```
     (venv_crm) [root@s26linux login]# supervisorctl -c /etc/supervisord.conf
     supervisor> stop s26nbcrm
     s26nbcrm: stopped
     supervisor> start s26nbcrm
     s26nbcrm: started
     supervisor>
     supervisor>
     supervisor> status
     s26nbcrm                         RUNNING   pid 8733, uptime 0:00:15
     ```

     注：若出现如下错误

     ```
     Error: Another program is already listening on a port that one of our HTTP servers is configured to use.  Shut this program down first before starting supervisord.
     
     
     ----------------------------
     ps -ef | grep supervisord
     kill -s SIGTERM 2503 对应端口
     #重新执行
     supervisord -c /etc/supervisor/supervisord.conf
     ```

+ supervisor管理nginx

  ```
  [program:nginx]
  command=/opt/tngx232/sbin/nginx  -g 'daemon off;'
  autostart=true       ; 在supervisord启动的时候也自动启动
  startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
  autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
  
  stopasgroup=true     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
  killasgroup=true     ;默认为false，向进程组发送kill信号，包括子进程
  
  
  
  -----------------------
  修改后记得更新 Supervisor 以及重启 Nginx 进程，命令:
  $ supervisorctl reread # 重新读取配置
  $ supervisorctl update # 更新配置
  $ supervisorctl restart nginx  # 重启 nginx
  $ killall nginx  # 杀掉所有的 nginx 进程
  ```

  