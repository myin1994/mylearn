# 进入客户端 mysql
#  mysql>

# 退出mysql客户端
#     mysql>exit
#     mysql>quit

# 和用户相关的命令
    # mysql>select user()  查看当前是以什么用户登录的sever端
    #输入;表示结束

# root用户（程序当中拥有最高的权限）
    #使用root 用户登录sever
    #mysql -uroot
    #mysql -uroot -p 输入密码
    #mysql -uguest -h192.168.34.112 -p
#设置密码
#mysql>set password = password("password")
#创建用户并授权（root用户）
#mysql> grant all on *.* to 'eva'@'%' identified by '123'
#mysql> grant 权限 on 文件.文件 to '用户名'@'IP段%' identified by '密码';
#mysql> flush privileges;    # 刷新使授权立即生效

# 创建一个文件夹
#mysql>creat database filename;

# mysql查看所有用户select user,host from mysql.user;