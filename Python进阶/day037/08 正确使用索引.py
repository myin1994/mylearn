# 1.对哪个字段创建了索引，条件就使用那个字段
# 2.条件列不能参与计算，条件列不能调用函数
# 3.如果列中重复值多，那么不适合创建索引（性别）（重复率超过10%）
# 4.尽量不使用范围查询，范围越小效率越高
    # limit初始值越大越慢，使用between and代替
# 5.使用like "a%" 效率高于 like "%a"

# 6.and 相连的多个条件，如果有一个索引，都可以被命中
    #select * from s1 where id =1000000 and name = "eva";
    #select count(*) from s1 where id =1000000 or name = "eva";

# 7.or 相连的多个条件，都有索引，才可以被命中

# 8.联合索引和最左侧前缀原则
# create index mix_ind on s1(id,name,email);
# 相等时
# 条件带有联合索引最左侧字段时可以命中索引
# 条件不带有联合索引最左侧字段时不可以命中索引

# 从使用了范围的那个字段之后的所有条件都无法命中索引
# select * from s1 where id >1000000 and email ="eva2000000@oldboy";
# select * from s1 where id =1000000 and email like "%@oldboy";
# 使用or根本命中不了联合索引

# 9.primary key /unique key /index key都是索引

# 执行计划（分析器中）
# explain
# explain  select * from s1 where id =1000000 and email like "%@oldboy";

# 索引合并
# 创建的两个索引原本是独立的，在特殊的情况下临时合并成一个使用（union）
# explain  select * from s1 where id =1000000 or email like "%@oldboy";
# 覆盖索引
# using index将索引当做条件，并使用这个索引进行计算
# select count(*) from s1 where id >10000;