## 补充知识点

+ 服务器：部署了服务的机器都是服务器
+ sql语言的3种类型
  + DDL（DATABASE DEFINE LANGUAGE）：数据库定义语言
    +  数据库、表、视图、索引、存储过程，例如CREATE DROP ALTER 
  + DML（D MANGAGE L）:数据库操纵语言
    +  插入数据INSERT、删除数据DELETE、更新数据UPDATE、查询数据SELECT 
  + DCL（D CONTROL L）：数据库控制语言
    +  例如控制用户的访问权限GRANT、REVOKE 
+ 表的介绍
  + 字段行-创建时决定
  + 数据-横向的一条数据称为一条记录



## mysql数据类型

+ 数值型

  + 整数-超限自动取最大范围值
    + tinyint -小整数值（用于定义年龄等）
      + 长度：1字节
      + 默认：有符号，-符号占一位（-128,127）
      + unsigned：无符号（0,255）
    + int-大整数值
      + 长度：4字节
      + 默认：有符号 (-2 147 483 648，2 147 483 647) 
      + unsigned： (0，4 294 967 295) 
  + 小数
    + float-单精度浮点数值
      + 使用：float(m,n)  m-一共多少位  n-小数点后占位数
    + double- 双精度浮点数值 
      + 使用：可限制但一般不加
    + decimal-高精度（底层使用字符串）
      + 默认： decimal(10,0)--使用时需要进行设置（整数位最大为35）

+ 字符串（必须约束长度）

  + char- 定长字符串 （手机号码、身份证号）
    + 长度：0-255 字符，存储时自动按位数补充空格（取时再去除）
    + 存取快，浪费空间
  + varchar- 变长字符串 （评论、发布的微博）
    + 长度：0-65535 不增加去除空格，底层会在最后标识长度
    + 节省空间，存取慢

+ 时间

  + datetime  8字节 年月日时分秒 开奖时间 聊天记录 转账 打卡时间

  + date：年月日 生日 入职离职

  + time：时分秒 上课时间 闹钟 体育项目/计时

  + year：年 以年为单位统计

  + timestamp时间戳：已经不常用了;不能为空，默认添加；自动记录修改时间

  + 自动获取时间戳格式的约束条件

    ```mysql
    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    ```

+ set和enum

  + set-集合方法（多选，去重，如爱好）（多选时再引号中写逗号进行选择）
  + enum-枚举方法（单选，如性别）
  
  ```mysql
  create table x1(gender enum("男","女"), hobby set("抽烟","读书","音乐"));
  
  insert into x1 values("男","读书,音乐");
  
                  +--------+---------------+
                  | gender | hobby         |
                  +--------+---------------+
                  | 男     | 读书,音乐       |
                  +--------+---------------+
  ```
  
+ sql中的函数

  + user()
  + database()
  + password()
  + now() 当前时间



## 完整性约束

+ unsigned 无符号

+ not null  非空约束

  ```mysql
  create table x1(id int not null,name char(20));
  
  mysql> insert into x1 values(null,1222);
  ERROR 1048 (23000): Column 'id' cannot be null
  mysql> insert into x1(name) values(1222);
  ERROR 1364 (HY000): Field 'id' doesn't have a default value
  ```

  + not null不生效需设置严格模式（设置后对数据类型有影响-输入格式不对会报错）

    + 不支持对not null字段插入null值
    + 不支持对自增长字段插入”值
    + 不支持text字段有默认值

    ```mysql
    直接在mysql中生效(重启失效):
    mysql>set sql_mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION";
    
    配置文件init添加(永久失效)：
    sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
    ```

+ default  设置默认值（一般与not null配合使用）

  ```mysql
  mysql> create table x1(id int,name char(20) not null default "张三");
  mysql> insert into x1(id) values(1),(2);
  
  mysql> select * from x1;
  +------+--------+
  | id   | name   |
  +------+--------+
  |    1 | 张三    |
  |    2 | 张三    |
  +------+--------+
  ```

