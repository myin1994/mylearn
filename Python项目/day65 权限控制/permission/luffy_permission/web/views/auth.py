from django.shortcuts import HttpResponse, render, redirect, reverse
from rbac import models


def login(request):
	if request.method == 'POST':
		# 获取用户名和密码
		username = request.POST.get('username')
		password = request.POST.get('password')
		# 在数据库筛选用户名和密码
		user = models.User.objects.filter(name=username, pwd=password).first()
		if not user:
			# 认证失败   返回错误提示
			return render(request, 'login.html', {'error': '用户名或密码错误'})

		# 认证成功   保存登录状态 权限的信息
		# 获取权限信息
		# 去除权限为空的权限  去重
		permission = user.roles.filter(permissions__url__isnull=False).values('permissions__url').distinct()
		# 保存权限信息到session中
		request.session['permission'] = list(permission)
		request.session['is_login'] = '1'

		# 重定向到首页
		return redirect('index')

	return render(request, 'login.html')


def index(request):
	return render(request, 'index.html')
