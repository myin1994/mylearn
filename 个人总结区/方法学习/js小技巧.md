+ 动态添加属性值

  ```javascript
  .attr({hidden:function(index, attr){
      return attr === 'hidden' ? null : 'hidden';
  }});
  ```

  