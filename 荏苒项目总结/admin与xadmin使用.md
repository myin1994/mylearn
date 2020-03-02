# Admin

django内置了一个强大的组件叫Admin，提供给网站管理员快速开发运营后台的管理站点。

站点文档： https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/admin/

辅助文档：https://www.runoob.com/django/django-admin-manage-tool.html

![1583133258488](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday102/day016/assets/1583133258488.png)

```
要使用Admin，必须先创建超级管理员.
python manage.py createsuperuser
```

访问地址：http://api.renran.cn:8000/admin，访问效果如下：

![1583133324063](F:/Python%E5%AD%A6%E4%B9%A0/%E8%80%81%E7%94%B7%E5%AD%A9%E7%9B%B8%E5%85%B3/%E6%AD%A3%E5%BC%8F%E5%AD%A6%E4%B9%A0%E8%A7%86%E9%A2%91/Python-vue-%E8%8D%8F%E8%8B%92%E9%A1%B9%E7%9B%AEday102/day016/assets/1583133324063.png)



admin站点默认并没有提供其他的操作给我们，所以一切功能都需要我们进行配置，在项目中，我们每次创建子应用的时候都会存在一个admin.py文件，这个文件就是用于配置admin站点功能的文件。

admin.py里面允许我们编写的代码一共可以分成三部分：

## 全局配置

用于配置运营站点的企业信息，站点标题，站点描述

```
暂无
```

## 列表页配置

主要用于针对项目中各个子应用里面的models.py里面的模型，根据这些模型自动生成后台运营站点的管理功能。

```python
from django.contrib import admin

# Register your models here.
from .models import User
class UserModelAdmin(admin.ModelAdmin):
    """用户模型管理类"""
    pass

admin.site.register(User, UserModelAdmin)
```

关于列表页的配置，代码：

```python
from django.contrib import admin
# Register your models here.
from .models import User
class UserModelAdmin(admin.ModelAdmin):
    """用户模型管理类"""
    date_hierarchy = 'last_login' # 按时间不同进行展示数据列表
    list_display = ['id', 'nickname',"username","last_login","is_superuser","email","my_mobile"]  # 设置列表页的展示字段
    ordering = ['-last_login'] # 设置默认排序字段,字段前面加上-号表示倒叙排列
    actions_on_bottom = True  # 下方控制栏是否显示,默认False表示隐藏
    actions_on_top = True     # 上方控制栏是否显示,默认False表示隐藏
    list_filter = ["is_superuser"] # 过滤器,按指定字段的不同值来进行展示
    search_fields = ["nickname"] # 搜索内容

    # 自定义字段的值,不能和模型同名
    def my_mobile(self, obj):
        # obj 表示当前模型
        if obj.mobile:
            return obj.mobile[:3]+"* * * *"+obj.mobile[-3:]
        else:
            return None

    my_mobile.empty_value_display = '-暂无-' # 自定义字段空值的时候,填补的默认值
    my_mobile.short_description = "手机号"   # 自定义字段的描述信息
    my_mobile.admin_order_field = "mobile"  # 自定义字段点击时使用哪个字段作为排序条件

    def save_model(self, request, obj, form, change):
        """当站点保存当前模型时"""
        print("有人修改了模型信息[添加/修改]")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """当站点删除当前模型时"""
        super().delete_model(request, obj)

admin.site.register(User, UserModelAdmin)
```

## 详情页配置

```python
from django.contrib import admin
# Register your models here.
from .models import User
class UserModelAdmin(admin.ModelAdmin):
    """用户模型管理类"""

    def save_model(self, request, obj, form, change):
        """当站点保存当前模型时"""
        print("有人修改了模型信息[添加/修改]")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """当站点删除当前模型时"""
        super().delete_model(request, obj)

    # 详情页中的展示字段
    # fields = ('nickname', 'username', 'mobile',"avatar") # exclude 作用与fields相反
    readonly_fields = ["nickname"] # 设置字段字段

    # 字段集,fieldsets和fields只能使用其中之一
    fieldsets = (
        ("必填项", {
            'fields': ('nickname', 'username', 'avatar')
        }),
        ('可选项', {
            'classes': ('collapse',), # 折叠样式
            'fields': ('mobile', 'alipay'),
        }),
    )

admin.site.register(User, UserModelAdmin)
```

# Xadmin

xadmin是Django的第三方扩展，可是使Django的admin站点使用更方便。

文档：https://xadmin.readthedocs.io/en/latest/index.html

## 安装

通过如下命令安装xadmin的最新版

```shell
pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
```

在配置文件中注册如下应用

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把apps目录设置环境变量中的导包路径
sys.path.append( os.path.join(BASE_DIR,"apps") )


INSTALLED_APPS = [
    ...
    # xamin主体模块
    'xadmin',
    # 渲染表格模块
    'crispy_forms',
    # 为模型通过版本控制，可以回滚数据
    'reversion',
    ...
]

