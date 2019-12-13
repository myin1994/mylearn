from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import HttpResponse, redirect
from django.conf import settings
import re


class RbacMiddleWare(MiddlewareMixin):

	def process_request(self, request):
		# 获取当前访问的URL地址
		url = request.path_info

		# 白名单
		for i in settings.WHITE_LIST:
			if re.match(i,url):
				return

		# 校验登录状态
		is_login = request.session.get('is_login')
		if is_login != '1':
			# 没有登录 跳转到登录页面
			return redirect(reverse('login'))

		# 判断免认证的地址
		for i in settings.NO_PERMISSION_LIST:
			if re.match(i,url):
				return

		# 获取权限信息
		permission = request.session.get('permission')
		# 权限的校验
		for i in permission:
			if re.match(r'^{}$'.format(i['permissions__url']),url):
				return

		return HttpResponse('没有访问权限 请联系管理员')
