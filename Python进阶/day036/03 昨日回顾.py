# 单表查询语句
# select distinct 字段名  #可以使用函数，四则运算（不建议），重命名
# from 表名 as e          #查询时临时修改表名
# where 条件              #条件可以用比较运算，逻辑运算，like，in，regexp
# group by 分组           #根据某个字段一致的项进行分组，为了分组统计
# having 过滤             #可以使用聚合函数，在分组之后对组数据进行筛选
# order by 字段排序        #默认升序asc，desc表示降序
# limit m,n               #从m+1开始取n条，默认m为0

# update 表set 字段=值 where order by limit
# update 表set 字段=值，字段=值 where order by limit

# delete from 表 where order by limit