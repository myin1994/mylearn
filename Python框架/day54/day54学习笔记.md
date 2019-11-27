##  AJAX 

+ 介绍

   *AJAX（Asynchronous Javascript And XML）*翻译成中文就是“异步的Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML,现在更多使用json数据）。 

+ 特性

  + 局部刷新
  + 异步请求

+ 实例（登录验证）

  + html

    ```html
    {% csrf_token %}
    <hr>
    用户名: <input type="text" id="login_name">
    密码: <input type="password" id="login_password">
    <button id="sub">提交</button>
    <h5 class="error" style="color: red"></h5>
    
    <script>
        $("#login_name,#login_password").focus(function () {
            $(".error").text("")
        });
        $("#sub").click(function () {
            var login_name = $("#login_name").val();
            var login_password = $("#login_password").val();
            $.ajax({
                url: "{% url 'app01:login' %}",
                type: "post",
                data: {
                    'login_name': login_name,
                    'login_password': login_password,
                    "csrfmiddlewaretoken": "{{ csrf_token }}"
                },#请求数据,不需要携带数据的请求,不需要写data参数
                # data数据部分的csrf_token认证的键值对的值直接写{{ csrf_token }} ,经过模板渲染之后,它直接就是那个input标签的value值
                {#"csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()},#}
                success: function (res) {
                    if (res === "error") {
                        $(".error").text("密码错误请重新登录")
                    } else {
                        location.href = "{% url 'app01:books' %}";
                    }
                }
            })
        })
    </script>
    <!--注意：外部引入js时不能进行渲染-->
    ```

## 基于form表单上传文件

+ form表单属性`enctype="multipart/form-data"`

+ html

  ```html
  html代码:  
      <form action="" method="post" enctype="multipart/form-data">
          {% csrf_token %}
          用户名:<input type="text" name="username">
          头像: <input type="file" name="file_obj">
          <input type="submit">
      </form>
  ```

+ views

  + `request.FILES`-----上传的文件数据

  ```python
  def upload(request):
  
      if request.method == 'GET':
  
          return render(request,'upload.html')
      else:
          print(request.POST)
          username = request.POST.get('user')
          file_obj = request.FILES.get('file_obj') #获得文件数据对象
          print('>>>',file_obj,type(file_obj))
          #>>> jaden博客.txt <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>,一个文件对象,可以理解为一个文件句柄
          file_name = file_obj.name #jaden博客.txt
          print(file_name)
          # 将数据写到文件里面,需要名字，需要数据
          with open(file_name,'wb') as f: #直接把文件名字放这里，那么文件将直接生成在django的整个项目目录下，因为django配置的系统搜索的根路径就是咱们的项目文件夹路径，那个BASE_DIR,一般我们需要自己建立一个文件夹专门存放上传的文件
  　　　　　　#所以需要我们自己来拼接一个路径放到这里，os.path.join(settings.BASE_DIR,'media','img',file_name)
  
              # f.write()  #不能一下写进去，占用的内容太多，要一点一点写
              for data in file_obj: #读数据
                  f.write(data)  #每次读取的data不是固定长度的，和读取其他文件一样，每次读一行，识别符为\r  \n  \r\n，遇到这几个符号就算是读了一行
  　　　　　　　#for chunks in file_obj.chunks(): #chunks()默认一次返回大小为经测试为65536B，也就是64KB，最大为2.5M，是一个生成器
      　　　　 #　 f.write(chunks)
  ```