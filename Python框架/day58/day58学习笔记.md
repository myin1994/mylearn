## Form组件使用

+ 主要功能

  + 生成页面可用的HTML标签
  + 对用户提交的数据进行校验
  + 保留上次输入内容

+ 基本使用方法

  + 定义form类

    ```python
    from django import forms
    
    # 按照Django form组件的要求自己写一个类
    class RegForm(forms.Form):
        name = forms.CharField(label="用户名")  #form字段的名称写的是什么，那么前端生成input标签的时候，input标签的name属性的值就是什么
        pwd = forms.CharField(label="密码")
    ```

  + views中使用

    ```python
    # 使用form组件实现注册方式
    def register2(request):
        form_obj = RegForm()
        if request.method == "POST":
            # 实例化form对象的时候，把post提交过来的数据直接传进去
            form_obj = RegForm(data=request.POST)  #既然传过来的input标签的name属性值和form类对应的字段名是一样的，所以接过来后，form就取出对应的form字段名相同的数据进行form校验
            # 调用form_obj校验数据的方法
            if form_obj.is_valid():
                print(form_obj.cleaned_data)#校验通过的数据包含所有form类中字段及对应值
                return HttpResponse("注册成功")
        return render(request, "register2.html", {"form_obj": form_obj})
    ```

  + html中使用

    + {{ form_obj.as_p }}   在<p> 显示表单

    + {{ form_obj.as_ul }}   在<ul> 显示表单

    + {{ form_obj.as_table }}   在<table> 显示表单

    + 循环设置

      ```html
      {% for field in obj %}
           {{ field.label_tag }}{{ field }}
           {{ field.errors }}
      {% endfor %}
      ```

    + 单独取值

      ```html
      <body>
          <form action="/reg2/" method="post" novalidate autocomplete="off">  #novalidate 告诉前端form表单，不要对输入的内容做校验
              {% csrf_token %}
              <div>
                  <label for="{{ form_obj.name.id_for_label }}">{{ form_obj.name.label }}</label>
                  {{ form_obj.name }} {{ form_obj.name.errors.0 }}  #errors是这个字段所有的错误，我就用其中一个错误提示就可以了，再错了再提示，并且不是给你生成ul标签了，单纯的是错误文本
                 {{ form_obj.errors }} #这是全局的所有错误，找对应字段的错误，就要form_obj.字段名
              </div>
              <div>
                  <label for="{{ form_obj.pwd.id_for_label }}">{{ form_obj.pwd.label }}</label>
                  {{ form_obj.pwd }} {{ form_obj.pwd.errors.0 }}
              </div>
              <div>
                  <input type="submit" class="btn btn-success" value="注册">
              </div>
          </form>
      </body>
      ```