# 修改使用中文界面
LANGUAGE_CODE = 'zh-Hans'

# 修改时区
TIME_ZONE = 'Asia/Shanghai'
```

xadmin有建立自己的数据库模型类，需要进行数据库迁移

```shell
python manage.py makemigrations
python manage.py migrate
```

在总路由中添加xadmin的路由信息

```python
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
]

```

创建超级用户

```python
python manage.py createsuperuser
```

## 使用

- xadmin不再使用Django的admin.py，而是需要编写代码在adminx.py文件中。
- xadmin的站点管理类不用继承`admin.ModelAdmin`，而是直接继承`object`即可。

例如：在子应用中创建adminx.py文件。

### 站点的全局配置

```python
import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)

```

### 站点Model管理

xadmin可以使用的页面样式控制基本与Django原生的admin一致。

+ 注册站点models

  ```python
  import xadmin
  
  from .models import Students
  class StudentModelAdmin(object):
      list_display = ["id", "name", "sex", "age","my_class_number"]
      list_editable = ["age"]  # 允许直接在列表页面中修改的字段
      show_detail_fields = ["name"]  # 允许用户通过点击哪些即可查看整个模型里面所有的数据
      refresh_times = [3, 30, 60, 90]  # 设置当前列表页在指定事件内刷新页面
  
      def my_class_number(self,obj):
          return obj.class_number+"班"
  
      my_class_number.short_description = "班级"
  
  xadmin.site.register(Students, StudentModelAdmin)
  ```

+ **list_display** 控制列表展示的字段

  ```python
  list_display = ['id', 'btitle', 'bread', 'bcomment']
  ```

+ **search_fields** 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询

  ```python
  search_fields = ['id','btitle']
  ```

+ **list_filter** 可以进行过滤操作的列，对于分类、性别、状态

  ```python
  list_filter = ['is_delete']
  ```

+ **ordering** 默认排序的字段

+ **readonly_fields** 在编辑页面的只读字段

+ **exclude** 在编辑页面隐藏的字段

+ **list_editable** 在列表页可以快速直接编辑的字段(与自定义字段冲突)

+ **show_detail_fields** 在列表页提供快速显示详情信息

+ **refresh_times** 指定列表页的定时刷新

  ```python
  refresh_times = [5, 10,30,60]  # 设置允许后端管理人员按多长时间(秒)刷新页面
  ```

+ **list_export** 控制列表页导出数据的可选格式

  ```python
  list_export = ('xls', 'xml', 'json')   #list_export设置为None来禁用数据导出功能
  list_export_fields = ('id', 'title', 'pub_date') # 允许导出的字段
  ```

+ **show_bookmarks** 控制是否显示书签功能

  ```python
  show_bookmarks = True
  ```

+ **data_charts** 控制显示图表的样式

  ```python
  data_charts = {
          "order_amount": {
            'title': '图书发布日期表', 
            "x-field": "bpub_date", 
            "y-field": ('btitle',),#可以使用自定义字段函数
            "order": ('id',)
          },
      #    支持生成多个不同的图表
      #    "order_amount": {
      #      'title': '图书发布日期表', 
      #      "x-field": "bpub_date", 
      #      "y-field": ('btitle',),
      #      "order": ('id',)
      #    },
      }
  
  ```

  - title 控制图标名称
  - x-field 控制x轴字段
  - y-field 控制y轴字段，可以是多个值
  - order 控制默认排序

- **model_icon** 控制菜单的图标

  ```python
  class BookInfoAdmin(object):
      model_icon = 'fa fa-gift'
  
  xadmin.site.register(models.BookInfo, BookInfodmin)
  ```
  
- 修改admin或者xadmin站点下的子应用成中文内容。

  ```python
  # 在子应用的apps下面的配置中，新增一个属性verbose_name
  from django.apps import AppConfig
  
  class StudentsConfig(AppConfig):
      name = 'students'
      verbose_name = "学生管理"
  
  
  # 然后在子应用的__init__.py里面新增一下代码：
  default_app_config = "students.apps.StudentsConfig"
  ```

### 自定义用户管理

```python
import xadmin
# Register your models here.

from .models import User
from xadmin.plugins import auth


class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'mobile', 'email', 'date_joined']
    readonly_fields = ['last_login', 'date_joined']
    search_fields = ('username', 'first_name', 'last_name', 'email', 'mobile')
    style_fields = {'user_permissions': 'm2m_transfer', 'groups': 'm2m_transfer'}

    def get_model_form(self, **kwargs):
        # org_obj, 原始数据对象(User), 判断是否有用户
        if self.org_obj is None:
            # 添加用户表单
            self.fields = ['username', 'mobile', 'is_staff']

        return super().get_model_form(**kwargs)


xadmin.site.unregister(User)  # 反注册
xadmin.site.register(User, UserAdmin)  # 自己再注册
```

