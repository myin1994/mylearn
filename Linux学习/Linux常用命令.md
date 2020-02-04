## 远程连接Linux

+ 远程工具

  ```
  Xshell
  SecureCRT
  ```

+ 查看系统ip

  ```
  方式1：ip addr
  方式2: ifconfig
  ifconfig不能使用时参考-https://jingyan.baidu.com/article/eb9f7b6d42636d869364e8c9.html
  ```

  + linux看不到ip时

    + 进入网卡的配置文件目录

      ```
      cd /etc/sysconfig/network-scripts
      ```

    + 修改网卡配置，文件以你自己的电脑为准，是以 ifcfg开头的文件

      ```
      修改网卡的配置参数,用vi编辑器 
      vi ifcfg-ens33
      修改参数 onboot=yes
      ```

    + 重启网络服务即可

      ```
      systemctl   restart   network
      ```

    + 此时可以查看ip了

      ```
      ifconfig  #如果没有这个命令,需要安装的  yum install  net-tools -y
      ```

+ 连接

  ```
  ssh  -p 22   root@192.168.178.253  
  #  ssh是一个远程链接的命令，-p是参数，定义端口的，默认是22可以省去参数， root是用户名 ，后面是ip地址
  
  简写ssh  root@192.168.178.253
  ```

+ 退出`exit`

+ 修改语言

  ```shell
  locale #查看语言包
  localectl  set-locale LANG=zh_CN.UTF8  #永久修改
  ```

  ```shell
  export LC_ALL=en_US.UTF-8  #切换英文
  export LC_ALL=zh_CN.UTF-8  #切换中文
  ```

  

## linux的文档目录结构

![image-20200204175645609](Linux常用命令.assets/image-20200204175645609.png)

- **/bin**：
  bin是Binary的缩写, 这个目录存放着最经常使用的命令。

- **/boot：**
  这里存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。

- **/dev ：**
  dev是Device(设备)的缩写, 该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。

- **/etc：**
  这个目录用来存放所有的系统管理所需要的配置文件和子目录。

- **/home**：
  用户的主目录，在Linux中，每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。

- **/lib**：
  这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。

- **/lost+found**：
  这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。

- **/media**：
  linux系统会自动识别一些设备，例如U盘、光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。

- **/mnt**：
  系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

- **/opt**：
   这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。

- **/proc**：
  这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息。
  这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件，比如可以通过下面的命令来屏蔽主机的ping命令，使别人无法ping你的机器：

  ```
  echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
  ```

- **/root**：
  该目录为系统管理员，也称作超级权限者的用户主目录。

- **/sbin**：
  s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。

- **/selinux**：
   这个目录是Redhat/CentOS所特有的目录，Selinux是一个安全机制，类似于windows的防火墙，但是这套机制比较复杂，这个目录就是存放selinux相关的文件的。

- **/srv**：
   该目录存放一些服务启动之后需要提取的数据。

- **/sys**：
   这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。

  sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。

   

  该文件系统是内核设备树的一个直观反映。

  当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。

- **/tmp**：
  这个目录是用来存放一些临时文件的。

- **/usr**：
   这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。

- **/usr/bin：**
  系统用户使用的应用程序。

- **/usr/sbin：**
  超级用户使用的比较高级的管理程序和系统守护程序。

- **/usr/src：**内核源代码默认的放置目录。

- **/var**：
  这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

## linux常用命令（简单的文件增删改查）

**语法：linux的语法格式 【命令    可选参数      你要操作的对象】**

### 增

+ useradd  创建系统用户的命令 

  + `useradd username`   创建用户username
  + `passwd username`  给该用户修改密码
  + 登录时可使用相应用户名密码

+ mkdir 创建文件夹命令

  + 在某个目录下创建一个文件夹

    ```
    [root@bogon ~]# cd /tmp
    [root@bogon tmp]# mkdir xx01
    ```

  + 同时创建多个文件夹

    ```
    [root@bogon tmp]# mkdir xx02 xx03
    ```

    ```
    [root@bogon tmp]# mkdir ./xx01/{xx0101,xx0102}
    ```

  + 递归创建文件夹

    ```
    [root@bogon tmp]# mkdir -p xx04/xx0401
    ```

+ touch  创建文本文件命令

  用touch命令的都是普通文本文件(存放字符串的文件)

  ```
  [root@bogon tmp]# touch xx02/yy01.txt
  ```

### 删

