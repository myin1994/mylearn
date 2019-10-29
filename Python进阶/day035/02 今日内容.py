# 数据的增删改查
#     增加insert
        # insert into 表名（字段们） values（值），（值）
        # insert into 表名（字段们） value（只能一行的值）
        #insrt into 表1（字段1,字段2）（select 字段1,字段2 from 表2） -字段一一对应,顺序不能颠倒
        # mysql> create table upd1(id int,name char(12));
        # mysql> create table upd2(sid int,sname char(12));
        # mysql> insert into upd1 values (1,"alex"),(2,"wusir"),(3,"hahaha");
        # mysql> insert into upd2(select * from upd1);
        #mysql> insert into upd3(id,name)(select * from upd2);

        #mysql> show variables like "%charac%";查看所有编码
#     删除delete（慎重-不可恢复-先查后删）
        #delete from 表名：清空表；
        #delete from 表名 where 条件；清除符合条件的数据
        #truncate table 表名；清空表并重置自增字段
#     修改update（不可逆）
        #update 表名 set 字段1=值1,字段2=值2, where 条件；
#     查询select
        #单表（今天）
        #select xxx from 表名 where 条件 group by 分组 having 聚合的过滤 order by排序 limit
        #多表


import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "xxxxx", "day35")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """insert into book values("学python从开始到放弃","alex","人民大学出版社",50,"2018-7-1"),
                                ("学mysql从开始到放弃","egon","机械工业出版社",60,"2018-6-3"),
                                ("学html从开始到放弃","alex","机械工业出版社",20,"2018-4-1"),
                                ("学css从开始到放弃","wusir","机械工业出版社",120,"2018-5-2"),
                                ("学js从开始到放弃","wusir","机械工业出版社",100,"2018-7-30")"""
try:
    cursor.execute(sql)  # 执行sql语句
    db.commit()  # 提交到数据库执行
except:
    db.rollback()  # 如果发生错误则回滚

# 关闭数据库连接
db.close()