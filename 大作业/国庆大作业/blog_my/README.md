程序名称：模拟博客园系统

程序流程：

```
1.定义不同的功能选项显示给用户让用户选择要执行的功能
2.将功能和显示给用户的序号进行数据关联
3.判断用户选择的功能,是否是我们定义的功能,如果是就执行此功能
4.在执行用户选择的功能前,先判断是否登录成功.如果登录成功就执行用户选择的功能
5.没有登录成功就先执行登录,登录成功后在执行用户选择的功能
6.注册时对密码进行加密，且对用户名和密码有限制
7.登录时连续3次错误会退出程序
8.用户登录后可写评论及日记
```

程序功能：

│  README.md
│  treefile.txt
│  
├─bin
│      start.py    `程序运行界面`
│      
├─conf
│  │  setting.py   `文件路径设置`
│  │  
│  └─__pycache__
│          setting.cpython-36.pyc
│          
├─core
│  │  src.py  `主要逻辑`
│  │  
│  └─__pycache__
│          src.cpython-36.pyc
│          
├─db
│  │  usercomment.txt   `用户名评论信息`
│  │  userinfo.txt  `用户名及密码`
│  │  
│  └─userdiary  `用户日记 `
│          mayang.txt
│          
├─lib
│  │  common.py  `公共模块（包含装饰器及登录函数）`
│  │  
│  └─__pycache__
│          common.cpython-36.pyc
│          
└─log