+ rm 删除命令remove `rm  可选参数   文件名`

  + 有提示删除文件

    ```
    [root@bogon tmp]# rm yy01.txt
    rm：是否删除普通空文件 "yy01.txt"？
    #默认会让用户确认是否删除，输入y删除，输入n取消
    ```

  + 强制删除文件`-f`，无提示（危险慎用-force）

    ```
    [root@bogon tmp]# rm -f yy01.txt 
    ```

  + 递归删除`-r`文件夹（recursive）及其子文件夹，有提示

    ```
    [root@bogon tmp]# rm -r xx01
    rm：是否进入目录"xx01"? y
    rm：是否删除目录 "xx01/xx0101"？y
    rm：是否删除目录 "xx01/xx0102"？
    ```

  + 强制递归删除文件和文件夹，且不给用户提示 `rf`

    ```
    [root@bogon tmp]# rm -rf xx01/* #删除xx01下所有内容，不加*则删除整个文件夹
    ```

### 改

+ cd 命令（change  directory更改目录）

  + cd  /   #切换目录到 根目录下  
  + cd  ./tmp   #切换到当前目录下的，tmp文件夹中

+ vi编辑器的用法过程

  + vi打开文件  vi  file.txt
  + 此时会进入叫做命令模式的状态，输入字母 i，进入编辑模式，这时你键盘敲击动作就是输入字符串了
  + 退出vim需要按下esc，退出编辑模式，回到命令模式下，（注意要是英文输入法）
  + 再输入一个冒号  ，进入底线命令模式，输入 :wq!  表示  write写入   quit 推出 ！感叹号是强制的含义

+ clear清空屏幕

+ hostnamectl set-hostname s26linux 修改主机名，重新登陆生效

+ 安装vim，写一个python的脚本

  + 安装 `yum install  vim -y`

  + 写入内容

    ```
    touch first.py
    vim first.py
    
    #!coding:utf8
    print ("hello world")
    ```

  + 执行`python  first.py `

+ linux的特殊重定向符号

  + echo 输出命令
  + `>`   重定向输出覆盖符,等同于w模式，覆盖写 
  + `>>` 重定向追加输出符,等同于r模式，追加写入
  + `<`重定向写入覆盖符,数据库数据导入时候用到
  + `<<`重定向追加写入符

+ cp 复制命令

  + 语法：cp  源文件  拷贝后的文件   可写文件路径

  + 拷贝单个文件

    ```
    [root@mypc ~]# cp first.py first2.py
    ```

  + 拷贝文件夹 ，需要递归的参数 `-r`递归拷贝

    ```
    [root@mypc ~]# cp -r xx01 xx02
    ```

+ mv 一个是移动的作用，二重命名的作用

  + 移动文件夹

    ```
    [root@mypc ~]# mv ./xx01 ./xx02
    ```

  + 重命名

    ```
    [root@mypc ~]# mv first.py first.pp
    ```

  + 重命名文件夹

    1. 新的文件夹名字不存在，则改名
    2. 新的文件夹名字存在，则是移动到此目录下

### 查

+ pwd （print work direcotry 打印工作目录，我在哪的意思，输出当前所处的绝对路径）

+ whoami  查看当前用户

+ ls .  点特殊文件夹，代表当前目录

+ ls .. 上级目录

+ ls  -   上一次的工作目录

+ ls  ~   当前登录用户的 家目录

+ ls  -l  /tmp  列出/tmp目录下详细内容

+ which  哪一个 

  ```
  which python  #去环境变量中，寻找是否存在python解释器  ，也就是PATH变量
  ```

+ cat 查询文件内容的命令

  + cat  文件名

  + 追加写入内容自定义停止符EOF---可换

    ```
    [root@s26linux tmp]# cat >> second.py<<EOF
    > #!coding:utf8
    > print("来左边跟我一起画个龙，在你右边划一刀彩虹")
    > EOF---停止命令
    ```

+ echo 打印的命令

  + linux定义一个变量  name="大郎"
  + 取出变量的值 echo $name

+ hostname  查看主机名字

+ linux的命令帮助信息查看help

  + ls --help  #查看简单帮助信息
  + man手册，查看命令的详细说明文档  man  ls

+ find 查询命令

  + 命令语法

    ```
    find  从哪找   -name   你要找的东西名字是什么
    ```

  + 在linux下全局搜索  以.txt结尾的文件

    ```
    find  /   -name   "*.txt"
    ```

  + 搜索/etc/ 目录下，进行局部搜索，找出网卡的文件，提示，网卡文件名字以 ifcfg开头

    ```
    find    /etc     -name     "ifcfg*"
    ```

  + -type 查找某一类型的文件

    + b - 块设备文件。
    + d - 目录。
    + c - 字符设备文件。
    + p - 管道文件。
    + l - 符号链接文件。
    + f - 普通文件。
    + s - socket文件

  + 全局搜索，和python相关的文件夹

    ```
    find  /  -type  d   -name "python*"
    ```

  + 全局搜索，和python相关的文件，找出来

    ```
    find  /  -type  f   -name "python*"
    ```

    