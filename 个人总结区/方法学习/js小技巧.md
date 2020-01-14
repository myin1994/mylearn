+ 动态添加属性值

  ```javascript
  .attr({hidden:function(index, attr){
      return attr === 'hidden' ? null : 'hidden';
  }});
  ```

+ 前端md5加密（postman加密）

  ```javascript
  // 1. 处理手机号 
  phoneNum var myPhone = "18211101111"
  // 2. 操作码 
  optCode var myOptCode = 'testfan'
  // 3. 获取时间戳 
  var myTimeStamp = new Date().getTime();
  // 4. 将上面的3个变量拼接起来 
  var myData = myPhone + myOptCode + myTimeStamp;
  // 5. 使用md5加密 
  var mySign = CryptoJS.MD5(myData).toString(); 
  console.log(myOptCode, myTimeStamp, myData, mySign);
  // 6. 将相关变量添加到postman中 
  pm.environment.set("myPhone", myPhone); 
  pm.environment.set("myOptCode", myOptCode); 
  pm.environment.set("myTimeStamp", myTimeStamp);
  pm.environment.set("mySign", mySign)
  ```

  