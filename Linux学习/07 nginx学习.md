## web服务器和web框架的关系

+ web服务器（nginx）：接收HTTP请求（例如www.pythonav.cn/xiaocang.jpg）并返回数据
+ web框架（django，flask）：开发web应用程序，处理接收到的数据

## nginx是什么

+ 描述

  ```
  nginx是一个开源的，支持高性能，高并发的www服务和代理服务软件。它是一个俄罗斯人lgor sysoev开发的，作者将源代码开源出来供全球使用。
  nginx比它大哥apache性能改进许多，nginx占用的系统资源更少，支持更高的并发连接，有更高的访问效率。
  nginx不但是一个优秀的web服务软件，还可以作为反向代理，负载均衡，以及缓存服务使用。
  安装更为简单，方便，灵活。
  ```

+ 面试回答nginx技巧

  ```
  支持高并发，能支持几万并发连接
  资源消耗少，在3万并发连接下开启10个nginx线程消耗的内存不到200M
  可以做http反向代理和负载均衡
  支持异步网络i/o事件模型epoll
  ```

  

## nginx安装与使用

### yum安装nginx

```
yum install nginx -y
安装版本较低
```

### 安装淘宝nginx

![image-20200206191221246]($%7Basserts%7D/image-20200206191221246.png)

+ 安装步骤

  1. 下载nginx源代码(从官网获取链接)

     ```
     yum install gcc-c++ -y
     wget http://tengine.taobao.org/download/tengine-2.3.2.tar.gz
     ```

2. 解压缩源代码

   ```
   tar  -zxvf  tengine-2.3.2.tar.gz
   ```

3. 进入nginx源码目录，指定安装路径

   ```
   [root@s26linux tengine-2.3.2]# ./configure --prefix=/opt/tngx232/
   ```

4. 开始编译且安装

   ```
   [root@s26linux tengine-2.3.2]# make && make install
   ```

5. 配置环境变量

   + 修改/etc/profile，修改PATH的值

     ```
     先查看PATH值，然后追加当前bin目录
     vim /etc/profile
     添加如下PATH变量
     PATH='/s26linux/python362/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/tngx232/sbin'
     ```

   + 手动读取这个/etc/profile

     ```
     [root@s26linux sbin]# source /etc/profile
     ```

   + 重新ssh链接

6. nginx可执行命令的常用方式

   + nginx -s reload  平滑重启，重新读取nginx配置文件，而不重启进程
   + nginx  直接输入nginx，是代表启动，只能首次使用
   + nginx -s stop  杀死nginx进程

### nginx常用功能

- nginx的虚拟主机功能
  - nginx支持多虚拟主机
- nginx的访客日志功能，检测用户的请求来源ip，请求客户端
  - 检测用户来源客户端，返回移动端/pc端的站点
  - 运维通过日志分析用户的请求情况，时间点等等
  - 检测恶意的爬虫客户端，进行封禁等
- nginx的错误页面优化等
- nginx的反向代理功能，请求转发
  - 实现负载均衡，请求分发

### nginx的文件夹介绍

```
[root@s26linux tngx232]# pwd
/opt/tngx232
[root@s26linux tngx232]# ls
conf  html  logs  sbin
```

+ conf 存放nginx配置文件的目录
+ html  存放nginx的网站站点 静态资源的目录
+ logs 存放各种日志的目录
+ sbin  存放nginx可执行脚本的目录

## nginx的虚拟主机站点功能

```
默认站点的文件夹在nginx的安装路径下，名为html的文件夹，这个是可以在nginx.conf中修改的
[root@s26linux html]# pwd
/opt/tngx232/html
[root@s26linux html]# ls
50x.html  ceshi.gif  index.html

192.168.178.133/ceshi.gif  #可以访问资源了
```

### nginx的配置文件学习

+ 参考博客：https://www.cnblogs.com/pyyu/p/9468680.html 

+ 主配置文件存放路径

  ```
  /opt/tngx232/conf/nginx.conf
  ```