+ unique  唯一约束

  + 指定某字段（ 指定某列或者几列组合不能重复-联合唯一 ）--不会约束null

    ```mysql
    create table x1(id int unique,name char(20),password char(32), unique(name,password));
    ```

  + 非空唯一(仅有时自动变为主键)

    ```mysql
    mysql> create table x1(id int unique not null,name char(20) not null unique);
    
    mysql> desc x1;
    +-------+----------+------+-----+---------+-------+
    | Field | Type     | Null | Key | Default | Extra |
    +-------+----------+------+-----+---------+-------+
    | id    | int(11)  | NO   | PRI | NULL    |       |
    | name  | char(20) | NO   | UNI | NULL    |       |
    +-------+----------+------+-----+---------+-------+
    ```

+ primary key  主键

  主键为了保证表中的每一条数据的该字段都是表格中的唯一值且不为空。 

  ```
  主键可以是属性或属性组。有时候必须多个属性组成的属性组作为主键才能唯一标识每个元组。有时候也只有联合主键才更符合实际情况。
  联合主键一般用在多对多联系上。
  例如大学的选课系统。每个学生可以选修多门课程，每门课程可以有多名学生选修。每个学生选修的每门课程有一个分数。那么现在建立“选课”这个表，有学生学号、课程号、分数3个属性。那么需要设学号和课程号为联合主键。因为单靠学号或单靠课程号都无法唯一标示一个元组（因为每个学生可以选修多门课程，每门课程可以有多名学生选修）。
  ```

  + 单字段主键
    + unique+not null
    + 字段后直接约束primary key---不能同时设置多个主键
    + 在所有字段后单独定义primary key(字段名)
    + int 主键默认为0，char默认值为空字符串“”？？？
  + 联合主键-多个字段组合用作主键
    + 在所有字段后单独定义primary key(字段名1,字段名2)

+ auto_increment  自增（自带not null约束）必须为键

  + 不指定id，则自动从1开始增长

  + 指定id后除非重新设置偏移量，否则删除后也仍从删除的位置增长

  + 使用truncate清空表，则重新从起始位置增长

    ```mysql
    truncate 表名;
    ```

  + 修改自增字段的起始值

    ```mysql
    mysql> alter table 表名 auto_increment=3;
    ```

  + 创建表时指定初始值（放于括号外）

    ```mysql
    create table x1(id int primary key auto_increment,name varchar(20))auto_increment=3;
    ```

  + 步长可设置

