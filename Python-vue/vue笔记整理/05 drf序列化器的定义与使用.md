# 序列化器-Serializer

+ 作用

  + 序列化

    序列化器会把模型对象转换成字典,将来提供给视图经过response以后变成json字符串

  + 反序列化

    + 把客户端发送过来的数据,经过视图调用序列化器以后变成python字典,序列化器可以把字典转成模型
    + 反序列化,完成数据校验功能和操作数据库


## 定义序列化器

Django REST framework中的Serializer使用类来定义，须继承自rest_framework.serializers.Serializer。

+ 创建子应用并注册

  接下来，为了方便演示序列化器的使用，我们另外创建一个新的子应用sers

  ```
  python manage.py startapp sers
  ```

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  
      'rest_framework', # 把drf框架注册到django项目中
  
      'sers',
  ]
  ```

+ 创建模型models

  ```python
  class Student(models.Model):
      # 模型字段
      name = models.CharField(max_length=100,verbose_name="姓名")
      sex = models.BooleanField(default=1,verbose_name="性别")
      age = models.IntegerField(verbose_name="年龄")
      class_number = models.CharField(max_length=5,verbose_name="班级编号")
      description = models.TextField(max_length=1000,verbose_name="个性签名")
  
      class Meta:
          db_table="tb_student"
          verbose_name = "学生"
          verbose_name_plural = verbose_name
  ```

+ 定义序列化器

  为这个模型类提供一个序列化器，可以命名为`StudentSerializer`，在子应用下创建serializers.py模块

  ```python
  from rest_framework import serializers
  
  # 声明序列化器，所有的序列化器都要直接或者间接继承于 Serializer
  # 其中，ModelSerializer是Serializer的子类，ModelSerializer在Serializer的基础上进行了代码简化
  class StudentSerializer(serializers.Serializer):
      """学生信息序列化器"""
      # 1. 需要进行数据转换的字段
      id = serializers.IntegerField()
      name = serializers.CharField()
      age = serializers.IntegerField()
      sex = serializers.BooleanField()
      description = serializers.CharField()
  
      # 2. 如果序列化器集成的是ModelSerializer，则需要声明调用的模型信息
  
      # 3. 验证代码
  
      # 4. 编写添加和更新模型的代码
  ```

  **注意：serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。**serializer是独立于数据库之外的存在。

+ **常用字段类型**

| 字段                    | 字段构造方式                                                 |
| ----------------------- | ------------------------------------------------------------ |
| **BooleanField**        | BooleanField()                                               |
| **NullBooleanField**    | NullBooleanField()                                           |
| **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True) |
| **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank=False) |
| **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
| **SlugField**           | SlugField(max*length=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9*-]+ |
| **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
| **UUIDField**           | UUIDField(format='hex_verbose')  format:  1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"`  2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"`  3）`'int'` - 如: `"123456789012312313134124512351145145114"`  4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
| **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
| **IntegerField**        | IntegerField(max_value=None, min_value=None)                 |
| **FloatField**          | FloatField(max_value=None, min_value=None)                   |
| **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None) max_digits: 最多位数 decimal_palces: 小数点位置 |
| **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
| **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
| **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
| **DurationField**       | DurationField()                                              |
| **ChoiceField**         | ChoiceField(choices) choices与Django的用法相同               |
| **MultipleChoiceField** | MultipleChoiceField(choices)                                 |
| **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ListField**           | ListField(child=, min_length=None, max_length=None)          |
| **DictField**           | DictField(child=)                                            |

+ **选项参数**

| 参数名称            | 作用             |
| ------------------- | ---------------- |
| **max_length**      | 最大长度         |
| **min_lenght**      | 最小长度         |
| **allow_blank**     | 是否允许为空     |
| **trim_whitespace** | 是否截断空白字符 |
| **max_value**       | 最小值           |
| **min_value**       | 最大值           |

+ **通用参数**

