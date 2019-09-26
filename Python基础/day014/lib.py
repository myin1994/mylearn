print("这是一个公共的工具箱-其他文件中")
def login():
    print("登录")

def register():
    print("注册")

a = 5

print(2222,"主函数之前内容")
print(repr(__name__))
if __name__ == "__main__":
    """
    自己使用的功能，测试用
    """
    login()
    print(111111)