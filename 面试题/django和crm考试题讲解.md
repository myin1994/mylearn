## Python面试重点（web篇）

### 第一部分 必答题

**注意：除第四题4分以外，其他题均每题3分。**

1. 写出常用的bootstrap的样式。

   1. form-control(input,select),  table(table table-striped table-hover,table-border )
   2. class='row'  col-md-3  col-md-offset-3
   3. btn btn-primary  btn-success  btn-danger...

2. 什么是响应式布局？(针对不同的设备屏幕宽度,来显示不同效果)

   1. cnblogs.com/clschao/articles/10093308.html 参考博客  

3. 请通过jQuery发送ajax请求。

   ```
   var formdata = new FormData()
   formdata.append('file_obj',$('[type=file]')[0].files[0])
   $.ajax({
           url:'/home/',
           type:'get',
           // data:{username:'alexdsb'},
           data:formdata,
           processData:false,
           contentType:false,
           success:function (res) {
               alert(res);
           }
   		
   
       });
       
   ```

   

4. JavaScript与this相关的面试题（4分）

   ```javascript
   name = '老男孩';
   
   info = {
   	name:'alex',
   	age:123,
   	func:function(){
   		console.log(this.name);
   	}
   }
   
   info.func() 
   ```

   ```javascript
   name = '老男孩'; // 3.this.name 实际上就是window.name,所以打印了老男孩
   
   info = {
   	name:'alex',
   	age:123,
   	func:function(){
   		console.log(this.name); //alex
           function f1(){
               console.log(this.name);  //2.所以这里this指向了window对象
           }
           f1()  #1.实际上是window.f1(),
   	}
   }
   
   info.func() 
   ```

   ```javascript
   name = '老男孩';
   
   info = {
   	name:'alex',
   	age:123,
   	func:function(){
   		console.log(this.name);
           (function(){
               console.log(this.name);
           })() // 自执行函数中这个this也是指向了window对象
   	}
   }
   
   info.func() 
   ```

   ```javascript
   name = '老男孩';
   
   info = {
   	name:'alex',
   	age:123,
   	func:function(){
   		console.log(this.name);   //alex
           var xxx = this;  // this---info对象
           (function(){
               console.log(xxx.name);  // info.name
           })()
   	}
   }
   
   
   xx = '小浩';
   
   let a = {
     xx:'张宇',
     //func:function(){}
     //func(){} //单体模式
     //data(){}
     //data:function(){}
     func:()=>{
       console.log(this.xx)
     }
   };
   a.func()
   ```

