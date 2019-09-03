# 预科day02

## 今日内容概要

1.码云

2.git

## 昨日内容回顾

+ 计算机组成结构
  + cpu
  + 硬盘
  + 内存
  + 输入输出设备
+ 编程语言介绍
  + 解释型：逐行解释执行（同声翻译）-先有
  + 编译型：一次性编译-最后执行
+ Python安装
+ Pycharm安装
+ 环境变量
+ 硬件之间的协作依赖操作系统
+ 输入a在计算机内部的过程
+ 利用pycharm建立py文件

## 今日内容

1.版本控制工具

+ 码云：gitee.com

+ 下载安装git（除路径全部默认即可 ）

  + 先在码云建立仓库

  + 对应文件夹空白处右键git bash here（修改隐藏文件夹选项）

  + cd 文件名-打开文件夹路径

  + ```Git
    
    Git 全局设置:
    git init
    git config --global user.name "mayangin"
    git config --global user.email "244797519@qq.com"
    
    ```

  + ```Git
    创建 git 仓库:
    git add . #匹配当前仓库所有增删改内容
    git commit -m "first commit" #确认修改内容及设置标签
    git remote add origin https://gitee.com/oldboy-python-full-stack-26/190830260002.git #设置仓库路径及输入账号密码（同一文件夹下一次即可）
    git push -u origin master #推送至远程仓库（首次新建）
    git push origin master #重复推送时使用
    ```

    - 输入账号密码错误后修改：

      - win10 系统下进入
        控制面板 》 用户帐户 》 管理你的凭据
        选择 [Windows 凭据]

        git 保存的用户信息在普通凭据列表里》编辑>>>完成

  + 冲突1：远程仓库与原始文件不统一（删除了远程仓库中文件）

    + git pull origin master  #远程同步到本地再重新提交（i进入插入模式；esc进入命令行模式“:wq”退出）
  + git push -f origin master 强制推送
  
+ 冲突2：重建文件夹后冲突
  
  + git pull origin master  --allow-unrelated-histories #将远程同步后重新提交
  
+ 冲突总结：根源上还是看远程仓库与本地仓库的差异性
  
    + 当远程仓库保持完整性时，对本地仓库的增删改可顺利同步至远程
    + 当本地仓库保持完整性时，远程仓库变化后，需要对本地更新后才能继续更新本地内容至远程仓库
    + 实际上直接整个复制远程仓库的内容再对本地进行修改，再重新同步也可正常进行
  + 可修改文件夹路径，只要.git隐藏文件未修改即可
  
+ 其它基本操作
  
    + git clone #克隆仓库至本地
    
    + touch filename 新建文件
    
    + ls 显示当前所有文件
    
    + git status -s 显示当前状态（不加-s会显示更详细的内容）
    
    + vim filename 编辑文件
    
    + 码云平台和github平台上传同一仓库
    
      + ```Git
        
        - git remote add github https://github.com/gongqingfeng/Drcom.git
        - git push github master
        
        ```
    
        















