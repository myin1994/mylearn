## linux的软件包管理工具

+ linux安装软件有几种方式
  + 源代码编译安装（最好的安装形式，可以自由定义安装路径，第三方功能扩展，以及获取官网最新的代码进行编译安装，缺点是对新手不友好）
  + yum工具（新手最好的工具，自动化解决程序安装所需的依赖关系，自动下载且安装依赖，要求得配置yum仓库源，软件版本可能较低）
  + rpm软件包手动安装（弃用，需要手动解决依赖关系，贼难受，不用）

+ 不同系统的软件包安装格式
  + windows  exe
  + macos   dmg
  + linux   rpm 格式

+ 软件的依赖关系

  ```
  如何安装django的？
  下载django源码进行python3  setup.py  build  
  
  #相比我们都是用的pip安装，为什么呢？
  能够自动的解决django模块的依赖关系
  
  #pip3是安装python模块的工具，自动搜索依赖，解决依赖关系
  
  #yum工具是linux系统安装软件的工具，例如安装redis数据库，安装mysql数据库等等
  ```

## yum工具

对于redhat，centos系列的操作系统，90%的软件都可以yum自动安装，前提是要配置好软件仓库（yum源）

```
安装，卸载nginx
yum install nginx -y 
yum remove nginx -y   #自动解决所有依赖关系，很nice，好用
```

## yum仓库的配置步骤（yum源）

1. 找到阿里的开源镜像站

   ```
   提前下载wget yum install wget -y
   https://developer.aliyun.com/mirror/
   ```

2. 备份linux本地现有的yum仓库文件

   1. 默认yum仓库地址`/etc/yum.repos.d/`

      注意！只有在这个目录第一层的以*.repo结尾的文件才会被识别为是一个yum仓库文件

   2. 进入该路径后进行备份repo仓库文件

      ```
      mkdir allrepoBak
      mv ./*  allrepoBak/
      ```

3. 下载新的仓库文件，下载阿里的

   1. 参数解释 -O  将下载的文件，指定一个路径存放，且改名

   2. 下载第一个仓库

      ```
      wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
      ```

   3. 下载第二个仓库

      ```
      wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
      ```

4. 清空之前的yum缓存

   ```
   yum clean all
   ```

5. 测试用yum安装nginx软件，或是redis数据库软件

   ```
   yum install nginx -y 
   yum install redis -y 
   ```

6. 管理yum安装的软件

   只要是通过yum安装的软件，都可以用systemctl  系统服务管理命令，进行启停管理

   + systemctl start nginx  启动
   + systemctl stop nginx  停止
   + systemctl restart nginx  重启
   + systemctl status nginx  查看状态

7. 验证redis和nginx软件是否正常

   ```
   [root@s26linux yum.repos.d]# redis-cli
   127.0.0.1:6379> ping
   PONG
   
   退出redis，可以直接ctrl + c 
   
   
   验证nginx，直接浏览器访问网站的80端口即可
   192.168.178.133:80
   ```