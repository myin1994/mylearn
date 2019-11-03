"""
创建用户表：
create table user(user_id int primary key auto_increment,
                   user_name varchar(20) unique,#用户名长度限制
                   password char(32) not null);

创建用户详细信息表：
create table user_detail(user_id int unique,
                        role enum("0","1") default "0",#默认为0普通用户
                        acc_balance int unsigned default 100
                        );

创建订单表：
create table orders(order_id int primary key auto_increment,
                    order_time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    payment float(13,3) unsigned,
                    uid int);

创建商品表：
create table goods(goods_id int primary key auto_increment,
                   gname varchar(30) unique,
                   price float(10,3) unsigned,
                   g_num int unsigned);
insert into goods(gname,price,g_num) values("商品1",5,0);
insert into goods(gname,price,g_num) values("商品2",10,1);
insert into goods(gname,price,g_num) values("商品3",20,10);
insert into goods(gname,price,g_num) values("商品4",30,10);
insert into goods(gname,price,g_num) values("商品5",40,10);
创建商品订单表：
create table goods_orders(id int primary key auto_increment,
                          g_id int not null,
                          o_id int not null,
                          buy_num int unsigned);

创建购物车表：
create table shop_car(id int unsigned,
                     user_name varchar(20),
                     goods_id int,
                      gname varchar(30),
                      buy_num int unsigned,
                      price float(10,3) unsigned);

insert into shop_car values (28,"999",1,"商品1",2,18);
"""

from socketserver import *
import pymysql
import json