+ 配置文件采用key value格式

  + CoreModule核心模块

    ```nginx
    user www;                       #Nginx进程所使用的用户
    worker_processes 1;             #Nginx运行的work进程数量(建议与CPU数量一致或auto)
    error_log /log/nginx/error.log  #Nginx错误日志存放路径
    pid /var/run/nginx.pid          #Nginx服务运行后产生的pid进程号
    ```

  + events事件模块

    ```nginx
    events {            
        worker_connections  //每个worker进程支持的最大连接数
        use epool;          //事件驱动模型, epoll默认
    }
    ```

  + http内核模块-核心web功能配置点

    ```nginx
    //公共的配置定义在http{}
    http {  //http层开始
    ...    
        //使用Server配置网站, 每个Server{}代表一个网站(简称虚拟主机)
        'server' {
            listen       80;        //监听端口, 默认80
            server_name  localhost; //提供服务的域名或主机名
            access_log host.access.log  //访问日志
            //控制网站访问路径
            'location' / {
                root   /usr/share/nginx/html;   //存放网站代码路径
                index  index.html index.htm;    //服务器返回的默认页面文件
            }
            //指定错误代码, 统一定义错误页面, 错误代码重定向到新的Locaiton
            error_page   500 502 503 504 =  /50x.html;
        }
        ...
        //第二个虚拟主机配置
        'server' {
        ...
        }
        
        include /etc/nginx/conf.d/*.conf;  //包含/etc/nginx/conf.d/目录下所有以.conf结尾的文件
    
    }   //http层结束
    ```