| 参数名称           | 说明                                          |
| ------------------ | --------------------------------------------- |
| **read_only**      | 表明该字段仅用于序列化输出，默认False         |
| **write_only**     | 表明该字段仅用于反序列化输入，默认False       |
| **required**       | 表明该字段在反序列化时必须输入，默认True      |
| **default**        | 反序列化时使用的默认值                        |
| **allow_null**     | 表明该字段是否允许传入None，默认False         |
| **validators**     | 该字段使用的验证器                            |
| **error_messages** | 包含错误编号与错误信息的字典                  |
| **label**          | 用于HTML展示API页面时，显示的字段名称         |
| **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |



## 创建Serializer对象

定义好Serializer类后，就可以创建Serializer对象了。

+ Serializer的构造方法为

  ```python
  Serializer(instance=None, data=empty, **kwarg)
  ```

+ 说明

  + 用于序列化时，将模型类对象传入**instance**参数

  + 用于反序列化时，将要被反序列化的数据传入**data**参数

  + 除了instance和data参数外，在构造Serializer对象时，还可通过**context**参数额外添加数据，如

    ```python
    serializer = AccountSerializer(account, context={'request': request})
    ```

    **通过context参数附加的数据，可以通过Serializer对象的self.context属性获取。**

+ 注意事项

  + 使用序列化器的时候一定要注意，序列化器声明了以后，不会自动执行，需要我们在视图中进行调用才可以。
  + 序列化器无法直接接收数据，需要我们在视图中创建序列化器对象时把使用的数据传递过来。
  + 序列化器的字段声明类似于我们前面使用过的表单系统。
  + 开发restful api时，序列化器会帮我们把模型数据转换成字典.
  + drf提供的视图会帮我们把字典转换成json,或者把客户端发送过来的数据转换字典.

## 序列化器的使用

+ 序列化器的使用分两个阶段：
  1. 在客户端请求时，使用序列化器可以完成对数据的反序列化。
  2. 在服务器响应时，使用序列化器可以完成对数据的序列化。

### 序列化

+ 获取模型对象（model、queryset对象）

  + 查询出一个学生对象--model

    ```python
    from students.models import Student
    
    student = Student.objects.get(id=3)
    ```

  + 查询多个--queryset

    ```python
    student_list = Student.objects.all()
    ```

+ 构造序列化器对象

  + model对象

    ```python
    from .serializers import StudentSerializer
    
    serializer = StudentSerializer(instance=student)
    ```

  + queryset对象---需要指定参数**many=True**

    ```python
    serializer = StudentSerializer(instance=student_list,many=True)
    ```

+ 获取序列化数据---serializer.data属性

  + 单个对象返回结果为字典

    ```python
    {'id': 4, 'name': '小张', 'age': 18, 'sex': True, 'description': '猴赛雷'}
    ```

  + 多个对象返回结果为字典套有序字典

    ```python
    [OrderedDict([('id', 1), ('name', 'xiaoming'), ('age', 20), ('sex', True), ('description', '测试')]), OrderedDict([('id', 2), ('name', 'xiaohui'), ('age', 22), ('sex', True), ('description', '后面来的测试')]), OrderedDict([('id', 4), ('name', '小张'), ('age', 18), ('sex', True), ('description', '猴赛雷')])]
    ```

+ 完整视图代码

  + 单个对象--model

    ```python
    from django.views import View
    from students.models import Student
    from .serializers import StudentSerializer
    from django.http.response import JsonResponse
    class StudentView(View):
        """使用序列化器序列化转换单个模型数据"""
        def get(self,request,pk):
            # 获取数据
            student = Student.objects.get(pk=pk)
            # 数据转换[序列化过程]
            serializer = StudentSerializer(instance=student)
            print(serializer.data)
            # 响应数据
            return JsonResponse(serializer.data)
    ```

  + 查询集--QuerySet

    ```python
        """使用序列化器序列化转换多个模型数据"""
        def get(self,request):
            # 获取数据
            student_list = Student.objects.all()
    
            # 转换数据[序列化过程]
            # 如果转换多个模型对象数据，则需要加上many=True
            serializer = StudentSerializer(instance=student_list,many=True)
            print( serializer.data ) # 序列化器转换后的数据
    
            # 响应数据给客户端
            # 返回的json数据，如果是列表，则需要声明safe=False
            return JsonResponse(serializer.data,safe=False)
    ```

### 反序列化

#### 数据校验

+ 功能介绍

  使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型类对象。

