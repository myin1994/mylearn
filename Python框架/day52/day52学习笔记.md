## 字段和参数

### 字段

+ CharField ----字符串字段, 用于较短的字符串

  + 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数

+ IntegerField----用于保存一个整数

+ DecimalField----浮点数（必须提供两个参数）

  + max_digits：总位数

  + decimal_places：小数位

    ```python
    models.DecimalField(..., max_digits=5, decimal_places=2)
    ```

+ AutoField----一个 IntegerField, 添加记录时它会自动增长

  + 通常不需要直接使用这个字段
  + 自定义一个主键：my_id=models.AutoField(primary_key=True)
  + 不指定主键的话,系统会自动添加一个主键字段-id(pk)

+ BooleanField----A true/false field

  + 用 checkbox 来表示此类字段

+ TextField----一个容量很大的文本字段

  + admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框)

+ EmailField----一个带有检查Email合法性的 CharField,不接受maxlength 参数

+ DateField----日期字段

  可选参数

  + Argument：描述

  + auto_now ：当对象被保存时(更新或者添加都行),自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳

  + auto_now_add：当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间（仅仅在admin中有意义...)

    ```
    #想让auto_now更新数据时自动更新时间，必须使用save方法来更新数据，所以很不方便，所以这个创建时自动添加时间或者更新时间的auto_now方法我们最好就别用了，比较恶心，并且支持我们自己来给这个字段更新时间：
    models.py:
    class Book(models.Model):
        name = models.CharField(max_length=32)
        date1 = models.DateTimeField(auto_now=True,null=True)
        date2 = models.DateTimeField(auto_now_add=True,null=True)
    
    views.py:
            import datetime
            models.Book.objects.filter(id=1).update(
                name='chao',
                date1=datetime.datetime.now(),
                date2=datetime.datetime.now(),
            )
    ```

+ DateTimeField----日期时间字段. 类似 DateField 支持同样的附加选项.

+ ImageField----类似 FileField, 不过要校验上传对象是否是一个合法图片

  + 两个可选参数:height_field和width_field,如果提供这两个参数,则图片将按提供的高度和宽度规格保存

+ FileField----文件上传字段

  + 必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting该格式将被上载文件的 date/time

    替换(so that uploaded files don't fill up the given directory)
  + admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件)

  ```
  注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
              （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
              (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
               WEB服务器用户帐号是可写的.
              （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
               使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
               出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
               叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.
  ```

  

+ URLField----用于保存 URL

  + 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且没有返回404响应)
  + admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)

+ NullBooleanField

  + 类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要用 BooleanField 加 null=True 选项
  + admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据

+ SlugField

  + "Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.#它们通常用于URLs

  + 若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50

    ````
    以前的 Django 版本,没有任何办法改变50 这个长度.
    这暗示了 db_index=True.
    它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto
    #populate the slug, via JavaScript,in the object's admin form: models.SlugField(prepopulate_from=("pre_name", "name"))
    prepopulate_from 不接受 DateTimeFields.
    ````

+ XMLField----一个校验值是否为合法XML的 TextField

  + 必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径

+ FilePathField----可选项目为某个特定目录下的文件名

  支持三个特殊的参数, 其中第一个是必须提供的

  + path :必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目( Example: "/home/images")

  + match：可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名（注意这个正则表达式只会应用到 base filename 而不是路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif）

  + recursive：可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录

    ```
    这三个参数可以同时使用.
            match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
            FilePathField(path="/home/images", match="foo.*", recursive=True)
            ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
    ```

+ IPAddressField----一个字符串形式的 IP 地址, (i.e. "24.124.1.30")

+ CommaSeparatedIntegerField

  + 用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数



### 约束参数

+ null
  + 如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False
+ blank
  + 如果为True，该字段允许不填。默认为False
  + 要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的
  + 如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的
+ default
  + 字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用
  + 如果字段没有设置可以为空，那么将来如果我们后添加一个字段，这个字段就要给一个default值
