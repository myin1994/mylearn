1.git init 初始化

2.git config --global user.name "username"
	git config --global user.email "useremail" 配置

3.git add . 匹配增删改内容

4.git commit -m "message"

5.git remote add origin/github xxx.git 配置仓库路径

6.git pull/push origin/github master 拉/推远程仓库

7.git push -f origin master 强制推送（慎用！慎用！）

8.git pull origin master  --allow-unrelated-histories 将远程同步后重新提交

9.git clone 克隆远程仓库

10.①git fetch git://repo.or.cz/tomato.git 支持断点克隆远程仓库

​	 ②git checkout FETCH_HEAD 完成后的下一步

11.ls 显示当前所有文件

12.touch filename 新建文件

13.git status -s 显示当前状态（不加-s会显示更详细的内容）

14.vim filename 编辑文件（:wq退出）

15：git remote remove origin/github xxx.git 删除仓库路径

16.问题处理

```
ahead of 'origin/master' by N commits.怎么处理？

每次都采用 git pull origin master会让本地节点一直指向远端 origin/master (指向不更新），所以当从远端获取到新的commit后，这个commit相对于本地节点的指向（远端的旧commit）就会提示“超前”。
解决方法：

直接使用git fetch命令修复现在的问题，让本地指向远端最新节点
后续更新使用 git pull, 不要带 origin master
```