+ 创建models模型对象

  ```python
  from django.db import models
  
  # Create your models here.
  class BookInfo(models.Model):
      """图书信息"""
      title = models.CharField(max_length=20, verbose_name='标题')
      pub_date = models.DateField(verbose_name='发布日期')
      image = models.ImageField(verbose_name='图书封面')
      price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
      read = models.IntegerField(verbose_name='阅读量')
      comment = models.IntegerField(verbose_name='评论量')
      class Meta:
          # db_table = "表名"
          db_table = "tb_book_info"
          verbose_name = "图书"
          verbose_name_plural = verbose_name
  ```

  **注意：因为当前模型中， 涉及到图片上传处理，所以我们需要安装`PIL`库**

  ```
  pip install Pillow
  ```

+ 创建序列化器

  ```python
  from rest_framework import serializers
  
  class BookInfoSerializer(serializers.Serializer):
      # 这里声明的字段用于进行反序列化器
      # 字段名 = serializers.字段类型(验证选项)
      title = serializers.CharField(max_length=20, label="标题", help_text="标题")
      # required=True 当前字段必填
      pub_date = serializers.DateField(required=True,label="发布日期", help_text="发布日期")
      image = serializers.ImageField(max_length=3*1024*1024, label="图书封面", help_text="图书封面")
      price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True, label="价格", help_text="价格")
      read  = serializers.IntegerField(min_value=0, default=0, label="阅读量", help_text="阅读量")
      comment = serializers.IntegerField(min_value=0, default=0, label="评论量", help_text="评论量")
  
      # 关于继承数据库选项
  
      # 验证部分的代码
  
      # 数据库
  ```

+ 数据校验---is_valid()

  + 在获取反序列化的数据前，必须调用**is_valid()**方法，序列化器内部是在**is_valid**方法内部进行验证，验证成功返回True，否则返回False。

  + 验证失败，可以通过序列化器对象的**errors**属性获取错误信息，返回字典，包含了字段和字段的错误。如果是非字段错误，可以通过修改REST framework配置中的**NON_FIELD_ERRORS_KEY**来控制错误字典中的键名。

  + 验证成功，可以通过序列化器对象的**validated_data**属性获取数据。

  + 在定义序列化器时，指明每个字段的序列化类型和选项参数，本身就是一种验证行为。

  + 构造序列化器对象---传入data数据

    ```python
    serializer = BookInfoSerializer(data=data)
    #data为待校验数据
    ```

  + 校验--调用is_valid()方法

    + 常规使用--根据返回值判断后续操作

      ```python
      ret = serializer.is_valid()
      ```
      
+ 调试使用--指定参数**raise_exception=True**
    
  在验证失败时抛出异常serializers.ValidationError，REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应。
    
+ 完整代码
  
  ```python
    # Create your views here.
    from django.views import View
    from django.http.response import HttpResponse
    from .serializers import BookInfoSerializer
    class BookInfoView(View):
        def get(self,request):
            """模拟客户端发送过来的数据"""
            data = {
                "title":"西厢记",
                "pub_date":"1980-10-10",
                "price": 19.80,
                "read": 100,
                "comment": -1,
            }
    
            # 对上面的数据进行反序列化器处理
            # 1. 初始化，填写data属性
            serializer = BookInfoSerializer(data=data)
            # 2. 调用序列化器提供的is_valid方法进行验证
            # raise_exception=True 表示终断程序，直接抛出错误
            ret = serializer.is_valid(raise_exception=True)
            print(ret) # is_valid的方法值就是验证结果，只会是True/False
            if ret:
                # 3.1 验证通过后，可以通过validated_data得到数据
                print("验证成功，ret=%s" % ret)
                print(serializer.validated_data)  # 验证处理后的数据
                """打印结果：
                OrderedDict([('title', '西厢记'), ('pub_date', datetime.date(1980, 10, 10)), ('price', Decimal('19.80')), ('read', 100), ('comment', 15)])
                """
            else:
                print("验证失败，ret=%s" % ret)
                # 3.1 验证没通过，可以通过
                print( serializer.errors )
                """打印结果：
                {'comment': [ErrorDetail(string='Ensure this value is greater than or equal to 0.', code='min_value')]}
                """
            return HttpResponse("ok")
    ```