+ foreign key外键约束（一般管理主键）

  一般将重复使用的值单独拆出一张表，然后使用外键将其关联（如工号-姓名-部门）

  + 先建立外键表（父表），且外键表对应字段唯一

    ```mysql
    mysql> create table department(pid int primary key,pname char(20));
    ```

  + 然后建立关联表（子表）

    ```mysql
    mysql> create table workers(id int primary key,code char(12),pid int,foreign key(pid) references department(pid));
    
    mysql> show create table workers;
    +---------+----------------------------------------------------------
    | workers | CREATE TABLE `workers` (
      `id` int(11) NOT NULL,
      `code` char(12) DEFAULT NULL,
      `pid` int(11) DEFAULT NULL,
      PRIMARY KEY (`id`),
      KEY `pid` (`pid`),
      CONSTRAINT `workers_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `department` (`pid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
    +---------+----------------------------------------------------------
    ```

  + 级联更新on update cascade---修改父表同步修改子表

  + 级联删除on delete cascade---删除父表记录同步删除子表中对应记录



## 修改表结构

+ 修改表名

  ```mysql
  alter table 表名 rename 新表名;
  ```

+ 增加字段

  ```mysql
  alter table 表名 add 字段名 数据类型 [完整性约束条件…],……
  ```

+ 删除字段

  ```mysql
  alter table 表名 drop 字段名;
  ```

+ 修改字段

  + 仅修改数据类型

    ```mysql
    alter table 表名 modify 字段名 数据类型 [约束条件];
    ```

  + 修改名字及数据类型

    ```mysql
    alter table 表名 change 旧名 新名 数据类型 [约束条件];
    ```

+ 修改字段排列顺序/在增加的时候指定字段位置

  修改时在约束条件后追加first--第一行/after 字段名--在某字段之后



## 多表结构的创建与分析

+ 多对一

  一个表（子表）的多条记录可以对应另一个表（父表）的一条记录，则外键建立在子表（对应多的表）中。

  ```mysql
  一对多（或多对一）：一个出版社可以出版多本书
  关联方式：foreign key
  
  mysql> create table press(
      id int primary key auto_increment,
      name varchar(20));
  
  mysql> create table book(
      id int primary key auto_increment,
      name varchar(20),
      press_id int not null,
      foreign key(press_id) references press(id) 
      on delete cascade 
      on update cascade);
  
  mysql> desc book;
  +----------+-------------+------+-----+---------+----------------+
  | Field    | Type        | Null | Key | Default | Extra          |
  +----------+-------------+------+-----+---------+----------------+
  | id       | int(11)     | NO   | PRI | NULL    | auto_increment |
  | name     | varchar(20) | YES  |     | NULL    |                |
  | press_id | int(11)     | NO   | MUL | NULL    |                |
  +----------+-------------+------+-----+---------+----------------+
  
  mysql> desc press;
  +-------+-------------+------+-----+---------+----------------+
  | Field | Type        | Null | Key | Default | Extra          |
  +-------+-------------+------+-----+---------+----------------+
  | id    | int(11)     | NO   | PRI | NULL    | auto_increment |
  | name  | varchar(20) | YES  |     | NULL    |                |
  +-------+-------------+------+-----+---------+----------------+
  
  mysql> insert into press(name) values("出版社1"),("出版社2"),("出版社3");
  
  mysql> insert into book(name,press_id) values("book1",1),("book2",2),("book3",3),("book4",1),("book5",2),("book6",3);
  ```

  

+ 一对一（如员工信息拆分）

  两表互相一条记录唯一对应另一个的一条记录，则在后有的表上添加外键+unique

+ 多对多（如书籍和作者）

  两表互相一条记录对应另一表的多条记录，则需要添加第三个表通过两个外键分别关联两个表的主键

  ```mysql
  #多对多
  三张表：出版社，作者信息，书
  
  多对多：一个作者可以写多本书，一本书也可以有多个作者，双向的一对多，即多对多
  　　
  关联方式：foreign key+一张新的表
  
  mysql> create table author(
      id int primary key auto_increment,
      name varchar(20));
  
  mysql> create table author2book(
      id int not null unique auto_increment,
      author_id int not null,
      book_id int not null,
      constraint fk_author foreign key(author_id) references author(id) on delete cascade on update cascade,
      constraint fk_book foreign key(book_id) references book(id) on delete cascade on update cascade,
      primary key(author_id,book_id));
  
  mysql> desc author;
  +-------+-------------+------+-----+---------+----------------+
  | Field | Type        | Null | Key | Default | Extra          |
  +-------+-------------+------+-----+---------+----------------+
  | id    | int(11)     | NO   | PRI | NULL    | auto_increment |
  | name  | varchar(20) | YES  |     | NULL    |                |
  +-------+-------------+------+-----+---------+----------------+
  
  mysql> desc author2book;
  +-----------+---------+------+-----+---------+----------------+
  | Field     | Type    | Null | Key | Default | Extra          |
  +-----------+---------+------+-----+---------+----------------+
  | id        | int(11) | NO   | UNI | NULL    | auto_increment |
  | author_id | int(11) | NO   | PRI | NULL    |                |
  | book_id   | int(11) | NO   | PRI | NULL    |                |
  +-----------+---------+------+-----+---------+----------------+
  
  mysql> insert into author(name) values("au1"),("au2"),("au3"),("au4");
  
  mysql> insert into author2book(author_id,book_id) values(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,6),(3,4),(3,5),(3,6),(4,1);
  ```

  