+ Nginx配置文件nginx.conf中文详解

  ```nginx
  #定义Nginx运行的用户和用户组
  user www www;
  
  #nginx进程数，建议设置为等于CPU总核心数。
  worker_processes 8;
   
  #全局错误日志定义类型，[ debug | info | notice | warn | error | crit ]
  error_log /usr/local/nginx/logs/error.log info;
  
  #进程pid文件
  pid /usr/local/nginx/logs/nginx.pid;
  
  #指定进程可以打开的最大描述符：数目
  #工作模式与连接数上限
  #这个指令是指当一个nginx进程打开的最多文件描述符数目，理论值应该是最多打开文件数（ulimit -n）与nginx进程数相除，但是nginx分配请求并不是那么均匀，所以最好与ulimit -n 的值保持一致。
  #现在在linux 2.6内核下开启文件打开数为65535，worker_rlimit_nofile就相应应该填写65535。
  #这是因为nginx调度时分配请求到进程并不是那么的均衡，所以假如填写10240，总并发量达到3-4万时就有进程可能超过10240了，这时会返回502错误。
  worker_rlimit_nofile 65535;
  
  
  events
  {
      #参考事件模型，use [ kqueue | rtsig | epoll | /dev/poll | select | poll ]; epoll模型
      #是Linux 2.6以上版本内核中的高性能网络I/O模型，linux建议epoll，如果跑在FreeBSD上面，就用kqueue模型。
      #补充说明：
      #与apache相类，nginx针对不同的操作系统，有不同的事件模型
      #A）标准事件模型
      #Select、poll属于标准事件模型，如果当前系统不存在更有效的方法，nginx会选择select或poll
      #B）高效事件模型
      #Kqueue：使用于FreeBSD 4.1+, OpenBSD 2.9+, NetBSD 2.0 和 MacOS X.使用双处理器的MacOS X系统使用kqueue可能会造成内核崩溃。
      #Epoll：使用于Linux内核2.6版本及以后的系统。
      #/dev/poll：使用于Solaris 7 11/99+，HP/UX 11.22+ (eventport)，IRIX 6.5.15+ 和 Tru64 UNIX 5.1A+。
      #Eventport：使用于Solaris 10。 为了防止出现内核崩溃的问题， 有必要安装安全补丁。
      use epoll;
  
      #单个进程最大连接数（最大连接数=连接数*进程数）
      #根据硬件调整，和前面工作进程配合起来用，尽量大，但是别把cpu跑到100%就行。每个进程允许的最多连接数，理论上每台nginx服务器的最大连接数为。
      worker_connections 65535;
  
      #keepalive超时时间。
      keepalive_timeout 60;
  
      #客户端请求头部的缓冲区大小。这个可以根据你的系统分页大小来设置，一般一个请求头的大小不会超过1k，不过由于一般系统分页都要大于1k，所以这里设置为分页大小。
      #分页大小可以用命令getconf PAGESIZE 取得。
      #[root@web001 ~]# getconf PAGESIZE
      #4096
      #但也有client_header_buffer_size超过4k的情况，但是client_header_buffer_size该值必须设置为“系统分页大小”的整倍数。
      client_header_buffer_size 4k;
  
      #这个将为打开文件指定缓存，默认是没有启用的，max指定缓存数量，建议和打开文件数一致，inactive是指经过多长时间文件没被请求后删除缓存。
      open_file_cache max=65535 inactive=60s;
  
      #这个是指多长时间检查一次缓存的有效信息。
      #语法:open_file_cache_valid time 默认值:open_file_cache_valid 60 使用字段:http, server, location 这个指令指定了何时需要检查open_file_cache中缓存项目的有效信息.
      open_file_cache_valid 80s;
  
      #open_file_cache指令中的inactive参数时间内文件的最少使用次数，如果超过这个数字，文件描述符一直是在缓存中打开的，如上例，如果有一个文件在inactive时间内一次没被使用，它将被移除。
      #语法:open_file_cache_min_uses number 默认值:open_file_cache_min_uses 1 使用字段:http, server, location  这个指令指定了在open_file_cache指令无效的参数中一定的时间范围内可以使用的最小文件数,如果使用更大的值,文件描述符在cache中总是打开状态.
      open_file_cache_min_uses 1;
      
      #语法:open_file_cache_errors on | off 默认值:open_file_cache_errors off 使用字段:http, server, location 这个指令指定是否在搜索一个文件是记录cache错误.
      open_file_cache_errors on;
  }
   
   
   
  #设定http服务器，利用它的反向代理功能提供负载均衡支持
  http
  {
      #文件扩展名与文件类型映射表
      include mime.types;
  
      #默认文件类型
      default_type application/octet-stream;
  
      #默认编码
      #charset utf-8;
  
      #服务器名字的hash表大小
      #保存服务器名字的hash表是由指令server_names_hash_max_size 和server_names_hash_bucket_size所控制的。参数hash bucket size总是等于hash表的大小，并且是一路处理器缓存大小的倍数。在减少了在内存中的存取次数后，使在处理器中加速查找hash表键值成为可能。如果hash bucket size等于一路处理器缓存的大小，那么在查找键的时候，最坏的情况下在内存中查找的次数为2。第一次是确定存储单元的地址，第二次是在存储单元中查找键 值。因此，如果Nginx给出需要增大hash max size 或 hash bucket size的提示，那么首要的是增大前一个参数的大小.
      server_names_hash_bucket_size 128;
  
      #客户端请求头部的缓冲区大小。这个可以根据你的系统分页大小来设置，一般一个请求的头部大小不会超过1k，不过由于一般系统分页都要大于1k，所以这里设置为分页大小。分页大小可以用命令getconf PAGESIZE取得。
      client_header_buffer_size 32k;
  
      #客户请求头缓冲大小。nginx默认会用client_header_buffer_size这个buffer来读取header值，如果header过大，它会使用large_client_header_buffers来读取。
      large_client_header_buffers 4 64k;
  
      #设定通过nginx上传文件的大小
      client_max_body_size 8m;
  
      #开启高效文件传输模式，sendfile指令指定nginx是否调用sendfile函数来输出文件，对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。注意：如果图片显示不正常把这个改成off。
      #sendfile指令指定 nginx 是否调用sendfile 函数（zero copy 方式）来输出文件，对于普通应用，必须设为on。如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络IO处理速度，降低系统uptime。
      sendfile on;
  
      #开启目录列表访问，合适下载服务器，默认关闭。
      autoindex on;
  
      #此选项允许或禁止使用socke的TCP_CORK的选项，此选项仅在使用sendfile的时候使用
      tcp_nopush on;
       
      tcp_nodelay on;
  
      #长连接超时时间，单位是秒
      keepalive_timeout 120;
  
      #FastCGI相关参数是为了改善网站的性能：减少资源占用，提高访问速度。下面参数看字面意思都能理解。
      fastcgi_connect_timeout 300;
      fastcgi_send_timeout 300;
      fastcgi_read_timeout 300;
      fastcgi_buffer_size 64k;
      fastcgi_buffers 4 64k;
      fastcgi_busy_buffers_size 128k;
      fastcgi_temp_file_write_size 128k;
  
      #gzip模块设置
      gzip on; #开启gzip压缩输出
      gzip_min_length 1k;    #最小压缩文件大小
      gzip_buffers 4 16k;    #压缩缓冲区
      gzip_http_version 1.0;    #压缩版本（默认1.1，前端如果是squid2.5请使用1.0）
      gzip_comp_level 2;    #压缩等级
      gzip_types text/plain application/x-javascript text/css application/xml;    #压缩类型，默认就已经包含textml，所以下面就不用再写了，写上去也不会有问题，但是会有一个warn。
      gzip_vary on;
  
      #开启限制IP连接数的时候需要使用
      #limit_zone crawler $binary_remote_addr 10m;
  
  
  
      #负载均衡配置
      upstream jh.w3cschool.cn {
       
          #upstream的负载均衡，weight是权重，可以根据机器配置定义权重。weigth参数表示权值，权值越高被分配到的几率越大。
          server 192.168.80.121:80 weight=3;
          server 192.168.80.122:80 weight=2;
          server 192.168.80.123:80 weight=3;
  
          #nginx的upstream目前支持4种方式的分配
          #1、轮询（默认）
          #每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。
          #2、weight
          #指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。
          #例如：
          #upstream bakend {
          #    server 192.168.0.14 weight=10;
          #    server 192.168.0.15 weight=10;
          #}
          #2、ip_hash
          #每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。
          #例如：
          #upstream bakend {
          #    ip_hash;
          #    server 192.168.0.14:88;
          #    server 192.168.0.15:80;
          #}
          #3、fair（第三方）
          #按后端服务器的响应时间来分配请求，响应时间短的优先分配。
          #upstream backend {
          #    server server1;
          #    server server2;
          #    fair;
          #}
          #4、url_hash（第三方）
          #按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。
          #例：在upstream中加入hash语句，server语句中不能写入weight等其他的参数，hash_method是使用的hash算法
          #upstream backend {
          #    server squid1:3128;
          #    server squid2:3128;
          #    hash $request_uri;
          #    hash_method crc32;
          #}
  
          #tips:
          #upstream bakend{#定义负载均衡设备的Ip及设备状态}{
          #    ip_hash;
          #    server 127.0.0.1:9090 down;
          #    server 127.0.0.1:8080 weight=2;
          #    server 127.0.0.1:6060;
          #    server 127.0.0.1:7070 backup;
          #}
          #在需要使用负载均衡的server中增加 proxy_pass http://bakend/;
  
          #每个设备的状态设置为:
          #1.down表示单前的server暂时不参与负载
          #2.weight为weight越大，负载的权重就越大。
          #3.max_fails：允许请求失败的次数默认为1.当超过最大次数时，返回proxy_next_upstream模块定义的错误
          #4.fail_timeout:max_fails次失败后，暂停的时间。
          #5.backup： 其它所有的非backup机器down或者忙的时候，请求backup机器。所以这台机器压力会最轻。
  
          #nginx支持同时设置多组的负载均衡，用来给不用的server来使用。
          #client_body_in_file_only设置为On 可以讲client post过来的数据记录到文件中用来做debug
          #client_body_temp_path设置记录文件的目录 可以设置最多3层目录
          #location对URL进行匹配.可以进行重定向或者进行新的代理 负载均衡
      }
       
       
       
      #虚拟主机的配置
      server
      {
          #监听端口
          listen 80;
  
          #域名可以有多个，用空格隔开
          server_name www.w3cschool.cn w3cschool.cn;
          index index.html index.htm index.php;
          root /data/www/w3cschool;
  
          #对******进行负载均衡
          location ~ .*.(php|php5)?$
          {
              fastcgi_pass 127.0.0.1:9000;
              fastcgi_index index.php;
              include fastcgi.conf;
          }
           
          #图片缓存时间设置
          location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$
          {
              expires 10d;
          }
           
          #JS和CSS缓存时间设置
          location ~ .*.(js|css)?$
          {
              expires 1h;
          }
           
          #日志格式设定
          #$remote_addr与$http_x_forwarded_for用以记录客户端的ip地址；
          #$remote_user：用来记录客户端用户名称；
          #$time_local： 用来记录访问时间与时区；
          #$request： 用来记录请求的url与http协议；
          #$status： 用来记录请求状态；成功是200，
          #$body_bytes_sent ：记录发送给客户端文件主体内容大小；
          #$http_referer：用来记录从那个页面链接访问过来的；
          #$http_user_agent：记录客户浏览器的相关信息；
          #通常web服务器放在反向代理的后面，这样就不能获取到客户的IP地址了，通过$remote_add拿到的IP地址是反向代理服务器的iP地址。反向代理服务器在转发请求的http头信息中，可以增加x_forwarded_for信息，用以记录原有客户端的IP地址和原来客户端的请求的服务器地址。
          log_format access '$remote_addr - $remote_user [$time_local] "$request" '
          '$status $body_bytes_sent "$http_referer" '
          '"$http_user_agent" $http_x_forwarded_for';
           
          #定义本虚拟主机的访问日志
          access_log  /usr/local/nginx/logs/host.access.log  main;
          access_log  /usr/local/nginx/logs/host.access.404.log  log404;
           
          #对 "/" 启用反向代理
          location / {
              proxy_pass http://127.0.0.1:88;
              proxy_redirect off;
              proxy_set_header X-Real-IP $remote_addr;
               
              #后端的Web服务器可以通过X-Forwarded-For获取用户真实IP
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
               
              #以下是一些反向代理的配置，可选。
              proxy_set_header Host $host;
  
              #允许客户端请求的最大单文件字节数
              client_max_body_size 10m;
  
              #缓冲区代理缓冲用户端请求的最大字节数，
              #如果把它设置为比较大的数值，例如256k，那么，无论使用firefox还是IE浏览器，来提交任意小于256k的图片，都很正常。如果注释该指令，使用默认的client_body_buffer_size设置，也就是操作系统页面大小的两倍，8k或者16k，问题就出现了。
              #无论使用firefox4.0还是IE8.0，提交一个比较大，200k左右的图片，都返回500 Internal Server Error错误
              client_body_buffer_size 128k;
  
              #表示使nginx阻止HTTP应答代码为400或者更高的应答。
              proxy_intercept_errors on;
  
              #后端服务器连接的超时时间_发起握手等候响应超时时间
              #nginx跟后端服务器连接超时时间(代理连接超时)
              proxy_connect_timeout 90;
  
              #后端服务器数据回传时间(代理发送超时)
              #后端服务器数据回传时间_就是在规定时间之内后端服务器必须传完所有的数据
              proxy_send_timeout 90;
  
              #连接成功后，后端服务器响应时间(代理接收超时)
              #连接成功后_等候后端服务器响应时间_其实已经进入后端的排队之中等候处理（也可以说是后端服务器处理请求的时间）
              proxy_read_timeout 90;
  
              #设置代理服务器（nginx）保存用户头信息的缓冲区大小
              #设置从被代理服务器读取的第一部分应答的缓冲区大小，通常情况下这部分应答中包含一个小的应答头，默认情况下这个值的大小为指令proxy_buffers中指定的一个缓冲区的大小，不过可以将其设置为更小
              proxy_buffer_size 4k;
  
              #proxy_buffers缓冲区，网页平均在32k以下的设置
              #设置用于读取应答（来自被代理服务器）的缓冲区数目和大小，默认情况也为分页大小，根据操作系统的不同可能是4k或者8k
              proxy_buffers 4 32k;
  
              #高负荷下缓冲大小（proxy_buffers*2）
              proxy_busy_buffers_size 64k;
  
              #设置在写入proxy_temp_path时数据的大小，预防一个工作进程在传递文件时阻塞太长
              #设定缓存文件夹大小，大于这个值，将从upstream服务器传
              proxy_temp_file_write_size 64k;
          }
           
           
          #设定查看Nginx状态的地址
          location /NginxStatus {
              stub_status on;
              access_log on;
              auth_basic "NginxStatus";
              auth_basic_user_file confpasswd;
              #htpasswd文件的内容可以用apache提供的htpasswd工具来产生。
          }
           
          #本地动静分离反向代理配置
          #所有jsp的页面均交由tomcat或resin处理
          location ~ .(jsp|jspx|do)?$ {
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_pass http://127.0.0.1:8080;
          }
           
          #所有静态文件由nginx直接读取不经过tomcat或resin
          location ~ .*.(htm|html|gif|jpg|jpeg|png|bmp|swf|ioc|rar|zip|txt|flv|mid|doc|ppt|
          pdf|xls|mp3|wma)$
          {
              expires 15d; 
          }
           
          location ~ .*.(js|css)?$
          {
              expires 1h;
          }
      }
  }
  ######Nginx配置文件nginx.conf中文详解#####
  
  nginx.conf详解
  ```

  

