1. 创建表

```
rbac组件中的user表
class UserInfo(models.Model):

    # username = models.CharField(max_length=32)
    # password = models.CharField(max_length=32)

    roles = models.ManyToManyField(Role)

    # def __str__(self):
    #     return self.username

    class Meta:
        abstract = True  #不让这个类去生成数据库中的表


crm项目中的userinfo表继承一下rbac中的userinfo表
class Userinfo(UserInfo):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    telephone = models.CharField(max_length=11,db_index=True) #db_index普通索引
    # roles = models.ManyToManyField(Role类空间)
    email = models.EmailField()  # form.CharField(validator=['@']) xx@xx
    is_active = models.BooleanField(default=True) #0--False  1--True

    def __str__(self):
        return self.username
```

2 路由分发

```
项目的urls.py文件中写入以下内容
url(r'^rbac/', include('rbac.urls',namespace='rbac')),
```

别忘了将html文件中使用的母版,改成crm中的母版

母版中需要引入一下我们rbac组件中的css文件和js文件

3 将所有权限数据批量添加到数据库中

```
#批量操作权限,访问这个路径
    url(r'^multi/permissions/$', views.multi_permissions, name='multi_permissions'),
别忘了添加权限的title名称
```

4 添加一级菜单

5 给权限分配一级菜单,然后再分配二级菜单(批量操作权限这里做)

6 权限分配(别忘了在母版中预留css的block块)

7 登录后权限注入,使用rbac中的server文件夹中的permission_insert.py文件中的那个函数

8 权限校验(中间件中使用咱们的rbac中间件,rbac中的mytags如果和项目中的mytags重名,别忘了修改名称,不然一直使用的注册app的最后一个app中的mytags)

settings配置

```
ROOT_URLCONF = 'NBCrm.urls'
PERMISSION_KEY = 'permission_list'
MENU_KEY = 'menu_dict'

```

9 生成左侧菜单(inclusion_tag)  别忘了左侧菜单的样式,要使用人家系统中的

```
@register.inclusion_tag('rbac/menu.html')
def menu(request):
    current_path = request.path
    menu_dict = request.session.get(settings.MENU_KEY)
    for menu_k,menu_v in menu_dict.items():
        menu_v['class'] = 'hidden'
        for path in menu_v['children']:
            path['class'] = ''  #除了和当前路径能匹配的请求路径对应的那个二级菜单加上active以外,其他的二级菜单都不加这个active类值
            # if path['url'] == current_path:
            if request.pid == path['id']:
                menu_v['class'] = ''
                path['class'] = 'active'
                
```

10 面包屑 路径导航,首页的时候,在rbac中间件中添加面包屑数据的时候,如果访问的是首页,就不需要在我们的数据中再添加一次首页路径了

```
else:
    if permission['permissions__url'] != reverse('home'):
        这里加上了home路径的判断
        bread_crumb.append({
        'title':permission['permissions__title'],
        'url':permission['permissions__url'],
        })
    request.pid = permission['permissions__id']

request.session['bread_crumb'] = bread_crumb
return
```

11 精确到按钮级别的权限

12 menu_list菜单展示时,权限展示部分的调整

```
permissions_dict = {}
    for permission in permissions_list:
        mid = permission.get('menu_id')
        if mid:
            permissions_dict[permission['id']] = permission
            permissions_dict[permission['id']]['children'] = []

    print(permissions_dict)
    for node in permissions_list:
        pid = node.get('parent_id')
        if pid:
            permissions_dict[pid]['children'].append(node)
```



