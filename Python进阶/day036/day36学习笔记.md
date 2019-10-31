## 多表连接查询

+ 交叉连接

   **不适用任何匹配条件。生成笛卡尔积** 

  ```mysql
  select * from 表1,表2
  #将表1的每一条记录分别与表2的每一条记录组合成为新的一条记录
  ```

  

+ 内连接---只连接匹配的行（表1和表2中不符合条件的数据都会被丢弃）

  + 直接连接同通过where加条件（通过两表匹配字段）

    ```mysql
    select * from 表1,表2 where 表1字段 = 表2字段;
    ```

  + inner join……on

    ```mysql
    select * from 表1 inner join 表2 on 表1字段 = 表2字段;
    ```

  **注：重名通过表名.获取**

+ 外连接

  + 左外连接 left join   ---优先显示左表全部记录(本质：在内连接的基础上增加左边有右边没有的结果)

    ```mysql
    select * from 表1 left join 表2 on 表1字段 = 表2字段;
    ```

  + 右外连接 right join   ---优先显示右表全部记录(本质：在内连接的基础上增加右边有左边没有的结果)

    ```mysql
    select * from 表1 right join 表2 on 表1字段 = 表2字段;
    ```

  +  全外连接union--显示左右两个表全部记录
  
    ```mysql
    select * from 表1 left join 表2 on 表1字段 = 表2字段;
    union
    select * from 表1 right join 表2 on 表1字段 = 表2字段;
    
    #注意 union与union all的区别：union会去掉相同的纪录
    ```
  
+ 子查询（一个select语句中总是出现另一个select语句）

   + 子查询是将一个查询语句嵌套在另一个查询语句中。
   + 内层查询语句的查询结果，可以为外层查询语句提供查询条件。
   + 子查询中可以包含：IN、NOT IN、AND、ALL、EXISTS 和 NOT EXISTS等关键字
   + 还可以包含比较运算符：= 、 !=、> 、<等

   ```
   备注：如果查出来的一张表需要连表，那么被查出来的表必须定义一个名字,如果查出的一张表中，显示字段引入了函数，那么这个字段必须重命名，才能在后续的查询中使用
   ```

   

## 数据库备份与恢复

+ 备份

  + 单库备份

    ```mysql
    mysqldump -uroot -p123 db1 > db1.sql
    mysqldump -uroot -p123 db1 table1 table2 > db1-table1-table2.sql
    ```

  + 多库备份

    ```mysql
    mysqldump -uroot -p123 --databases db1 db2 mysql db3 > db1_db2_mysql_db3.sql
    ```

  + 备份所有库

    ```mysql
    mysqldump -uroot -p123 --all-databases > all.sql
    ```

    

+ 恢复（比单纯写入快-网络传输+优化器优化）

  ```
  mysql -uroot -p123 < /backup/all.sql
  
  source path;路径不能包含中文
  ```

  

## pymysql模块

+ 连接服务器

  ```python
  import pymysql
  conn = pymysql.connect(host="localhost",user="root",password="xxxx",database="dbname")
  
  cur = conn.cursor() #使用 cursor() 方法创建一个游标对象 cur
  ```

+ 创建表操作

  ```python
  # 使用 execute() 方法执行 SQL，如果表存在则删除
  cur.execute("DROP TABLE IF EXISTS test1")
  ```

  ```python
  # 使用预处理语句创建表
  sql = """CREATE TABLE test1 (
           FIRST_NAME  CHAR(20) NOT NULL,
           LAST_NAME  CHAR(20),
           AGE INT
           )"""
   
  cur.execute(sql)
  ```

+ 查询

  ```python
  cur.execute("select * from book")#陆续获取数据并记录位置
  ```

  + 获取一条记录

    ```python
    print(cur.fetchone()) #均为元组组成的元组
    ```

  + 获取指定数量记录

    ```python
    print(cur.fetchmany(2))
    ```

  + 获取剩余全部记录

    ```python
    print(cur.fetchall())
    ```

  + 获取查询到的记录总条数

    ```python
    cur.execute("select * from test1")
    print(cur.rowcount) #只读，每次execute执行后即确定不更改
    ```

    

+ 插入/更新/删除（执行后先保存在缓存中，commit后提交到数据库执行）

  + 插入

    ```python
    cur.execute("insert into test1 values(4,4,4)")
    conn.commit()
    ```

  + 更新

    ```python
    cur.execute("update test1 set first_name='张三' where age=4")
    conn.commit()
    ```

  + 删除

    ```python
    cur.execute("delete from test1 where age=3")
    conn.commit()
    ```

  + 回滚 rollback（ DML 才能 rollback ）

    数据库里做修改后 （ update ,insert , delete）未commit 之前 使用rollback 可以恢复数据到修改之前。

    ```python
    try:
        cur.execute("insert into test1 values(4,4,4,5)")
        conn.commit()
    except:
        conn.rollback()
    ```

+ 关闭游标及数据库连接

  ```python
  cur.close()
  conn.close()
  ```

+ sql传入时的方法

  ```python
  username = input("用户名")
  password = input("密码")
  # sql = f'select * from userinfo where user ="{username}" and password ="{password}"'
  sql = 'select * from userinfo where user =%s and password =%s'
  #使用%s，%d占位后用元组按位置传参，避免sql注入问题
  ret = cur.execute(sql,(username,password))
  if ret:
      print("登录成功")
  else:
      print("登录失败")
  ```

+ 防护

  ```
  归纳一下，主要有以下几点：
  1.永远不要信任用户的输入。对用户的输入进行校验，可以通过正则表达式，或限制长度；对单引号和
  双"-"进行转换等。
  2.永远不要使用动态拼装sql，可以使用参数化的sql或者直接使用存储过程进行数据查询存取。
  3.永远不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接。
  4.不要把机密信息直接存放，加密或者hash掉密码和敏感的信息。
  5.应用的异常信息应该给出尽可能少的提示，最好使用自定义的错误信息对原始错误信息进行包装
  6.sql注入的检测方法一般采取辅助软件或网站平台来检测，软件一般采用sql注入检测工具jsky，网站平台就有亿思网站安全平台检测工具。MDCSOFT SCAN等。采用MDCSOFT-IPS可以有效的防御SQL注入，XSS攻击等。
  ```

  