### nginx支持多虚拟主机站点

+ 多虚拟主机配置-其实就是在nginx.conf中定义多个server{}标签而已

  + 基于域名的多虚拟主机，基于域名区分不同的站点配置，直接修改server_name配置
  + 基于端口的多虚拟主机配置，直接修改listen 的配置
  + 基于ip的多虚拟主机配置

+ 需求---一个服务器运行2个网站，返回不同的页面

  + 当用户访问 www.s26python.com    >   /s26linux/python/index.html
  + 当用户访问  www.s26linux.com   >  /s26linux/linux/index.html  

+ 配置步骤

  1. 准备一台服务器，安装好nginx

  2. 准备好2个域名 ,由于资金有限，在本地进行假的解析，测试使用，hosts文件

     ```
     修改/etc/hosts文件，添加如下内容，问题，在linux添加，还是在别的地方添加？
     答案：应该在客户端本地添加 ，macos或者是windows的hosts文件中添加
     添加如下内容到hosts文件
     192.168.178.133 www.s26python.com
     192.168.178.133 www.s26linux.com
     
     
     windows中hosts文件位置C:/windows/system32/drivers/etc/hosts
     ```

  3. 修改nginx的配置，支持多域名的虚拟主机

     + vim nginx.conf ，修改为如下的配置

     + 第一个站点 www.s26python.com ，修改如下server{}标签

       ```
       server {
               #定义网站端口的参数
               listen       80;
               # 填写网站域名的参数
               server_name  www.s26python.com;
       
               #charset koi8-r;
       
               #access_log  logs/host.access.log  main;
               #access_log  "pipe:rollback logs/host.access_log interval=1d baknum=7 maxsize=2G"  main;
               # 这个locaiton类似于url.py的功能，进行路由匹配
               # location / 代表最低级的匹配，所有的请求都会走到这里
               # 例如 192.168.178.133/hehe.txt
               # 例如  192.168.178.133/index.html
               location / {
                   # root关键词定义的是 网页根目录的路径
                   root   /s26linux/s26python;
                  # index参数 定义的是首页文件的名字
                   index  index.html index.htm;
               }
               }
       ```

     + 第二个虚拟主机站的配置，也就是 www.s26linux.com 再添加一个server{}标签

       ```
       server {
       listen 80;
       server_name www.s26linux.com;
       location / {
               root  /s26linux/s26linux/;
               index   index.html;
       }
       
       }
       ```

  4. 此时可以准备2个站点的资源文件夹了

     ```
     [root@s26linux conf]# mkdir -p /s26linux/{s26python,s26linux}
     ```

  5. 分别创建2个首页文件，写入对应的内容nginx

     ```
     [root@s26linux conf]# echo "我是第一个虚拟主机，s26python" > /s26linux/s26python/index.html
     [root@s26linux conf]# echo "我是第二个虚拟主机，s26linux~~~各位帅哥美女们，你们懂了没有" > /s26linux/s26linux/index.html
     ```

  6. 平滑重启nginx，查看页面效果

     ```
     nginx -s reload
     ```