6. 什么是跨域？如何解决？ 

   1. 协议\ip\端口三个都相同才是同源,跨域就是两个项目中前面这三项内容有一个不同,就是非同源,那么他们之间互相访问就是跨域
   2. 响应对象加上对应的响应头就可以了,比如说对于一个简单请求,被请求的网站,回复响应对象的时候加上obj["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000" 就可以了

7. 简述你对Http协议的理解？

7. 简述你对Https协议的理解？

   SSL\TLS  安全协议

   对称加密和非对称加密

   非对称加密：公私钥RSA

   

   

   

8. 列举常见的http请求头及作用？

9. 列举常见的http请求方法及作用？

10. 列举常见的http响应状态码。

11. http中`connections：keep-alive`的请求头的作用？

12. django请求生命周期？

    1. https://img2018.cnblogs.com/blog/988061/201903/988061-20190307152249812-1922952163.png

       

13. 什么是wsgi？

    1. web服务器网关接口 ,应用程序与服务器程序(socket)之间交互数据的格式要求,django内部使用的wsigref来完成这个接口,实际我们部署项目使用的是uwsgi,因为wsgiref不支持并发,uwsgi支持并发.

14. 什么是MVC ？什么是MTV？

    1. MVC:model-view-control(url)      MTV:model-template-views+url控制器  框架模式

15. django中间件作用以及应用场景？

    1. 对全局请求或者响应做出一些相关处理  (登录认证\权限认证\限制访问批量\ip过滤)

16. django中FBV和CBV有什么区别？

    1. function based view    class based view

    2. fbv--url:  url("^index/',views.函数名称')       cbv: url("^index/',views.类名.as_view()')

    3. cbv里面针对不同的请求方法写对应逻辑时的不同

       1. fbv:  request.method来进行请求方法的判断

       2. cbv:get请求想处理就定义get方法

          1. cbv里面: dispatch--进行请求方法分发到不同的类方法上的处理,原理:反射  request_method_list = ['get','post'....],   getattr(self,'get')

          2. class xx(VIew): -- getattr('get',xx) 
          
          3. get()
          
              

17. django orm中如何批量创建数据？

    1. 对象 = models.Book(title='金瓶梅')
    2. models.Book.objects.bulk_create([model对象1,对象2])

18. django 如何执行原生SQL？

    1. models.Book.objects.raw('select * from app01_book;')

    2. 借用到pymysql,

       1. from django.db import connection

           connection  ----  conn = pymysql(host=127.0.0.1,port=3306,........)

          cursor = connection  .cursors()

          cursor.excute('select * from xx;')

          cursor.fetchall()

19. django的orm如何查询id不等于5的数据。

    1. models.Book.objects.exclude(id=5)
    2. models.Book.objects.all().filter().exclude(id=5)

20. cookie和session的区别？

    1. cookie:保存在浏览器端的数据
    2. session是将数据保存在了服务端,但是借助了cookie,session_id给了cookie,用户带着个session_id就能获取到自己的数据,更安全一些
    3. cookie有个数限制: 300个
    4. 一个服务器最多在客户端浏览器上保存20个Cookie； 
    5. Cookie大小上限为4KB；

21. django的orm中on_delete的作用？

    1. on_delete级联删除,on_delete=CASCADE,  on_delete=SET_NULL 关联数据置空
    2. models.Foreignkey(on_delete=CASCADE) -- on delete cascade   -

22. 描述crm有哪些功能？

    1. 注册登录

    2. 批量操作  bulk_create()   --  modelformset_factory

    3. 模糊搜索  -- Q  

    4. 公私户转换(事务和锁)     transaction  atomic():

    5. ​                                               models.Customer.objects.select_for_update().fitler()

    6. 分页(自定义分页组件)

    7. 各业务数据的增删改查(orm操作,modelform,form)

    8. 批量创建记录和修改记录(modelformset_factory)  models.Foreignkey(to='self')

    9. 权限组件开发

       1. 数据库表设计(6张表,4个model类)  一级菜单（菜单动态效果）  用户表 --多对多--  角色表 --多对多-- 权限表
       2. 权限对应url路径,基于rbac,也就是基于角色进行了权限控制
       3. 权限分配
          1. 权限数据批量生成(modelformset_factory,和formset_factory,),首先获取项目中各个应用的url路径,递归 import_string(),然后和数据库中保存的url权限数据进行比较(set集合),项目中比数据库中多的,就是我们要添加的权限数据,少的就是剔除的一些功能,
          2. 给用户分角色,给角色分权限  

          4. 权限注入(数据库查询改用户的所有权限数据,然后讲这些数据注入到session中,session可以配置缓存,各个位置存取数据都很方便,而且数据是加密的)

          5. 权限校验(中间件,权限认证白名单,通过正则来校验该用户当前访问的路径有没有在他的所有权限路径中)

          6. 动态菜单(二级菜单)(做了菜单数据结构,注入到session中,通过inclusion_tag渲染每个用户不同的菜单标签)

          7. 路径导航-面包屑(定义了一个面包屑列表,将用户访问的路径所对应的二级菜单信息和一级菜单信息,加到了这个列表中,并将列表封装到了request对象里面,在前端进行了模板渲染,循环生成了路径导航)

          8. 精确到按钮级别的权限

             class Book():

             ​	authors = models.ManyToMany('author')

                def get_all_author_name(self):

             ​		name= ''

             ​      for i in self.authors.all()

             ​           name+= i.name

             ​     return name

23. crm中什么是公户？什么是私户？为什么要做这个区分？

    1. 没有分配给任何一个销售的客户,都称为公户,已经分配了的就是某个销售的私户
    2. 销售容易产生矛盾,提高销售的服务质量,提高转化率,并且可以进行销售的业绩统计

24. 请列举出CRM系统中的表。

    1. 用户表,客户表,跟进记录表,报名表,课程表,学习记录表,权限表....

25. 对数据库的数据做展示时，不同字段类型有不同的展示方法，分别是什么？

    1. models.CharField(choices=[('1','男'),]) -- get_字段名_display   对象.属性     对象.属性.另外一张表的属性   
    2. 对象.属性.all()   

26. 请详细说说你们公司销售是如何使用CRM的。 

    1. 登录
    2. 查看公户信息,选取自己想聊的客户,拉到自己的私户中
    3. 然后对客户进行一对一深入交流
    4. 将每次交流体验记录到跟进记录中
    5. 也负责帮助客户写报名信息
    6. 然后缴费成功之后,进行售后服务

27. CRM中有哪些技术点？

    1. 技术栈:  django\modelformset_factory\jquery\bootstrap\ajax\html\css\mysql\orm\nginx\uwsig

28. 为什么不用现成的crm而是自己去开发？

    1. 公司业务定制性很强,现成的crm不能够满足需求

29. 请简述实现权限控制的流程。

    1. 

30. 列举权限有多少张表？表中都有那些字段？ 

31. 为什么要把权限信息放到session中？权限信息放到session有什么优点？ 

32. 权限控制到按钮级别是如何实现的？

33. 如何实现把权限粒度控制到数据行？    添加一条件表,记录着数据表名,查询条件(id>2)

销售A：查询公户信息  



tablex

表名    查询条件   角色

customer   id>5    销售





### 第二部分 补充题

1. 详细描述是jsonp实现机制？   跨域  cors其实jsonp  json+padding

2. django的orm如何通过数据自动化生成models类？  inspectdb

3. django中如何设置缓存？

4. django中信号的作用？

5. django中如何设置读写分离



orm性能相关

```python

1 能用values的尽量不用对象.的形式来获取数据
    students = models.Student.objects.all().values('classes__name') #链表查询，查询一次 queryset[{'classes__name':'27期'},{'classes__name':'27期'},{'classes__name':'27期'}]
    for s in students:
        # print(s.classes.name)  #查询多次，每次点都进行一次sql查询，效率低
        print(s['classes__name'])  

        
2 通过select_related直接进行连表查询  针对一对一和一对多
    students = models.Student.objects.all().select_related('classes')
    for s in students:
        print(s.classes.name)

3 通过prefetch_related子查询来完成
    students = models.Student.objects.all().prefetch_related('classes')
    for s in students:
        print(s.classes.name)
        
4 only和defer

		当我们进行orm查询的时候，你通过翻译出来的sql语句可以看到，每次查询都是查询了每个字段的数据，所以我们通过only和defer，可以指定查询哪些字段数据
    all_students = models.Student.objects.all().only('name')#只要这个字段数据
    all_students = models.Student.objects.all().defer('name')#排除，除了这个字段其他字段数据都要
```

