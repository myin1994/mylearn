from django.conf.urls import url
from rbac.views import *

urlpatterns = [
    #角色页面
    url(r'^role/list/$', RoleList.as_view(),name='role_list'),
    url(r'^role/add/$', AddOrEdit.as_view(),name='role_add'),
    url(r'^role/edit/(\d+)/$', AddOrEdit.as_view(),name='role_edit'),
    url(r'^role/del/$',  RoleList.as_view(),name='role_del'),
    #菜单页面
    url(r'^menu/list/$', MenuList.as_view(),name='menu_list'),
    url(r'^menu/add/$', AddOrEdit.as_view(),name='menu_add'),
    url(r'^menu/edit/(\d+)/$', AddOrEdit.as_view(),name='menu_edit'),
    url(r'^menu/del/$', MenuList.as_view(),name='menu_del'),

    #权限编辑
    url(r'^access/add/$', AddOrEdit.as_view(),name='access_add'),
    url(r'^access/edit/(\d+)/$', AddOrEdit.as_view(),name='access_edit'),
    url(r'^access/del/$', MenuList.as_view(),name='access_del'),
    #批量编辑权限
    url(r'^access/list/$', AccessList.as_view(),name='access_list'),

    #权限分发
    url(r'^access/distribute/$', AccessDistribute.as_view(),name='access_distribute'),
    #测试用
    # url(r'^test/$', test,name='test'),

]
