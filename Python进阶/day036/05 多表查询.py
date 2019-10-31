# 笛卡尔积--连表基础（较快）
# 1 xx  a yy
# 2 xx  b yy
# 3 xx
# (1,a)
# (1,b)
# (2,a)
# (2,b)
# (3,a)
# (3,b)
# select * from employee,department;联合查询

# 内连接:表1和表2中不符合条件的数据都会被丢弃
# select * from employee,department where dep_id = department.id;重名通过表名.
# select * from employee inner join department on dep_id = department.id;重名通过表名.

# 外连接
#     左外连接  left join
        # select * from employee left join department on dep_id = department.id;重名通过表名.
#     右外连接  right join
        # select * from employee right join department on dep_id = department.id;重名通过表名.
#     全外连接  full join（mysql中没有）
        # select * from employee left join department on dep_id = department.id;重名通过表名.
        # union
        # select * from employee right join department on dep_id = department.id;重名通过表名.


# 子查询 一个select语句中总是出现另一个select语句
    #多个值 in
    #一个值 = > <

# 查看技术部员工姓名
# select * from employee e inner join department d on dep_id=d.id and d.name="技术部"
# 查看不足1人的部门名(子查询得到的是有人的部门id)
# select dep_id from employee group by dep_id;

# select * from employee
# select avg(age) from employee;
# select name,age from employee where age>(select avg(age) from employee);

#查询大于部门内平均年龄的员工名、年龄
# select avg(age) from employee group by dep_id;
# select e.name,e.age from employee e,(select dep_id,avg(age) as av from employee group by dep_id) as av1 where av1.dep_id=e.dep_id and age > av1.av;

# select dep_id,avg(age) from employee group by dep_id;
# select * from employee e inner join (select dep_id,avg(age) as av from employee group by dep_id) as tmp on tmp.dep_id=e.dep_id where age>av;

# 备注：如果查出来的一张表需要连表，那么被查出来的表必须定义一个名字
# 如果查出的一张表中，显示字段引入了函数，那么这个字段必须重命名，才能在后续的查询中使用


# mysqldump -uroot -pxxxxx database>path 导出.sql

# 导入 create database day36_bak;
    #source path