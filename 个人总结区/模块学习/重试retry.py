# retry
# 正如它的名字，retry是用来实现重试的。很多时候我们都需要重试功能，比如写爬虫的时候，有时候就会出现网络问题导致爬取失败，然后就需要重试了，一般我是这样写的（每隔两秒重试一次，共5次）：

# import time
# def do_something():
#   xxx
#
# for i in range(5):
#   try:
#     do_something()
#     break
#   except:
#     time.sleep(2)
# 这样未免有些累赘。有了retry后，只需要。


# from retry import retry
# import time
#
# @retry(tries=5, delay=2)
# def do_something():
#     print(1)
#
# do_something()
#
# time.sleep(10)
# 也就是在函数的定义前，加一句@retry就行了。

import random
from retry import retry

@retry(tries=5, delay=2)
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


print(do_something_unreliable())
