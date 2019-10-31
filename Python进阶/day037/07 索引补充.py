# 1）创建表时，不能在同一个字段上建立两个索引(主键默认建立唯一索引)，在需要经常查询的字段上建立索引(如：deal_id已经是主键，不能再次执行：create index tmp_table_index on tmp_table(deal_id),会报错);
#                 a) 主键：该字段没有重复值，且不允许为空
#                  惟一索引：该字段没有重复值，但允许空值(该字段可以有多个null值)
#                  一张table只允许一个主键，但可以创建多个unique index
#                 比如，表中有5行，ID的值是   1   2   3   4   5，就可以作为主键
#                 但如果ID的值是   1   2   3   4   NULL  NULL，则可以建立惟一索引，不能作为主键
#                 可以为多个字段建立唯一索引：
#                create unique index unique_index01 on search_result_tmp(deal_id,compare_flag);
#                建立唯一索引以后，只允许插入一条如下记录,插入两条时会违反unique index约束
#                 Insert into search_result_temp values(1,null);
#   （2）删除索引：drop index unique_index01；
#   （3）函数索引
# 　　如果在我们的查询条件使用了函数，那么索引就不可用了。
# 　　可以用建立函数索引的方式，来解决这个问题
# 　　例如:
# 　　      select * from product where nvl(price,0.0)>1000.0 ;
# 　　这里，nvl(price,0.0)使用了函数，索引不能利用price字段上做的索引了
# 　　ok,我们来创建函数索引
# 　　create index index_price on product(nvl(price,0.0));
# （4）其他：
#         唯一索引能极大的提高查询速度，而且还有唯一约束的作用
# 　　一般索引，只能提高30%左右的速度
# 　　经常插入，修改，应在查询允许的情况下，尽量减少索引，因为添加索引，插入，修改等操作，需要更多的时间
#
#
# 1. 主键一定是唯一性索引，唯一性索引并不一定就是主键。 
#
# 2. 一个表中可以有多个唯一性索引，但只能有一个主键。
#  
# 3. 主键列不允许空值，而唯一性索引列允许空值。 
#
# 4. 索引可以提高查询的速度。 
#
# 主键和索引都是键，不过主键是逻辑键，索引是物理键，意思就是主键不实际存在，而索引实际存在在数据库中