### dns解析

dns解析就是 域名解析

把一个网站域名，解析成对应的ip地址，去访问 

好比  www.pythonav.cn  对应的服务器ip是 123.206.16.61

理解dns解析

```
在公网上，存在各个厂家的dns服务器，就是一个超大的key value数据库
存放着所有公网的 
域名 -----ip  的对应解析关系
常见的dns服务器有 
119.29.29.29  腾讯的dns服务器
223.5.5.5 阿里的dns服务器1
223.6.6.6   阿里的dns服务器2

比如
wwww.pythonav.cn  ------123.206.16.61

好比你的手机电话簿
小李 ------  152xxxxxxx
小红------   136xxxx
```

linux的dns客户端配置文件

```
/etc/resolv.conf    #这是公网dns服务器的配置
nameserver  119.29.29.29
```

本地的dns强制解析配置文件，hosts文件

```
linux在 
/etc/hosts  
```

## nginx的访问日志功能

+ 相关状态码

  + 404   40x  客户端请求出错，用户那里出错了，你请求的姿势不对
  + 500  50x  服务器端出错了，django后台崩溃了，可能是mysql数据库连不上了，python报错了
  + 200   20x  表示请求正确给与响应
  + 300  30x  表示请求被重定向转发了，etiantian.org 弃用了 > 跳转到 www.oldboeyedu.com

