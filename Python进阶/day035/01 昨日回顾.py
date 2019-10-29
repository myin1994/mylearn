# 基础数据类型
    #数字类型：tinyint int float(7,2) decimal
    # 时间类型：datetime date time
    #字符串类型：char定长浪费空间存取快，varchar变长节省空间存取慢

#约束
    #unsigned
    #not null
    #default
    #unique 联合唯一
    #primary key 联合主键
    #auto_increment（依赖unique）
    #foreign key（依赖关联字段unique） on update cascade on delete cascade

# 表与表之间的关系
    #多对一/一对多
    #一对一
    #多对多

# 创建表
    #create table 表名(字段名 类型(长度) 约束1 约束2,字段2……)

# 删除表
    #drop table 表名;

#修改表
    #alter table 表名add/drop/modify/change/rename/

# 查看表结构
    #desc 表名;
    #show create table 表名;