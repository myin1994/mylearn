## Modelform

form与model的结合，会根据model中的字段转换成对应的form字段，并且生成标签等操作。

+ 定义方法

  + 继承forms.ModelForm类

  + 定义Meta类（相关参数针对modes表中字段分别设置）

    + `model = models.Book` 对应的Model中的类
    + `fields = "__all__" `# 字段，如果是`__all__`,就是表示列出所有的字段
    + `exclude = None`  排除的字段
    + `labels = None` 提示信息
    + `help_texts = None` 帮助提示信息
    + `widgets = None` 自定义插件
    + `error_messages = None`  自定义错误信息

    ```python
    class Meta:
            model = models.Book
            fields = '__all__'
            labels = {
                'title':'书名',
                'price':'价格',
                'publishDate':'出版日期',
                'publishs':'出版社',
                'authors':'作者',
            }
            error_messages = {
                'title':{
                    'required':'书名不能为空',
                    'max_length':'太长了',
                },
                'price':{
                    'required':'价格不能为空',
                }
    
            }
            validators={
                'title':[mobile_validate,]
            }
    ```

  + 重写字段属性并覆盖自动翻译的字段（按照Form的写法）

    ```python
    class BookModelForm(forms.ModelForm):
        
        # 自己定义的属性优先级高,会覆盖modelform翻译出来的属性
        # title = forms.CharField(
        #     label='书籍名称',
        #     min_length=1,
        #     max_length=32,
        #     validators=[mobile_validate, ],
        #     # widget=forms.TextInput(attrs={'class':'form-control'})
        #     error_messages={
        #         'required': '不能为空',
        #         'min_length': '太短了,你也好意思!',
        # 
        #     }
        # )
    ```

  + init进行批量操作、局部、全局钩子同Form

    ```python
        def __init__(self,*args,**kwargs):
    
            super().__init__(*args,**kwargs)
    
            for field in self.fields.values():
                field.widget.attrs.update({'class':'form-control xx oo'})
    	
    	#init方法和局部钩子还有全局钩子写法和form一模一样
    	#局部钩子：
        def clean_title(self):
            pass
    　　#全局钩子
        def clean(self):
            pass
    ```

+ ModelForm的验证

  + ModelForm表单的验证在调用is_valid() 或访问errors 属性时隐式调用
  + 可以像使用Form类一样自定义局部钩子方法和全局钩子方法来实现自定义的校验规则
  + 如果不重写具体字段并设置validators属性的话，ModelForm是按照模型中字段的validators来校验的

+ save()方法

  每个ModelForm还具有一个save()方法。 这个方法根据表单绑定的数据创建并保存数据库对象。 ModelForm的子类可以接受现有的模型实例作为关键字参数instance。

  + 不提供instance参数，将创建模型的一个新实例
  + 提供instance参数，save()将更新该实例

  ```python
  >>> from myapp.models import Book
  >>> from myapp.forms import BookForm
  
  # 根据POST数据创建一个新的form对象
  >>> form_obj = BookForm(request.POST)
  
  # 创建书籍对象
  >>> new_ book = form_obj.save()
  
  # 基于一个书籍对象创建form对象
  >>> edit_obj = Book.objects.get(id=1)
  # 使用POST提交的数据更新书籍对象
  >>> form_obj = BookForm(request.POST, instance=edit_obj)
  >>> form_obj.save()
  ```

  + save(commit=False)

    如果声明 save(commit=False)，那么它就会返回一个还未保存至数据库的对象，这样的话 你可以用这个对象添加一些额外的数据，然后在用save（）保存到数据库

  + save_m2m()方法

    在save（commit=False）的时候，如果你的model中含有many-to-many的数据模型，那么你将无法使用save（）方法去保存数据，只能使用save_m2m()方法来保存