#### 钩子函数

类似django的form和modelform，为了补充定义验证行为，可以使用以下三种方法

##### validate_字段名--局部钩子

对`<field_name>`字段进行验证，如

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    ...

    # 单个字段的验证，方法名必须： validate_<字段名>(self,data)    # data 就是当前字段中客户端提交的数据
    # validate_price 会被is_valid调用
    def validate_price(self, data):
        """"""
        if data < 0:
            raise serializers.ValidationError("对不起，价格不能低于0元")
        # 验证通过以后，必须要返回验证的结果数据，否则序列化器的validated_data无法得到当前字段的结果
        return data
```

#####  validate--全局钩子

在序列化器中需要同时对多个字段进行比较验证时，可以定义validate方法来验证，如

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    ...

    # 多个字段的验证，必须方法名叫 "validate"
    # data 表示客户端发送过来的所有数据，字典格式
    def validate(self, data):
        # 判断图书的阅读量不能低于评论量
        read = data.get("read")
        comment = data.get("comment")
        if read < comment:
            raise serializers.ValidationError("对不起，阅读量不能低于评论量")

        return data
```

#####  validators--自定义校验函数

在字段中添加validators选项参数，也可以补充验证行为，如

```python
from rest_framework import serializers
from .models import BookInfo
# 可以把验证函数进行多次使用，提供不用的字段或者不同的序列化器里面使用
def about_django(data):
    if "django" in data:
        raise serializers.ValidationError("对不起，图书标题不能出现关键字django")
    # 返回验证以后的数据
    return data

class BookInfoSerializer(serializers.Serializer):
    # 这里声明的字段用于进行反序列化器
    # 字段名 = serializers.字段类型(验证选项)
    title = serializers.CharField(max_length=20,validators=[about_django], label="标题", help_text="标题")
    # required=True 当前字段必填
    pub_date = serializers.DateField(required=True, label="发布日期", help_text="发布日期")
    # max_length 文件的大小
    # allow_null=True 允许传递的image数据为None
    image = serializers.ImageField(required=False, allow_null=True, max_length=3*1024*1024, label="图书封面", help_text="图书封面")
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True, label="价格", help_text="价格")
    # min_value 数值大小
    # default 设置默认值
    read  = serializers.IntegerField(min_value=0, default=0, label="阅读量", help_text="阅读量")
    comment = serializers.IntegerField(min_value=0, default=0, label="评论量", help_text="评论量")

```

##### is_valid验证顺序

is_valid实际上内部执行了三种不同的验证方式：
1. 先执行字段内置的验证选项
2. 再执行validators自定义选项
3. 最后执行validate自定义验证方法[包含了validate_<字段>, validate]



#### 操作数据

前面的验证数据成功后,我们可以使用序列化器来完成数据反序列化的过程.这个过程可以把数据转成模型类对象.

##### 数据添加

+ 在序列器中添加create方法

  ```python
  def create(self, validated_data):
  	return BookInfo.objects.create(**validated_data)
  ```

+ view中调用--serializer.save()

  ```python
  #验证通过后使用，返回添加的model对象
  book = serializer.save()
  ```

##### 数据更新

+ 在序列器中添加update方法

  ```python
  def update(self, instance, validated_data):
      for attr,value in validated_data.items():
          setattr(instance,attr,value)
          instance.save()
          return instance
  ```

+ 构造序列化器对象---更新操作，需要传入2个参数，分别是instance和data

  ```python
  book = BookInfo.objects.get(pk=id)
  serializer = BookInfoSerializer(instance=book,data=data)
  ```

+ view中调用--serializer.save()

  ```python
  #验证通过后使用，返回更新的model对象
  book = serializer.save()
  ```

##### 序列化器save的调用规则

+ serailzier对象调用的save方法是什么？怎么做到自动调用update和create?

  + 这里的save不是数据库ORM模型对象的save，是BaseSerializer定义的。
  + save方法中根据实例化serializer时是否传入instance参数来判断执行update还是create的
    + 当传入instance时，则instance.save调用的就是update方法
    + 没有传入instance，则instance.save调用的就是create方法
  + serializer.save使用前提是必须在序列化器中声明create或者update方法，否则报错！！