+ 配置日志文件

  1. 打开nginx.conf，找到如下配置，打开注释即可(记录所有server的日志)

     ```nginx
     log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                       '$status $body_bytes_sent "$http_referer" '
                       '"$http_user_agent" "$http_x_forwarded_for"';
     
     access_log  logs/access.log  main;
     access_log  "pipe:rollback logs/access_log interval=1d baknum=7 maxsize=2G"  main;
     ```

     **注：每个server单独的日志将后两行写在server标签中即可**

  2. 变量解释

     ```
     $remote_addr    记录客户端ip
     $remote_user    远程用户，没有就是 “-”
     $time_local 　　 对应[14/Aug/2018:18:46:52 +0800]
     $request　　　 　对应请求信息"GET /favicon.ico HTTP/1.1"
     $status　　　  　状态码
     $body_bytes_sent　　571字节 请求体的大小
     $http_referer　　对应“-”　　由于是直接输入浏览器就是 -
     $http_user_agent　　客户端身份信息
     $http_x_forwarded_for　　记录客户端的来源真实ip 97.64.34.118
     ```

  3. 开注释之后，平滑重启nginx

     ```
     nginx -s reload
     ```

  4. 如果想杀死nginx，可以用

     ```
      kill  pid ,杀死进程id
      pkill nginx名字  通过名字杀死进程
     ```