class Mysever(BaseRequestHandler):
    def handle(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="77963333", database="shopping")
        self.cur = self.conn.cursor()
        self.user = None
        self.user_id = None
        while True:
            try:
                choice = self.request.recv(20).decode()
                if hasattr(self,choice):
                    func = getattr(self,choice)
                    self.request.send("1".encode())
                    func()
                else:
                    self.request.send("0".encode())
            except:
                continue

    def login(self):
        username, password = json.loads(self.request.recv(1024).decode())
        sql = "select * from user where user_name = %s and password =%s"
        try:
            ret = self.cur.execute(sql, (username, password))
            if ret:
                self.conn.commit()
                self.request.send("1".encode())
                self.user = username
                self.user_id = self.cur.fetchall()[0][0]
                return
            else:
                self.request.send("0".encode())
                return
        except Exception as e:
            self.request.send("0".encode())
            print(e)
            return

    def sign_up(self):
        username, password = json.loads(self.request.recv(1024).decode())
        sql1 = "insert into user(user_name,password) values (%s,%s)"
        try:
            ret = self.cur.execute(sql1,(username, password))
            if ret:
                self.conn.commit()
                sql2 = "insert into user_detail(user_id) (select user_id from user where user_name=%s)"
                ret2 = self.cur.execute(sql2,(username))
                self.conn.commit()
                self.request.send("1".encode())
                return
            else:
                self.request.send("0".encode())
                return
        except Exception as e:
            self.request.send(e.args[1].encode())
            return
    def show_goods(self):
        sql = "select * from goods"
        self.cur.execute(sql)
        goods_list = list(self.cur.fetchall())
        goods_message = json.dumps(goods_list,ensure_ascii=False)
        self.request.send(goods_message.encode())

    def control_shopcar(self):
        def show():
            sql = "select * from shop_car where user_name = %s order by goods_id"
            self.cur.execute(sql, (self.user))
            goods_list = list(self.cur.fetchall())
            goods_message = json.dumps(goods_list, ensure_ascii=False)
            self.request.send(goods_message.encode())

        def add():
            goods_id = self.request.recv(1024).decode()
            sql1 = "update shop_car set buy_num=buy_num+1 where user_name=%s and goods_id=%s"
            sql2 = "select * from goods where goods_id=%s"
            sql3 = "select * from shop_car where user_name=%s and goods_id=%s"
            try:
                ret1 = self.cur.execute(sql2, (goods_id))
                if ret1:
                    goods_id, gname, gprice, g_num = self.cur.fetchall()[0]
                    if g_num > 0:
                        ret2 = self.cur.execute(sql3, (self.user, goods_id))
                        if ret2 == 1:
                            self.cur.execute(sql1, (self.user, goods_id))
                        else:
                            sql1_1 = "insert into shop_car values (%s,%s,%s,%s,1,%s)"
                            self.cur.execute(sql1_1, (self.user_id,self.user, goods_id,gname,gprice))
                        self.conn.commit()
                        self.request.send("1".encode())
                    else:
                        self.request.send("-1".encode())
                        return
                else:
                    self.request.send("0".encode())
                    return
            except Exception as e:
                self.request.send("0".encode())
                print(e)
                return

        def reduce():
            goods_id = self.request.recv(1024).decode()
            sql1 = "update shop_car set buy_num=buy_num-1 where user_name=%s and goods_id=%s"
            sql2 = "select * from goods where goods_id=%s"
            sql3 = "select buy_num from shop_car where user_name=%s and goods_id=%s"
            try:
                ret1 = self.cur.execute(sql2, (goods_id))
                if ret1:
                    goods_id, gname, gprice, g_num = self.cur.fetchall()[0]
                    ret2 = self.cur.execute(sql3, (self.user, goods_id))
                    if ret2 == 1:
                        buy_num = self.cur.fetchall()[0][0]
                        if buy_num > 1:
                            self.cur.execute(sql1, (self.user, goods_id))
                        else:
                            sql1_1 = "delete from shop_car where user_name=%s and goods_id=%s"
                            self.cur.execute(sql1_1, (self.user, goods_id))
                        self.conn.commit()
                        self.request.send("1".encode())
                    else:
                        self.request.send("-1".encode())
                        return
                else:
                    self.request.send("0".encode())
                    return
            except Exception as e:
                self.request.send("0".encode())
                print(e)
                return

        def drop():
            goods_id = self.request.recv(1024).decode()
            sql1 = "delete from shop_car where user_name=%s and goods_id=%s"
            sql2 = "select * from goods where goods_id=%s"
            sql3 = "select buy_num from shop_car where user_name=%s and goods_id=%s"
            try:
                ret1 = self.cur.execute(sql2, (goods_id))
                if ret1:
                    goods_id, gname, gprice, g_num = self.cur.fetchall()[0]
                    ret2 = self.cur.execute(sql3, (self.user, goods_id))
                    if ret2 == 1:
                        self.cur.execute(sql1, (self.user, goods_id))
                        self.conn.commit()
                        self.request.send("1".encode())
                    else:
                        self.request.send("-1".encode())
                        return
                else:
                    self.request.send("0".encode())
                    return
            except Exception as e:
                self.request.send("0".encode())
                print(e)
                return


        dic = {"1": show,
               "2": add,
               "3": reduce,
               "4": drop}
        while True:
            choice = self.request.recv(1024).decode()
            if choice in dic:
                dic[choice]()
            else:
                return
    def settle_account(self):
        # 先判断能否结算，能结算的结算，不能结算的暂时保留在购物车
        #获取库存大于0的支付总金额与账户余额
        try:
            sql1 = " select sum(buy_num*g.price) from goods g,shop_car s where g.goods_id=s.goods_id and g_num>=buy_num"
            self.cur.execute(sql1)
            payment = self.cur.fetchall()[0][0]
            sql1_1 ="select acc_balance from user_detail where user_id=%s"
            self.cur.execute(sql1_1,(self.user_id,))
            acc_balance = self.cur.fetchall()[0][0]
            if payment <= acc_balance:
                #更新订单表及用户余额
                sql2 = "insert into orders(payment,uid) values(%s,%s)"
                self.cur.execute(sql2,(payment,self.user_id))
                sql3 = "update user_detail set acc_balance=acc_balance-%s where user_id=%s"
                self.cur.execute(sql3, (payment, self.user_id))
                #更新商品表及购物车
                #获取可结算的goods_id及新的库存
                sql2_1 = "select g_num-buy_num,g.goods_id,buy_num from goods g,shop_car s where g.goods_id=s.goods_id and g_num>=buy_num"
                self.cur.execute(sql2_1)
                new_goods = self.cur.fetchall()
                for i in new_goods:
                    sql2_2 = "update goods set g_num=%s where goods_id=%s"
                    self.cur.execute(sql2_2,(i[0],i[1]))
                    sql2_3 = "delete from shop_car where id=%s and goods_id=%s"
                    self.cur.execute(sql2_3, (self.user_id,i[1]))
                self.conn.commit()
                #更新商品_订单表
                sql4 = "select order_id from orders where uid=%s order by order_time desc limit 1"
                self.cur.execute(sql4,(self.user_id))
                order_id = self.cur.fetchall()[0][0]
                for i in new_goods:
                    sql4_1 = "insert into goods_orders(g_id,o_id,buy_num) values(%s,%s,%s)"
                    self.cur.execute(sql4_1,(i[1],order_id,i[2]))
                self.conn.commit()
                self.request.send("1".encode())
            else:
                self.request.send("0".encode())
        except Exception as e:
            print(e)

    def show_orders(self):
        sql = "select * from orders where uid=%s"
        self.cur.execute(sql,(self.user_id))
        orders_list = list(self.cur.fetchall())
        print(orders_list)
        orders_message = json.dumps(orders_list, ensure_ascii=False)
        self.request.send(orders_message.encode())
        self.request.send(orders_message.encode())




















TCPServer.allow_reuse_address = True # 允许地址（端口）重用
server = ThreadingTCPServer(("",7878),Mysever)
server.serve_forever()