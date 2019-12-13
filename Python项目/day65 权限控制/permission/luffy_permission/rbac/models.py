from django.db import models


class Permission(models.Model):
	"""权限表"""
	url = models.CharField('URL地址', max_length=108)
	title = models.CharField('标题', max_length=32)

	class Meta:
		verbose_name = '权限'
		verbose_name_plural = '所有权限'

	def __str__(self):
		return self.title


class Role(models.Model):
	"""角色表"""
	name = models.CharField('角色名称', max_length=32)
	permissions = models.ManyToManyField('Permission', verbose_name='角色所拥有的权限', blank=True)

	class Meta:
		verbose_name_plural = '所有角色'

	def __str__(self):
		return self.name


class User(models.Model):
	"""用户表"""
	name = models.CharField('用户名', max_length=32)
	pwd = models.CharField('密码', max_length=32)
	roles = models.ManyToManyField('Role', verbose_name='用户所拥有的角色', blank=True)

	class Meta:
		verbose_name_plural = '所有用户'

	def __str__(self):
		return self.name