## nginx自定义404、500页面

1. 修改nginx.conf

   ```nginx
   #直接在对应server标签中加入即可，=号根据实际情况决定是否加入
   #存放位置，location下root根目录下
   
   error_page 404 = /40x.html;
   ```

2. 平滑重启nginx

   ```
   nginx -s reload
   ```

3. 手动创建错误页面40x.html文件



## nginx的反向代理功能与配置

+ 代理功能

  + 正向代理---代理的是客户端（比如vpn连接）

    可将正向代理与客户端整体看做客户端

  + 反向代理--代理的是服务端

    可将反向代理与服务端整体看做服务端

+ 反向代理的网站部署中的应用

  ```
  浏览器 ->  nginx web服务器  ->  django（后端到底有多少的机器，我们无需知道）
  ```

+ nginx的反向代理配置（请求转发）

  1. 环境准备

     ```
     准备2台linux虚拟机（在vmware里安装2个linux机器）
     
     机器1的ip  ：192.168.178.181    （中介代理）（nginx，配置代理功能）
     
     机器2的ip：  192.168.178.134     （房东，资源服务器）（nginx，返回一个网站页面）
     ```

  2. 先配置中介代理，181服务器，先装一个nginx

  3. 修改nginx.conf

     ```nginx
     #在server标签的location中修改
     #当请求是192.168.178.181的时候，进入这个location路径匹配
     #请求通过proxy_pass参数，转发给  另一台机器的地址
     
     location / {
              proxy_pass http://192.168.178.134;
             }
     ```

  4. 改完nginx.conf之后，保存退出，启动nginx

     ```
     nginx -s reload
     ```

  5. 正常配置资源服务器即可

  6. 访问代理服务器ip即可

