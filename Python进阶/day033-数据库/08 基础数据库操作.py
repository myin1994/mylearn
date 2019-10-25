#数据库 database db 文件夹
    # show databases; 显示所有数据库（文件夹）
    # create database 文件夹名;
    # use database数据库名-切换文件夹
    # select databse(); 查看当前所在的文件夹

# 表操作
    #显示当前文件都有哪些表
    #create table 表名(id int,name char(最大长度20),age int)
    # show tables; 显示当前数据库所有表
    #drop table 表名; 删除表
    #desc 表名；查看表结构
    #show create table 表名；查看表结构，更完整
    #alter table ts01 rename to ts01_new; 修改表名

# 数据操作
    #增insert
        #insert into 表名 values(数据1,数据2,数据3)
        #insert into table1 values(1,"alex","alex1234")
        #insert into table1 (id,username) values(2,"wusir") #指定字段
        #insert into table1 values(3,"alex","alex1234"),(4,"alex","alex1234")
        #insert into table1 (id,username) values(5,"小弟"),(6,"大哥") #指定字段
    #删delete
        #delete from 表名 where 条件;
        #delete from table1 where id=5;
    #改update
        #update 表名 set 字段名 = 值 where id=2;
        #update table1 set password="123456" where id =6
    #查select
        #select * from 表名;