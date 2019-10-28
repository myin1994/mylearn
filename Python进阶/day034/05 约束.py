
# unsigned

# 非空约束  not null
# create table user(username char(18) not null,password char(32) not null,age tinyint unsigined)
# 设置严格模式：
#     不支持对not null字段插入null值
#     不支持对自增长字段插入”值
#     不支持text字段有默认值
#
# 直接在mysql中生效(重启失效):
# mysql>set sql_mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION";
#
# 配置文件添加(永久失效)：
# sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"


#设置默认值 default
# create table user2(username char(18) not null",password char(32) not null,age tinyint unsigned default 18)


# 唯一约束  unique
# create table user3(username char(18) unique,password char(32) not null,age tinyint unsigned default 18)


# 非空唯一(仅有时自动变为主键)
# create table user4(username char(18) not null unique not null,password char(32) not null,age tinyint unsigned default 18)


# primary key 主键
    #一张表只能有一个主键
    #主键约束了一个字段的非空唯一

# auto_increment 自增(自带not null约束)
# create table user5(id int unique auto_increment,username char(20));

# 重要的难点
# 外键约束（关联主键建议）
# foreign key
# create table stu(
#     sid int,
#     sname char(18),
#     gender enum("male","female"),
#     classid int,
#     foreign key(classid) references class(cid)
# );
#
# # 需要先建立外键表
# create table class(
#     cid int unique,
#     cname char(18)
# );


# 级联更新 on update cascade---关联表同步修改
# 级联删除on delete cascade
# foreign key
# create table stu1(
#     sid int,
#     sname char(18),
#     gender enum("male","female"),
#     classid int,
#     foreign key(classid) references class(cid) on update cascade
# );

# create table class1(
#     cid int unique,
#     cname char(18)
# );


# 联合唯一
# create table person(
#     id int,
#     familyname char(10),
#     firstname char(10),
#     unique(familyname,firstname)
# );

# 联合主键
# create table person(
#     id int,
#     familyname char(10),
#     firstname char(10),
#     primary key(familyname,firstname)
# );