## nginx负载均衡配置

+ 概述

  ```
  Web服务器，直接面向用户，往往要承载大量并发请求，单台服务器难以负荷，我使用多台WEB服务器组成集群，前端使用Nginx负载均衡，将请求分散的打到我们的后端服务器集群中，
  实现负载的分发。那么会大大提升系统的吞吐率、请求性能、高容灾
  ```

  ![image-20200208143809058]($%7Basserts%7D/image-20200208143809058.png)

+ 负载均衡与代理的异同

  + Nginx要实现负载均衡需要用到proxy_pass代理模块配置
  + Nginx负载均衡与Nginx代理不同地方在于Nginx代理仅代理一台服务器，而Nginx负载均衡则是将客户端请求代理转发至一组upstream虚拟服务池
  + Nginx可以配置代理多台服务器，当一台服务器宕机之后，仍能保持系统可用。

+ 负载均衡配置

  1. 环境准备

     ```
     应该准备至少3台服务器
     
     机器1：代理服务器（nginx提供负载均衡，反向代理的功能）
     机器2：资源服务器1
     机器3：资源服务器2  
     
     请求发给 代理服务器，然后配置规则，请求是发给机器2，还是机器3
     -----------------------------------------------------------
     这里使用两个站点模拟两个资源服务器
     
     请求 ->  代理服务器  ->负载均衡转发   -> 第一次发给 server{} 第一个站点
     								  -> 第二次发给 server{} 第二个站点
     ```

  2. 配置资源服务器，准备两个页面

     ```
     实验阶段，为了看到效果，是准备2个不同的资源服务器页面
     ```

     **注：线上真实的负载均衡部署，后端服务器应该是一样的**

  3. 配置负载均衡服务器

     1. 准备代理服务器 192.168.178.181

     2. 修改nginx如下配置，添加负载均衡参数

        ```nginx
        # 在server{}标签上面，添加一个负载均衡池  upstream{} 
        # 服务器地址池 名字是 s26_server
        
        upstream s26_server {
        server 192.168.178.134:80;
        server 192.168.178.134:81;
        }
        ```

        ```nginx
        #在server标签的location中修改
        
        location / {
                 proxy_pass http://s26_server;
                }
        ```

     3. 使用命令，检测nginx.conf是否编写正确

        ```
        nginx -t
        ```

     4. 编写正确后，重启nginx

        ```
        ngins -s reload
        ```

+ nginx负载均衡的分发算法

  + 分发规则，自行决定，根据自己的服务器架构决定

  + 最常用的就是权重，或者大家根本就不管，默认用轮循

  + 分发算法模式

    + 默认是轮循模式，一台服务器一次

    + 权重模式，配置如下

      ```nginx
      upstream s26_server {
      server 192.168.178.134:80 weight=1;
      server 192.168.178.134:81 weight=4;
      }
      ```

    + ip哈希模式，根据客户端的ip来源，指定给一台机器

      根据客户端的来源ip进行哈希，得到一个唯一值，永远只发给某一台机器了,就是指定某一个服务器来服务客户端

      ```nginx
      upstream s26_server {
      server 192.168.178.134:80 ;
      server 192.168.178.134:81 ;
      ip_hash;
      }
      ```

      