+ BaseSerializer中定义的save方法源码：

![1582086563954]($%7Basserts%7D/1582086563954.png)



##### 附加说明

+ 在对序列化器进行save()保存时，可以额外传递数据，这些数据可以在create()和update()中的validated_data参数获取到

```python
# request.user 是django中记录当前登录用户的模型对象
serializer.save(owner=request.user)
```

+ 默认序列化器必须传递所有required的字段，否则会抛出验证异常。但是我们可以使用partial参数来允许部分字段更新

```python
# Update `BookInfo` with partial data
serializer = BookInfoSerializer(book, data=data, partial=True)
```

# 模型类序列化器-ModelSerializer

针对上面虽然序列化和反序列化，我们可只声明一个序列化器，但是序列化器和模型还是存在很高的相似度。

所以我们可以在序列化器字段和模型字段公共字段较多的时候，可以基于ModelSerializer来声明创建序列化器。

如果我们想要使用序列化器对应的是Django的模型类，DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。

ModelSerializer是之前序列坏器基类Serializer的子类，功能大部分相同，但ModelSerializer还提供了：

- 基于模型类自动生成系列化器的字段
- 基于模型类自动为Serializer生成validators，比如unique_together[多个字段唯一]
- 包含默认的create()和update()的实现

## 定义

比如我们创建一个BookInfoModelSerializer

```python
class BookInfoModelSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
        # 从什么模型继承过来
        model = BookInfo
        # 继承那些字段过来
        fields = "__all__" # 表示继承所有字段
```

- model 指明参照哪个模型类
- fields 指明为模型类的哪些字段生成

我们可以在python manage.py shell中查看自动生成的BookInfoSerializer的具体实现

```python
from rest_framework import serializers

class BookInfoSerializer(serializers.Serializer):
    """图书信息"""
    id = serializers.IntegerField(read_only=True, label="ID", help_text="ID")
    title = serializers.CharField(max_length=20, label="标题", help_text="标题")
    pub_date = serializers.DateField(required=True, label="发布日期", help_text="发布日期")
    image = serializers.ImageField(required=False, allow_null=True, max_length=3 * 1024 * 1024, label="图书封面",
                                   help_text="图书封面")
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True, label="价格", help_text="价格")
    read = serializers.IntegerField(min_value=0, default=0, label="阅读量", help_text="阅读量")
    comment = serializers.IntegerField(min_value=0, default=0, label="评论量", help_text="评论量")
```

## 指定字段

+ 使用**fields**来明确字段，`__all__`表名包含所有字段，也可以写明具体哪些字段，如

  ```python
  class BookInfoModelSerializer(serializers.ModelSerializer):
      """图书数据序列化器"""
      class Meta:
          model = BookInfo
          fields = "__all__"
  ```

+ 使用**exclude**可以明确排除掉哪些字段

  ```python
  class BookInfoModelSerializer(serializers.ModelSerializer):
      """图书数据序列化器"""
      class Meta:
          model = BookInfo
          exclude = ['image']
  ```

+ 显式指明字段，如：

  ```python
  class BookInfoModelSerializer(serializers.ModelSerializer):
      class Meta:
          model = BookInfo
          fields = ["id","title","pub_date","price","read","comment"]
  ```

+ 指明只读字段

  可以通过**read_only_fields**指明只读字段，即仅用于序列化输出的字段

  ```python
  class BookInfoModelSerializer(serializers.ModelSerializer):
      """图书数据序列化器"""
      class Meta:
          model = BookInfo
          fields = ('id', 'title', 'pub_date'， 'read', 'comment')
          read_only_fields = ('id', 'read', 'comment')
  ```

## 添加额外参数

使用**extra_kwargs**参数为ModelSerializer添加或修改原有的选项参数，效果同序列化器的直接定义

```python
extra_kwargs = {
            "read":{"min_value":0,"help_text":"阅读量",},
            "title":{"min_length": 2,},
        }
```

## 钩子函数

定义使用方法同序列化器

```python
# def validate(self,data):
    # """所有字段验证"""
    # pass

# def validate_<字段>
	# pass
```

## 使用

使用方法同序列化器