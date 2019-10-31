import time
# 在循环体中套入qtmd即可实现进度条，如进行爬虫时


# tqdm(list)方法可以传入任意一种list,比如数组
# from tqdm import tqdm
# for i in tqdm(range(1000)):
#     time.sleep(1)
#     pass

# from tqdm import tqdm
# for char in tqdm(["a", "b", "c", "d"]):
#     #do something
#     time.sleep(1)
#     pass

# trange(i) 是 tqdm(range(i)) 的简单写法
# from tqdm import trange
# for i in trange(100):
#     #do something
#     time.sleep(1)
#     pass

# 在for循环外部初始化tqdm,可以打印其他信息
from tqdm import tqdm
import time
bar = tqdm(["a", "b", "c", "d"])
for char in bar:
    time.sleep(1)
    bar.set_description(f"进度条 {char}")

