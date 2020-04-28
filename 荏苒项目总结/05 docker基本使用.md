# Docker 介绍

*Docker*是一款于安装部署项目运营时需要的软件和依赖的工具，类似于VMware虚拟机平台。

docker可以通过git从docker官网仓库中下载各种各样的镜像到本地，然后可以通过命令，对镜像进行操作。

# Docker 安装

+ 官网：https://docs.docker.com/
+ Docker 提供了两个版本：社区版 (CE) 和企业版 (EE)
+ docker palyground
  + 地址：https://labs.play-with-docker.com/
  + 直接使用云端的docker

## ubuntu安装

> 更新ubuntu的apt源索引

```shell
sudo apt-get update
```

> 安装包允许apt通过HTTPS使用仓库

```shell
sudo dpkg --configure -a
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

> 添加Docker官方GPG key【这个是国外服务器地址，所以网路不好的时候，会失败！在网路好的情况下，多执行几次就没问题了】

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

> 设置Docker稳定版仓库

```shell
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

> 添加仓库后，更新apt源索引

```shell
sudo apt-get update
```

> 前面的准备工作完成以后，接下来安装最新版Docker CE（社区版）

```shell
sudo apt-get install docker-ce
```

> 检查Docker CE是否安装正确

```shell
sudo docker run hello-world
```

> 出现了`helo from Docker`则表示上面的安装成功！

![1563502563172](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday109/day023/assets/1563502563172.png)



![1563503374720](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday109/day023/assets/1563503374720.png)



我们获取镜像文件，可以直接去官方网站上获取: https://hub.docker.com/

## centos安装

> 卸载旧的版本

```shell
yum remove docker \
docker-client \
docker-client-latest \
docker-common \
docker-latest \
docker-latest-logrotate \
docker-logrotate \
docker-selinux \
docker-engine-selinux \
docker-engine
```

> 安装依赖

```shell
yum install -y yum-utils \
device-mapper-persistent-data \
lvm2
```

> 添加repository

```shell
yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
```

> 查询可以装什么docker版本

```shell
yum list docker-ce --showduplicates | sort -r
```

> 安装指定版本

```shell
yum -y install docker-ce-18.06.1.ce-3.el7
```

> 查看版本信息

```shell
docker version
```

# Docker 命令

## 通用命令

### 查看docker 当前版本

```shell
docker --version  # 查看整个docker的版本。
docker version
```

### 启动docker

```bash
# 启动docker
sudo service docker start

# 停止docker
sudo service docker stop

# 重启docker
sudo service docker restart

#设置开机自启
systemctl enable docker
```



## 镜像操作[image]

### 列出所有镜像

```shell
docker image ls
# 上面的命令时省略了 --all
docker image ls --all
```

> 根据镜像id，查看到镜像分层信息

```shell
docker history <镜像名称:版本号>
```

### 拉取镜像

下载镜像，默认从官网镜像库下载镜像的，也可以修改docker的源，让docker从国内其他镜像库下载镜像回来。

这可以达到下载加速的作用。

例如，使用阿里云的镜像源：

```shell
sudo vim /etc/docker/daemon.json   # 文件如果不存在，则创建
# 添加如下内容：


{
  "registry-mirrors": ["https://2xdmrl8d.mirror.aliyuncs.com"]
}
或者
{
"registry-mirrors": [
"https://kfwkfulq.mirror.aliyuncs.com",
"https://2lqq34jg.mirror.aliyuncs.com",
"https://pee6w651.mirror.aliyuncs.com",
"https://registry.docker-cn.com",
"http://hub-mirror.c.163.com"
],
"dns": ["8.8.8.8","8.8.4.4"]
}
# 重启docker即可。

```

如果不指定版本号，默认拉取最新版本的镜像

```shell
docker image pull <镜像名称:版本号>
```

### 删除镜像

删除的时候，必须注意是否有容器在运行当前镜像文件，如果在使用，则需要先删除容器，才能删除镜像

```shell
docker image rm <镜像名称/镜像ID>:版本号
```

删除的镜像如果被容器提前使用了，则错误如下：

![1563504236734](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday109/day023/assets/1563504236734.png)

### 制作镜像

> 创建源文件,命名固定

```shell
vim Dockerfile
```

> 写入内容

```shell
FROM ubuntu
CMD echo "hello my"
```

> 编译镜像

```shell
docker build -t my/hello-world .
```

### 把docker中的镜像打包成文件

用于分享发送给他人，或备份

```shell
docker save -o <文件名.tar.gz>  <镜像名>
```

### 把镜像文件加载到docker中

```shell
docker load -i <文件名.tar>
```

### Dockerfile详解

+ FROM：从哪开始，从一个系统开始

  ```shell
  FROM scratch         # 最小系统
  FROM centos         
  FROM ubuntu:14.04
  ```

+ LABEL：注释

  ```shell
  LABEL version=”1.0”
  LABEL auther=”sjc”
  ```

+ RUN：执行命令，每RUN一次，会多一个系统分层，尽量少一些层

  ```shell
  RUN yum -y update && install lrzsz \ 
  net-tools
  ```

