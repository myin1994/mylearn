## Django项目快速配置

### 项目urls配置

```python
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include("app01.urls",namespace="app01")),
]
```

### 应用urls配置

```python
from django.conf.urls import url
from app01.views import *
urlpatterns = [
    url(r'^login/', Login.as_view(),name="login"),
]
```

### 项目settings配置

#### 数据库配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bms', # 要连接的数据库，连接前需要创建好
        'USER':'root',# 连接数据库的用户名
        'PASSWORD':'77963333', # 连接数据库的密码
        'HOST':'127.0.0.1',  # 连接主机，默认本机
        'PORT':3306 #  端口 默认3306
    }
}
```

#### 静态文件配置

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'statics'),
]
```

#### 时区配置

```python
TIME_ZONE = 'Asia/Shanghai'
```

#### Debug及允许ip配置

```python
DEBUG = True

ALLOWED_HOSTS = ["*"]
```

### 应用views配置

```python
from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from django.views import View
from django.utils.decorators import method_decorator
from django.urls import reverse
from app01 import models
from django.db import transaction
from django.db.models import *
from django.db.utils import *
```

### 应用中间件配置

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
```

### 应用Forms组件配置

```python
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models
import re
```

