# 今日内容



## ajax上传文件

+ 传输的数据类型data：`var formdata = new FormData()`

+ html

  ```html
  {% csrf_token %}
  用户名ajax ：<input type="text" id="name">
  头像：<input type="file" id="file_obj">
  <input type="button" value="提交" id="btn">
  ```

+ js&ajax

  ```javascript
  <script>
      $("#btn").click(function () {
          var formdata = new FormData();
          var name = $("#name").val();
  
          //var file_obj = $("#file_obj").val();//拿到的是文件本地路径
          var file_obj = $("#file_obj")[0].files[0];//文件对象（files拿到的是所有文件对象）
          formdata.append("name",name);#将要发送的数据添加进消息体中
          formdata.append("file_obj",file_obj);
          formdata.append("csrfmiddlewaretoken",$("[name='csrfmiddlewaretoken']").val());
          $.ajax({
              url:"/ajaxupload/",
              type:"post",
              data:formdata,#固定
              processData:false,#固定设置
              contentType:false,#固定设置
              success:function (res) {
                      console.log(res)
                  }
          })
      })
  </script>
  ```

+ 后端处理：同form



## Django与Ajax之间的json通信

![img](https://images2018.cnblogs.com/blog/867021/201804/867021-20180407213606833-782897022.jpg) 

### 传递json字符串

+ Django----->Ajax（`d1 = {'name':'myname','age':18}`）

  + 方式1（字典和列表均可）

    + Django：先进行序列化，通过HttpResponse返回json字符串

      ```python
      d1_str = json.dumps(d1,ensure_ascii=False)
      return HttpResponse(d1_str)
      ```

    + Ajax:接收到的数据为json字符串，需要反序列化后使用

      ```javascript
      success:function (res) {
      var res_dic = JSON.parse(res);
      console.log(res_dic);#{name: "myname", age: 18}
      console.log(typeof res_dic);#object
      console.log(res);#{"name": "myname", "age": 18}
      console.log(typeof res);#string
      }
      ```

  + 方式2（在方式1的基础上）

    + Django：通过HttpResponse返回json字符串的同时指定消息格式`content_type="application/json"`

      ```python
      d1_str = json.dumps(d1,ensure_ascii=False)
      return HttpResponse(d1_str,content_type="application/json")
      ```

    + Ajax:接收到的数据为反序列化后的原始数据，可直接使用

      ```javascript
      success:function (res) {
      console.log(res);#{name: "myname", age: 18}
      console.log(typeof res);#object
      }
      ```

  + 方式3（通过JsonResponse）

    + Django：直接通过JsonResponse返回数据（其中列表需要加safe=False）

      ```python
      return JsonResponse(d1,safe=False)
      ```

    + Ajax:接收到的数据为反序列化后的原始数据，可直接使用

      ```javascript
      success:function (res) {
      console.log(res);#{name: "myname", age: 18}
      console.log(typeof res);#object
      }
      ```

+ Ajax----->Django

  + 方式1

    + Ajax:将数据通过`JSON.stringify(dic)`序列化后发送

      ```javascript
      dic1 = JSON.stringify(dic)
      ```

    + Django：通过loads反序列化，数据格式将保持一致

      ```python
      dic = request.POST.get("dic1")
      print(type(json.loads(dic)),json.loads(dic))
      #<class 'dict'> {'name': 'myname', 'age': 18}
      ```

  + 方式2：直接将字典或者列表本身发送，则字典转换为一个个键值对，且全部数据均被转换为字符串。

### JSON序列化datetime和decimal类型数据(构建 DateEncoder类)

+ 序列化datetime

  ```python
  import json
  import datetime
  
  class DateEncoder(json.JSONEncoder):
  
      def default(self, obj):
          if isinstance(obj, datetime.datetime):
              return obj.strftime("%Y-%m-%d %H:%M:%S")
          else:
              return json.JSONEncoder.default(self, obj)
  t = datetime.datetime.now()
  print(type(t))#<class 'datetime.datetime'>
  t1 = json.dumps(t,cls=DateEncoder)
  print(t1)#"2019-11-27 19:38:12"
  ```

+ 序列化decimal

  ```python
  import json
  import decimal
  
  class DecimalEncoder(json.JSONEncoder):
      def default(self, o):
          if isinstance(o, decimal.Decimal):
              return float(o)
          super(DecimalEncoder, self).default(o)
  ```

## SweetAlert插件

```javascript
$(".del-book-2").on("click", function () {   //对按钮添加事件
        var delbtn = $(this);
        swal({
                title: "你确定要删除吗？",
                text: "删除可就找不回来了哦！",
                type: "warning",
                showCancelButton: true,
                confirmButtonClass: "btn-danger",
                confirmButtonText: "删除",
                cancelButtonText: "取消",
                closeOnConfirm: false
            },
            function () {
                var deleteId = delbtn.parent().siblings('.hide').text();
                console.log(deleteId);
                $.ajax({
                    url: "/books/",
                    type: "post",
                    data: {"del_id": deleteId,
                    "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()},
                    success: function (data) {
                        if (data.status === 1) {
                            swal("删除成功!", "你可以准备跑路了！", "success");
                            //location.reload()
                            delbtn.parent().parent().remove();
                            var num_td = $(".number");
                            for(var i =0;i<num_td.length;i++){
                                num_td[i].innerText=i+1
                            }
                        } else {
                            swal("删除失败", "你可以再尝试一下！", "error")
                        }
                    }
                })
            });
    })
```