+ WORKDIR：进入或创建目录，尽量不要用相对路径

  ```shell
  WORKDIR /root     # 进入 /root 目录
  WORKDIR /test     # 会在根下，创建 /test 并进入
  WORKDIR demo    # 创建demo，进入
  RUN pwd          # /test/demo
  ```

+ ADD and COPY：将本地的文件，添加到image里，COPY和ADD区别是不会解压

  ```shell
  ADD hello /  # 将当前目录下hello，添加到容器的根下
  ADD tt.tar.gz /  # 压缩包扔进去，并解压
  ```

+ ENV，增加Dockerfile的可读性，健壮性

+ CMD and ENTRYPOINT：执行命令或运行某个脚本

  + Shell和Exec格式

    ```shell
    FROM centos
    #shell格式
    CMD echo "hello docker"
    #exec格式
    CMD ["/bin/echo","hello docker"]
    ENTRYPOINT ["/bin/echo","hello docker"]
    ```

  + ENTRYPOINT与CMD：容器启动时，运行什么命令

    ```shell
    ENTRYPOINT ["docker-entrypoint.sh"]
    CMD ["mysqld"]
    ```

    **ENTRYPOINT比CMD用的多，因为CMD有可能执行完前面的，把后面定义的CMD给忽略不执行了**

## 容器操作[container]

### 创建容器

必须先有镜像，才能运行创建容器，需要指定使用的镜像名，并且设置创建容器以后，执行对应的第一条命令 ，

如果本地不存在则去仓库下载创建。

```shell
docker run <参数选项> <镜像名称> <命令>
```

例如：使用"hello-world"镜像，创建一个容器，但没有进行任何操作

```shell
docker run hello-world
```

例如：使用ubuntu镜像，创建一个名为ubuntu1

```
docker pull ubuntu:18.04
docker run -it --name=ubuntu1 ubuntu:18.04 bash
```

注意：必须启动的时候，让容器运行bash解析器，才能在接下来的操作让容器不会立刻关闭，而且也能够让我们可以输入linux终端命令， 如果我们一般创建一个容器，选项都是： -itd

### docker run的选项

> -t    表示容器启动后会进入其命令行终端

> -i     表示以“交互模式”运行容器

> --name  表示设置容器的名称

> -d    创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器，如果只加-i -t 两个参数，创建后就会自动进去容器)

> -p    指定端口映射，格式为：**主机(宿主)端口:容器端口**

> -e 变量名="变量值"   设置环境变量

> --network=host    指定容器的网络连接类型

> --restart=always   在docker重启的时候，是否要自动重启容器

> -v 把docker外接的目录和指定容器内部的目录进行映射，共享文件

例如，使用ubuntu镜像，创建一个名为ubuntu，并且在后台运行的容器像

```
docker run -itd --name=ubuntu ubuntu<:版本>
```

### 列出所有容器

```shell
docker container ls                      # 所有正在启动运行的容器

docker container ls --all                # 所有容器[不管是否在启动运行中]
```

### 启动容器

> 可以同时启动多个容器，容器之间使用空格隔开

```shell
# 启动一个容器
docker container start <容器名称/容器ID>

# 启动多个容器
docker container start <容器名称/容器ID>  <容器名称/容器ID> <容器名称/容器ID>
```

### 停止容器

```shell
docker container stop <容器名称/容器ID>
```

### 杀死容器

在容器无法停止的时使用[强制关机，相当于电源]

```shell
docker container kill <容器名称/容器ID>
```

### 进入容器

要进入容器，必须当前容器是启动状态的

```shell
docker container exec -it <容器名称/容器ID>  <第一个命令>
```

**注意：第一个命令根据镜像决定（常用bash）**

### 删除容器

> 删除某个容器

```shell
docker  container rm <容器名称/容器ID>
```

> 删除所有容器

```shell
docker rm $(docker container ls -aq)
```

> 删除没有在运行的容器

```shell
docker rm $(docker container ls -f "status=exited" -q)
```

### 复制文件

+ 语法  

  >docker cp  原地址:新地址

+ 使用

  1. 从外界复制文件到指定容器中

     ```shell
     sudo docker container cp <路径/文件名>  <容器名称/容器ID>:<路径/文件名>
     ```

  2. 从容器内部复制文件到外界来

     ```shell
     sudo docker container cp <容器名称/容器ID>:<路径/文件名>  <路径/文件名>
     ```

### 把容器保存成镜像

```shell
docker commit <容器名称/容器ID>  <新镜像名>:<版本号>
```

## 扩展

使用docker命令需要管理员权限，如果希望每次输入docker相关命令时，不用sudo，可通过以下命令进行设置

[以下操作不保证有效！]

```shell
sudo usermod -a -G docker $USER
sudo service docker restart
newgrp - docker
```

官方提供的ubuntu系统镜像，工具命令很少，如希望内部安装ping、ifconfig网卡或者vim等工具，可以通过以下命令进行设置[需要联网，而且耗时]

```shell
apt-get update
apt install net-tools        # ifconfig 
apt install iputils-ping     # ping
```