+ Form常用字段与插件

  创建Form类时，主要涉及到 【字段】 和 【插件】，字段用于对用户请求数据的验证，插件用于自动生成HTML

  + initial:初始值，input框里面的初始值(str)

    ```python
    class LoginForm(forms.Form):
        username = forms.CharField(  
            min_length=8,
            label="用户名",
            initial="张三"  # 设置默认值
        )
        pwd = forms.CharField(min_length=6, label="密码")
    ```

  + error_messages:重写错误信息(dic)

    ```python
    class LoginForm(forms.Form):
        username = forms.CharField(
            min_length=8,
            label="用户名",
            initial="张三",
            error_messages={
                "required": "不能为空",
                "invalid": "格式错误",
                "min_length": "用户名最短8位"
            }
        )
        pwd = forms.CharField(min_length=6, label="密码")
    ```

  + widget:自定义小部件(Django默认TextInput窗口小部件)

    + password

      ```python
      class LoginForm(forms.Form):
          ...
          pwd = forms.CharField(
              min_length=6,
              label="密码",
              widget=forms.widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True) #这个密码字段和其他字段不一样，默认在前端输入数据错误的时候，点击提交之后，默认是不保存的原来数据的，但是可以通过这个render_value=True让这个字段在前端保留用户输入的数据
          )
      ```

    + radioSelect:单选

      ```python
      class LoginForm(forms.Form):
          username = forms.CharField(  #其他选择框或者输入框，基本都是在这个CharField的基础上通过插件来搞的
              min_length=8,
              label="用户名",
              initial="张三",
              error_messages={
                  "required": "不能为空",
                  "invalid": "格式错误",
                  "min_length": "用户名最短8位"
              }
          )
          pwd = forms.CharField(min_length=6, label="密码")
          gender = forms.fields.ChoiceField(
              choices=((1, "男"), (2, "女"), (3, "保密")),
              label="性别",
              initial=3,
              widget=forms.widgets.RadioSelect()
          )
      ```

    + Select：下拉单选

      ```python
      class LoginForm(forms.Form):
          ...
          hobby = forms.fields.ChoiceField(  #注意，单选框用的是ChoiceField，并且里面的插件是Select，不然验证的时候会报错， Select a valid choice的错误。
              choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
              label="爱好",
              initial=3,
              widget=forms.widgets.Select()
          )
      ```

    + Select:多选

      ```python
      class LoginForm(forms.Form):
          ...
          hobby = forms.fields.MultipleChoiceField( #多选框的时候用MultipleChoiceField，并且里面的插件用的是SelectMultiple，不然验证的时候会报错。
              choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
              label="爱好",
              initial=[1, 3],
              widget=forms.widgets.SelectMultiple()
          )
      ```

    + checkbox:单选&多选

      ```python
      #单选
      class LoginForm(forms.Form):
          ...
          keep = forms.fields.ChoiceField(
              label="是否记住密码",
              initial="checked",
              widget=forms.widgets.CheckboxInput()
          )
      ```

      ```python
      #多选
      class LoginForm(forms.Form):
          ...
          hobby = forms.fields.MultipleChoiceField(
              choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
              label="爱好",
              initial=[1, 3],
              widget=forms.widgets.CheckboxSelectMultiple()
          )
      ```

    + date类型

      ```python
      from django import forms
      from django.forms import widgets
      class BookForm(forms.Form):
          date = forms.DateField(widget=widgets.TextInput(attrs={'type':'date'}))  #必须指定type，不然不能渲染成选择时间的input框
      ```

  + choice字段注意事项

    在使用选择标签时，需要注意choices的选项可以配置从数据库中获取，但是由于是静态字段 获取的值无法实时更新，需要重写构造方法从而实现choice实时更新。

    + 方式一：

      ```python
      from django.forms import Form
      from django.forms import widgets
      from django.forms import fields
      
       
      class MyForm(Form):
       
          user = fields.ChoiceField(
              # choices=((1, '上海'), (2, '北京'),),
              initial=2,
              widget=widgets.Select
          )
       
          def __init__(self, *args, **kwargs):
              super(MyForm,self).__init__(*args, **kwargs)
              # self.fields['user'].choices = ((1, '上海'), (2, '北京'),)
              # 或
              self.fields['user'].choices = models.Classes.objects.all().values_list('id','caption')
      ```

    + 方式二：

      ```python
      publishs = forms.ModelChoiceField(
              label="出版社",
              queryset=models.Publish.objects.all()
          )
          authors = forms.ModelMultipleChoiceField(
              label="作者",
              # choices=[(1,"name1"),(2,"name2"),(3,"name3")]
              queryset=models.Author.objects.all()
          )
      #如果用这种方式，别忘了model表中，NNEWType的__str__方法要写上，不然选择框里面是一个个的object对象
      ```

+ Form所有内置字段总结

  + Field

    + required=True,               是否允许为空
    + widget=None,                 HTML插件
    + label=None,                  用于生成Label标签或显示内容
    + initial=None,                初始值
    +  help_text='',                帮助信息(在标签旁边显示)
    + error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
    + validators=[],               自定义验证规则
    + localize=False,              是否支持本地化
    + disabled=False,              是否可以编辑
    + label_suffix=None            Label内容后缀

  + CharField(Field)

    + max_length=None,             最大长度
    + min_length=None,             最小长度
    + strip=True                   是否移除用户输入空白

  + IntegerField(Field)

    + max_value=None,              最大值
    + min_value=None,              最小值
    + FloatField(IntegerField)

  + DecimalField(IntegerField)

    + max_value=None,              最大值
    + min_value=None,              最小值
    + max_digits=None,             总长度
    + decimal_places=None,         小数位长度

  + BaseTemporalField(Field)

    + input_formats=None          时间格式化
    + DateField(BaseTemporalField)    格式：2015-09-01
    + TimeField(BaseTemporalField)    格式：11:12
    + DateTimeField(BaseTemporalField)格式：2015-09-01 11:12
    + DurationField(Field)            时间间隔：%d %H:%M:%S.%f

  + RegexField(CharField)

    + regex,                      自定制正则表达式
    + max_length=None,            最大长度
    + min_length=None,            最小长度
    + error_message=None,         忽略，错误信息使用 error_messages={'invalid': '...'}

  + EmailField(CharField)

  + FileField(Field)

    + allow_empty_file=False     是否允许空文件

  + URLField(Field)

  + BooleanField(Field) 

  + NullBooleanField(BooleanField)

  + ChoiceField(Field)

    + choices=(),                选项，如：choices = ((0,'上海'),(1,'北京'),)
    + required=True,             是否必填
    + widget=None,               插件，默认select插件
    + label=None,                Label内容
    + initial=None,              初始值
    + help_text='',              帮助提示

  + ModelChoiceField(ChoiceField)/ModelMultipleChoiceField(ModelChoiceField)

    + queryset,                  # 查询数据库中的数据
    + empty_label="---------",   # 默认空显示内容
    + to_field_name=None,        # HTML中value的值对应的字段
    + limit_choices_to=None      # ModelForm中对queryset二次筛选

  + TypedChoiceField(ChoiceField)

    + coerce = lambda val: val   对选中的值进行一次转换
    + empty_value= " "            空值的默认值

  + MultipleChoiceField(ChoiceField)

  + TypedMultipleChoiceField(MultipleChoiceField)

    + coerce = lambda val: val   对选中的每一个值进行一次转换
    +  empty_value= ''            空值的默认值

  + ComboField(Field)

    +  fields=()                  使用多个验证

      ```python
      #如：即验证最大长度20，又验证邮箱格式
      fields.ComboField(fields=[fields.CharField(max_length=20), fields.EmailField(),])
      ```

  + MultiValueField(Field)

    抽象类，子类中可以实现聚合多个字典去匹配一个值，要配合MultiWidget使用

  + SplitDateTimeField(MultiValueField)

    + input_date_formats=None,   格式列表：['%Y--%m--%d', '%m%d/%Y', '%m/%d/%y']
    + input_time_formats=None    格式列表：['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']

  + FilePathField(ChoiceField)     文件选项，目录下文件显示在页面中

    + path,                      文件夹路径
    + match=None,                正则匹配
    + recursive=False,           递归下面的文件夹
    + allow_files=True,          允许文件
    + allow_folders=False,       允许文件夹
    + required=True,
    + widget=None,
    + label=None,
    + initial=None,
    + help_text=''

  + GenericIPAddressField

    + protocol='both',           both,ipv4,ipv6支持的IP格式
    + unpack_ipv4=False          解析ipv4地址，如果是::ffff:192.0.2.1时候，可解析为192.0.2.1， PS：protocol必须为both才能启用

  + SlugField(CharField)           数字，字母，下划线，减号（连字符）

  + UUIDField(CharField)           uuid类型

