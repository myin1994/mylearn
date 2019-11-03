from socket import *
import json
class Myclient:
    def __init__(self):
        self.status = False
        self.s = socket()
        self.server_addr = (gethostbyname(gethostname()),7878)
        self.s.connect(self.server_addr)
        msg1 = """
                  1.登录
                  2.注册
                  3.退出
                  请选择操作序号（1|2|3）："""
        dict1 ={"1":"login",
                "2":"sign_up",
                "3":"exit"}
        while not self.status:
            choice = input(msg1).strip()
            try:
                func = getattr(self,dict1[choice])
                func()
            except KeyError:
                print("输入错误请重新输入！")
        msg2 = """
                  1.查看商品列表
                  2.操作购物车
                  3.结算
                  4.查看订单
                  5.退出
                  请选择操作序号（1|2|3|4|5）："""
        dict2 = {"1": "show_goods",
                 "2": "control_shopcar",
                 "3": "settle_account",
                 "4":"show_orders",
                 "5":"exit"}
        while self.status:
            choice2 = input(msg2).strip()
            try:
                func = getattr(self, dict2[choice2])
                func()
            except KeyError:
                print("输入错误请重新输入！")

    def login(self):

        self.s.send("login".encode())
        ack = self.s.recv(1).decode()
        while True:
            if ack == "1":
                print("开始登录")
                name = input("请输入用户名：")
                if name :
                    password = input("请输入密码：")
                    if password:
                        self.s.send(json.dumps([name,password],ensure_ascii=False).encode())
                    else:
                        print("密码不能为空，请重新输入")
                        continue
                else:
                    print("用户名不能为空，请重新输入")
                    continue
                result = self.s.recv(1024).decode()
                if result == "1":
                    print("登录成功！")
                    self.status = True
                    return
                else:
                    print("登录失败！请重新登录！")

    def sign_up(self):
        self.s.send("sign_up".encode())
        ack = self.s.recv(1).decode()
        while True:
            if ack == "1":
                print("开始登录")
                name = input("请输入用户名：")
                if name:
                    password = input("请输入密码：")
                    if password:
                        self.s.send(json.dumps([name, password], ensure_ascii=False).encode())
                    else:
                        print("密码不能为空，请重新输入")
                        continue
                else:
                    print("用户名不能为空，请重新输入")
                    continue
                result = self.s.recv(1024).decode()
                if result == "1":
                    print("注册成功！")
                    return
                elif "Duplicate" in result:
                    print("用户名重复！请重新注册！")
                else:
                    print("未知错误，请重新注册！")

            else:
                print("服务器未响应,请重试！")

    def show_goods(self):
        print("展示商品列表")
        self.s.send("show_goods".encode())
        ack = self.s.recv(1).decode()
        if ack == "1":
            recv_message = json.loads(self.s.recv(1024).decode())
            for i in recv_message:
                print(f"商品编号：{i[0]} 商品名称：{i[1]} 单价：{i[2]} 商品库存{i[3]}")

    def control_shopcar(self):
        print("操作购物车")
        self.s.send("control_shopcar".encode())
        ack = self.s.recv(1).decode()
        if ack == "1":
            while True:
                choice = input("请输入操作（查看：1|增加：2|减少：3|删除：4|返回上一页：5）：")
                def show():
                    self.s.send("1".encode())
                    print("当前购物车".center(10))
                    recv = self.s.recv(1024).decode()
                    if len(recv)==2:
                        print("当前购物车为空！")
                        return
                    recv_message = json.loads(recv)
                    goods_sum = 0
                    for i in recv_message:
                        goods_sum += i[4]*i[5]
                        print(f"商品id：{i[2]} 商品名称：{i[3]} 购买数量：{i[4]} 单价：{i[5]} 总价：{i[4]*i[5]}")
                    print(f"购物车总金额：{goods_sum}")
                def add():
                    while True:
                        self.s.send("2".encode())
                        goods_id = input("请输入要增加的商品id：")
                        if goods_id:
                            self.s.send(goods_id.encode())
                        else:
                            print("id不能为空，请重新输入")
                            continue
                        result = self.s.recv(1024).decode()
                        if result == "1":
                            print("操作成功！")
                            return
                        elif result == "0":
                            print("无该商品id，请重新填写！")
                        elif result == "-1":
                            print("该商品库存不足，请重新填写！")
                        else:
                            print("其他错误！")

                def reduce():
                    while True:
                        self.s.send("3".encode())
                        goods_id = input("请输入要减少的商品id：")
                        if goods_id:
                            self.s.send(goods_id.encode())
                        else:
                            print("id不能为空，请重新输入")
                            continue
                        result = self.s.recv(1024).decode()
                        if result == "1":
                            print("操作成功！")
                            return
                        elif result == "0":
                            print("无该商品id，请重新填写！")
                        elif result == "-1":
                            print("购物车中无该商品，请重新填写！")
                        else:
                            print("其他错误！")
                def drop():
                    while True:
                        self.s.send("4".encode())
                        goods_id = input("请输入要删除的商品id（全部）：")
                        if goods_id:
                            self.s.send(goods_id.encode())
                        else:
                            print("id不能为空，请重新输入")
                            continue
                        result = self.s.recv(1024).decode()
                        if result == "1":
                            print("操作成功！")
                            return
                        elif result == "0":
                            print("无该商品id，请重新填写！")
                        elif result == "-1":
                            print("购物车中无该商品，请重新填写！")
                        else:
                            print("其他错误！")
                dic = {"1":show,
                       "2":add,
                       "3":reduce,
                       "4":drop}
                if choice == "5":
                    self.s.send("5".encode())
                    return
                if choice in dic:
                    dic[choice]()
                else:
                    print("输入有误，请重新选择！")
    def settle_account(self):
        print("开始结算")
        self.s.send("settle_account".encode())
        ack = self.s.recv(1).decode()
        if ack == "1":
            result = self.s.recv(1024).decode()
            if result == "0":
                print("账户余额不足，请从购物车删减商品！")
            if result == "1":
                print("结算成功！")
    def show_orders(self):
        print("当前订单")
        self.s.send("show_orders".encode())
        ack = self.s.recv(1).decode()
        if ack == "1":
            recv_message = json.loads(self.s.recv(1024).decode())
            for i in recv_message:
                print(f"订单编号：{i[0]} 下单时间：{i[1]} 支付金额：{i[2]}元")

    def exit(self):
        print("退出")
        self.s.close()
        exit()

myclient = Myclient()
