from wxpy import *
from pyecharts.charts import Pie
import webbrowser

bot = Bot()
friends=bot.friends()    #拿到所有朋友对象
attr=['男朋友','女朋友','性别不详']
value=[0,0,0]
for friend in friends:
    if friend.sex == 1: # 等于1代表男性
        value[0]+=1
    elif friend.sex == 2: #等于2代表女性
        value[1]+=1
    else:
        value[2]+=1

pie = Pie()
pie.add("", attr, value, is_label_show=True)
pie.render('sex.html')#生成html页面
# 打开浏览器
webbrowser.open("sex.html")