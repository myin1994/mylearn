1.git init 初始化

2.git config --global user.name "username"
	git config --global user.email "useremail" 配置

3.git add . 匹配增删改内容

4.git commit -m "message"

5.git remote add origin/github xxx.git 配置仓库路径

6.git pull/push origin/github master 拉/推远程仓库

7.git push -f origin master 强制推送

8.git pull origin master  --allow-unrelated-histories 将远程同步后重新提交

9.git clone 克隆远程仓库

10.①git fetch git://repo.or.cz/tomato.git 支持断点克隆远程仓库

​	 ②git checkout FETCH_HEAD 完成后的下一步

11.ls 显示当前所有文件

12.touch filename 新建文件

13.git status -s 显示当前状态（不加-s会显示更详细的内容）

14.vim filename 编辑文件（:wq退出）