+ 字段校验

  + RegexValidator验证器

    ```python
    from django.forms import Form
    from django.forms import widgets
    from django.forms import fields
    from django.core.validators import RegexValidator
     
    class MyForm(Form):
        user = fields.CharField(
            validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
        )
    ```

  + 自定义验证函数

    ```python
    from django.core.exceptions import ValidationError
    from app01 import models
    import re
    
    
    def title_validate(value):
        title_re = re.compile(r'.*--.*')
        if title_re.match(value):
            raise ValidationError('不能包含--特殊字符')#固定异常类型
    
    
    class BookForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs["class"] = "form-control"
    
        title = forms.CharField(
            label="书籍名称",
            label_suffix="",
            min_length=1,
            validators=[title_validate, ],
            # widget=forms.TextInput(attrs={"class":"form-control"})
            error_messages={
                "required": "不能为空"
            }
        )
    ```

  + 钩子函数实现自定义的验证功能

    + 局部钩子

      在Fom类中定义 clean_字段名() 方法，就能够实现对特定字段进行校验

      ```python
      class LoginForm(forms.Form):
          username = forms.CharField(
              min_length=8,
              label="用户名",
              initial="张三",
              error_messages={
                  "required": "不能为空",
                  "invalid": "格式错误",
                  "min_length": "用户名最短8位"
              },
              widget=forms.widgets.TextInput(attrs={"class": "form-control"})
          )
          ...
          # 定义局部钩子，用来校验username字段,之前的校验股则还在，给你提供了一个添加一些校验功能的钩子
          def clean_username(self):
              value = self.cleaned_data.get("username")
              if "666" in value:
                  raise ValidationError("光喊666是不行的")
              else:
                  return value
      ```

    + 全局钩子

      我们在Fom类中定义 clean() 方法，就能够实现对字段进行全局校验，字段全部验证完，局部钩子也全部执行完之后，执行这个全局钩子校验。

      ```python
      class LoginForm(forms.Form):
          ...
          password = forms.CharField(
              min_length=6,
              label="密码",
              widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
          )
          re_password = forms.CharField(
              min_length=6,
              label="确认密码",
              widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
          )
          ...
          # 定义全局的钩子，用来校验密码和确认密码字段是否相同，执行全局钩子的时候，cleaned_data里面肯定是有了通过前面验证的所有数据
          def clean(self):
              password_value = self.cleaned_data.get('password')
              re_password_value = self.cleaned_data.get('re_password')
              if password_value == re_password_value:
                  return self.cleaned_data #全局钩子要返回所有的数据
              else:
                  self.add_error('re_password', '两次密码不一致') #在re_password这个字段的错误列表中加上一个错误，并且clean_data里面会自动清除这个re_password的值，所以打印clean_data的时候会看不到它
                  raise ValidationError('两次密码不一致')
      ```

+ 批量添加样式

  通过重写form类的init方法来实现

  ```python
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field_name, field in self.fields.items():
              field.widget.attrs["class"] = "form-control a b"#多个通过空格分隔
  ```

  