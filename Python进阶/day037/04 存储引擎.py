#myisam
# 只支持表级锁
# 修改某个数据时会把整张表锁住--表级锁

#memory

#innodb

# show engines;显示所有引擎信息
# Supports transactions, row-level locking, and foreign keys
# 支持事务 ，行级锁，表级锁，外键（只有innodb）

# 事务
# select balance from t where name = "name"
# update t set balance where name="name"

# 意外未成功
# update t set balance=balance-200 where name = "name"
# update t set balance=balance+200 where name = "name2"

# 开启事务 begin/start transactions
# update t set balance=balance-200 where name = "name"
# update t set balance=balance+200 where name = "name2"
# 提交事务commit（若超时未提交则回滚至开启事务之前）

# 事务四大特点
# 持久性，一致性，原子性，隔离性


# 行级锁---修改数据时，将整行数据锁住（修改大量数据时用表锁较合适）
# 表级锁


# 事务和锁
# 参考线程锁，
# begin;
# select id from s2 where name="alex" for update;
# commit;