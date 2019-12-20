+ 将组建复制至新项目并在项目settings中进行配置

+ 创建表

  + 项目原始用户表继承rbac组件中的UserInfo表

    ```python
    from rbac.models import UserInfo as Userinfo
    
    class UserInfo(Userinfo):
        username = CharField(max_length=16, blank=False, unique=True)
        password = CharField(max_length=32, blank=False)
        telephone = CharField(max_length=20, blank=False)
        email = EmailField(max_length=50, blank=False)
        is_active = BooleanField(default=True)
    
        def __str__(self):
            return self.username
    ```

  + rbac组件中的用户表仅保留角色映射字段（同时注销admin中对应类）

    ```python
    class Role(Model):
        """
        角色表，与权限多对多
        """
        role_name = CharField(max_length=32,verbose_name='角色')
        permissions = ManyToManyField('Permission')
        def __str__(self):
            return self.role_name
    
    class UserInfo(Model):
        """
        用户表，与角色多对多
        """
        # username = CharField(max_length=32)
        # password = CharField(max_length=32)
        roles = ManyToManyField(Role)
        # def __str__(self):
        #     return self.username
    
        class Meta:
            abstract = True #不让这个类去生成数据库中的表
    ```

  + 执行数据库迁移指令

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

+ 路由分发

  ```
  项目的urls.py文件中补充以下内容
  url(r'^rbac/', include('rbac.urls',namespace='rbac')),\
  ```

+ 修改模板，并引入rbac中的组件及css文件，js文件

  ```
  
  
  模板中
  <link rel="stylesheet" href="{% static 'rbac/css/menu.css' %} "/>
  
  <script src="{% static 'rbac/js/menu_control.js' %}"></script>
  <script src="{% static 'rbac/js/table_control.js' %}"></script>
  ```

+ 批量添加路径及权限名

  ```
  对应路径：rbac/access/list/
  ```

  