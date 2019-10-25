# 1.目录选择
    #不能带中文 空格  \tools

# 2.创建my.ini 修改配置文件

# 3.配置环境变量 bin目录

# 4.以管理员身份运行cmd

# 5.mysqld install 安装-->Service successfully installed.
#    net start mysql启动验证--->MySQL 服务正在启动 .  MySQL 服务已经启动成功。

# 若缺少系统文件则进行安装

# 重新安装方法 mysqld remove
# 删除安装包并重启-重新解压再重装

# 关闭sever端
# net stop mysql

# 6.通过客户端操作mysql服务端
    #mysql自带的客户端
    #python代码
    #第三方软件  navcat

# 7.注意
    #my.ini不能打开，始终要记得编码问题utf-8
    #默认开机自启动的服务

# 8.分清客户端（mysql.exe）和服务端