+ primary_key
  + 如果为True，那么这个字段就是模型的主键。
  + 如果你没有指定任何一个字段的primary_key=True，Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，否则没必要设置任何一个字段的primary_key=True
+ unique
  + 如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
+ choices
  + 由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项
  + 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项
+ db_index
  + 如果db_index=True 则代表着为此字段设置数据库索引



## 创建关系字段

+ 一对一( 作者模型 - 作者详细信息模型 )

  + 从表

    ```python
    class Author(models.Model): #比较常用的信息放到这个表里面
        name=models.CharField( max_length=32)
        age=models.IntegerField()
    
        # 与AuthorDetail建立一对一的关系，一对一的这个关系字段写在两个表的任意一个表里面都可以
        author_detail=models.OneToOneField(
            to="AuthorDetail",#to=可以不用写
            to_field="id",#可以不写,默认找主键
            on_delete=models.CASCADE#默认是级联删除,想做级联更新,直接去数据库修改表结构
        ) 
                             
        #就是foreignkey+unique，只不过不需要我们自己来写参数了，并且orm会自动帮你给这个字段名字拼上一个_id，数据库中字段名称为authorDetail_id
    
    ```

  + 主表

    ```python
    class AuthorDetail(models.Model):#不常用的放到这个表里面
        birthday=models.DateField()
        telephone=models.BigIntegerField()
        addr=models.CharField( max_length=64)
    ```

  +  创建一对一关系字段时的一些参数 

    + to：设置要关联的表
    + to_field：设置要关联的字段
    + on_delete：当删除关联表中的数据时，当前表与其关联的行的行为

+ 多对一（ 出版商模型 - 书籍模型 ：假定）

  + 主表

    ```python
    class Publish(models.Model):
        name=models.CharField(max_length=32)
        city=models.CharField(max_length=32)
    ```

  + 从表

    ```python
    class Book(models.Model):
        title = models.CharField(max_length=32)
        publishDate=models.DateField()
        price=models.DecimalField(max_digits=5,decimal_places=2)
        # 与Publish建立一对多的关系,外键字段建立在多的一方，字段publish如果是外键字段，那么它自动是int类型
        publishs=models.ForeignKey(
            to="Publish",
            to_field="id",
            on_delete=models.CASCADE
        )#自动在数据库中拼接为publishs_id
        authors=models.ManyToManyField(to='Author',)
    ```

  +  创建一对多关系字段时的一些参数

    + to：设置要关联的表
    + to_field：设置要关联的表的字段
    + related_name：反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'
    + related_query_name： 反向查询操作时，使用的连接前缀，用于替换表名
    + on_delete：当删除关联表中的数据时，当前表与其关联的行的行为

+ 多对多（ 作者模型 - 书籍模型 ）

  + 通过ManyToManyField自动创建第三张表（从表）

    ```python
    class Book(models.Model):
        title = models.CharField(max_length=32)
        publishDate=models.DateField()
        price=models.DecimalField(max_digits=5,decimal_places=2)
        publishs=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
        
        # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表(表名：应用名_当前表表名_属性名)，并且注意一点，你查看book表的时候，你看不到这个字段，因为这个字段就是创建第三张表的意思，不是创建字段的意思，所以只能说这个book类里面有authors这个字段属性
        authors=models.ManyToManyField(to='Author',)
        #自动创建app01_book_authors
        #注意不管是一对多还是多对多，写to这个参数的时候，最后后面的值是个字符串，不然你就需要将你要关联的那个表放到这个表的上面
    ```

  + 创建多对多字段时的一些参数

    + to：设置要关联的表
    + related_name：同ForeignKey字段
    + related_query_name：同ForeignKey字段
    + through：在使用ManyToManyField字段时，Django将自动生成一张表来管理多对多的关联关系，但我们也可以手动创建第三张表来管理多对多关系，此时就需要通过through来指定第三张表的表名。
    + through_fields：设置关联的字段
    + db_table：默认创建第三张表时，数据库中表的名称



## 多表增删改查

