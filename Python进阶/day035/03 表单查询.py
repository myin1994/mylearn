# create table employee(
# id int not null unique auto_increment,
# emp_name varchar(20) not null,
# sex enum('male','female') not null default 'male', #大部分是男的
# age int(3) unsigned not null default 28,
# hire_date date not null,
# post varchar(50),
# post_comment varchar(100),
# salary double(15,2),
# office int, #一个部门一个屋子
# depart_id int
# );

# #插入记录
# #三个部门：教学，销售，运营
# insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
# ('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
# ('alex','male',78,'20150302','teacher',1000000.31,401,1),
# ('wupeiqi','male',81,'20130305','teacher',8300,401,1),
# ('yuanhao','male',73,'20140701','teacher',3500,401,1),
# ('liwenzhou','male',28,'20121101','teacher',2100,401,1),
# ('jingliyang','female',18,'20110211','teacher',9000,401,1),
# ('jinxin','male',18,'19000301','teacher',30000,401,1),
# ('成龙','male',48,'20101111','teacher',10000,401,1),
#
# ('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
# ('丫丫','female',38,'20101101','sale',2000.35,402,2),
# ('丁丁','female',18,'20110312','sale',1000.37,402,2),
# ('星星','female',18,'20160513','sale',3000.29,402,2),
# ('格格','female',28,'20170127','sale',4000.33,402,2),
#
# ('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
# ('程咬金','male',18,'19970312','operation',20000,403,3),
# ('程咬银','female',18,'20130311','operation',19000,403,3),
# ('程咬铜','male',18,'20150411','operation',18000,403,3),
# ('程咬铁','female',18,'20140512','operation',17000,403,3)
# ;

# select * from 表;（对列进行筛选）
# select 字段,字段 from 表;

#避免重复distinct
    # SELECT DISTINCT post FROM employee;

#通过四则运算查询
    # SELECT emp_name, salary*12 FROM employee;
    # SELECT emp_name, salary*12 AS Annual_salary FROM employee;重命名
    # SELECT emp_name, salary*12 Annual_salary FROM employee;重命名


# 两个函数
    #concat（） 拼接
    #concat_ws（"符号"）
# 定义显示格式
# CONCAT()
# 函数用于连接字符串
# SELECT
# CONCAT('姓名: ', emp_name, '  年薪: ', salary * 12)
# AS
# Annual_salary
# FROM
# employee;
#
# CONCAT_WS()
# 第一个参数为分隔符，用分隔符进行连接
# SELECT
# CONCAT_WS(':', emp_name, salary * 12)
# AS
# Annual_salary
# FROM
# employee;

# 结合CASE语句：
#    SELECT
#        (
#            CASE
#            WHEN emp_name = 'jingliyang' THEN
#                emp_name
#            WHEN emp_name = 'alex' THEN
#                CONCAT(emp_name,'_BIGSB')
#            ELSE
#                concat(emp_name, 'SB')
#            END
#        ) as new_name
#    FROM
#        employee;


# where关键字（对行进行筛选）
# 比较运算 > < = >= <= != <>
# 范围：in(18,20,30)
#       between and

# 模糊查询
    #like
        #name like "a%"---%代表任意长度
        #name like "%a%"---含有a
        #name like "a_"---任意一个字符
    #regexp
        #name regexp "^a"


# 逻辑运算
    #and
    #or
    #not ：not in,is not null


# group 分组-做统计
# group by 字段  根据这个字段分组

# 统计函数--聚合函数
    #count sum min max


# having--用于过滤组


# order by 默认升序(asc)排列(desc降序)
# select * from 表 order by 字段;
# select * from 表 order by 字段 asc;
# select * from 表 order by 字段 desc;
# select * from 表 order by 字段1 desc,字段2 asc;首先按照字段1从大到小排，字段1相同时按照字段2从小到大排

# limit x取前x
# limit x.y 从x+1开始取取y条  用于分页


