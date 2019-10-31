# 多表查询
    #连表查
        #内
        #左外
        #内外
        #全
    #子查询

# pymqsl
    #获取连接conn = pymsql.Connect(连接参数)
    #获取游标conn.sursor()
    #执行sql
        #读（select） fetchone fetchmany(n) fetchall
        #写（insert delete update） conn.commit
    #关闭游标和连接 cur.close conn.close


# 存储引擎
    #myisam:三个文件存储 （表结构，数据，索引） 5.5及之前的默认存储引擎
    #innodb: 两个文件存储（表结构，数据索引） 5.6之后的默认存储引擎
    #memory：只有表结构存储在硬盘上，其他都在内存里，sever断电消失