### 增加

+ 一对一

  + 先增加主表数据----作者详细信息表

    ```python
    models.AuthorDetail.objects.create(
            birthday='2018-11-11',
            telephone='15122220000',
            addr='北京'
        )
    ```

  + 再增加从表数据--作者表

    ```python
    models.Author.objects.create(
            name='金龙',
            age=2,
            ad=models.AuthorDetail.objects.get(id=1)#将一条记录直接插入
        )
    
    
    models.Author.objects.create(
            name='金龙2',
            age=2,
            ad_id=2#直接对外键赋值
    
        )
    ```

+ 一对多

  + 先增加主表（方法同上）----出版社信息

  + 再增加从表数据（方法同一对一）----书籍信息

    ```python
    models.Book.objects.create(
            title='白洁',
            publishDate='2011-01-01',
            price=200,
            publishs=models.Publish.objects.get(id=1)#只能添加主表中存在的id
        )
    
        models.Book.objects.create(
            title='白洁第二部',
            publishDate='2011-01-01',
            price=300,
            publishs_id=1
        )
    ```

+ 多对多

  + 先增加主表数据----书籍信息&作者信息

  + 再增加从表数据（第三张表）----app01_book_authors

    + 方式1：通过对象记录添加

      ```python
      book_obj = models.Book.objects.get(id=1)
      author1 = models.Author.objects.get(id=1)
      author2 = models.Author.objects.get(id=2)
      
      #通过添加建表属性的属性方法添加（因为没有第三个表的类存在）
      book_obj.authors.add(author1,author2)
      book_obj.authors.add(*[author1,author2])
      ```

    + 方式2：直接添加值

      ```python
      book_obj = models.Book.objects.get(id=1)
      book_obj.authors.add(1,2)
      book_obj.authors.add(*[1,2])
      ```

### 删除

+ 一对一和一对多都是直接delete(删除主表数据会通过级联删除自动删除从表数据)

  ```python
  models.Author.objects.get(id=1).delete()
  ```

+ 多对多`book_obj = models.Book.objects.get(id=1)`

  + 删除

    ```python
    book_obj.authors.remove(3)
    book_obj.authors.remove(2,3)
    ```

  + 清空:`book_obj.authors.clear()`

  + 先清空再添加：`book_obj.authors.set(['4',])`

### 修改

+ 修改 update,一对多和一对一操作时和单表的是一样的（亦同插入数据）

  ```python
   models.Book.objects.filter(id=1).update(
          title='白洁新版',
          # publishs=models.Publish.objects.get(id=3),
          publishs_id=3
      )
  ```


### 查询

#### 基于对象的跨表查询

+ 一对一

  + 正向查询（从表--->主表）

    ```python
    author_obj = models.Author.objects.get(name='金龙2')
    author_obj.author_detail#从表记录.外键属性拿到对应主表的记录对象
    author_obj.author_detail.addr
    ```

  + 反向查询（主表--->从表）

    ```python
    authordetail_obj = models.AuthorDetail.objects.filter(telephone__startswith='151').first()#从主表拿到一条记录
    print(authordetail_obj.author.name)#主表.小写从表类名取取对应值（仅一条）
    ```

+ 一对多

  + 正向查询

    ```python
     book_obj = models.Book.objects.filter(title='白洁新版').first()
    print(book_obj.publishs.name)#通过对象.外键属性拿到主表对应的值
    ```

  + 反向查询

    ```python
    pub_obj = models.Publish.objects.get(name='东京出版社')
    books = pub_obj.book_set.all().values('title')#默认会查到多个对象queryset对象
    ```

+ 多对多（均同一对多）

  + 正向查询

    ```python
    book_obj = models.Book.objects.filter(title='白洁新版').first()
    authors = book_obj.authors.all().values('name')
    print(authors)
    ```

  + 反向查询

    ```
    jinlong2_obj = models.Author.objects.get(name='金龙2')
    ret = jinlong2_obj.book_set.all().values('title')
    print(ret)
    ```