# 创建索引
# create index 索引名 on 表名（字段名）
    # mysql> create index ind_id on s1(id);


# 索引的优点：加速查询效率
# 索引的缺点：拖慢写的速度（减少写的频率,删除索引），占用更多的硬盘空间



# 删除索然
# drop index 索引名 on 表名;
    # drop index ind_id on s1;
