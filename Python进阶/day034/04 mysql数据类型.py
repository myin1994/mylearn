# 数值型
    #整数
        #tinyint 1字节  默认-有符号（-128,127） unsigned-无符号（0-255） 小整数型（如年龄）
        #int 4字节
        #create table i1(ti tinyint,i int, tiu tinyint unsigined,iu int unsigned);
        #insert into i1 values(-10,-10,-10,-10); 超限 -10 -10 0 0
        #insert into i1 values(255,255,255,255); 超限  127 |  255 |  255 |  255

    #小数
        # float float(255-一共多少位,30-小数点后多少位)
        # double double一般不设置
         #create table i2(f float,d double, f2 float(5,2),d2 double(5,2))
         # insert into i2 values(1.222222222222222222233333,1.222222222222222222233333,1.222222222222222222233333,1.222222222222222222233333);
         # 1.22222 | 1.2222222222222223 | 1.22 | 1.22
        #decimal 高精度（底层使用字符串）小数点前最多35位

# 字符串 必须约束长度
    #char 0-255 字符 自动去除空格  存取快，浪费空间  手机号码 身份证号
        #定长：char(10),自动补空格
    #varchar 0-65535 不去除空格 节省空间，存取慢  评论 发布的微博
        #变长：varchar(10) "a(1)" "aa(2)-标识"
    #create table s1(c char(4),vc varchar(4));

# 时间
    #datetime  8字节 年月日时分秒 开奖时间 聊天记录 转账 打卡时间
    #date：年月日 生日 入职离职
    #time：时分秒 上课时间 闹钟 体育项目/计时
    #year：年 以年为单位统计
    #timestamp时间戳：已经不常用了;不能为空，默认添加；自动记录修改时间
    #create table t1(dt datetime,d date,t time,y year,ts timestamp)
    #insert into t1 values(now(),now(),now(),now(),now())
    #insert into t1(dt) values("20170808100000")
    #create table t2(y year,dt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)

# set和enum
    #enum  枚举方法 单选方法
        #性别
    #set 集合方法 多选方法/去重  引号中写逗号
        #爱好
    #create table se1(gender enum("male","female"),hobby set("抽烟","喝酒")）


# 函数
    #user();
    #database();
    #password();
    #now();