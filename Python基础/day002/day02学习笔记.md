## while

+ 关键字

+ 循环：不断的重复做某件事情

+ 先判断关键字后的条件，满足时执行，执行完最后一个语句返回继续判断，直到条件不成立

+ 理解逻辑

  + 死循环

    ```
    print("循环开始之前")
    while True: #死循环
        print("郭德纲")
        print("于谦")
        print("小岳岳")
        print("孙悦")
        print("五环之歌")
        print("鸡你太美")
        print("大面")
    print("造作")
    ```

  + 有限次数循环

    + break：终止当前循环

      ```
      count = 0
      while True:  #死循环
          print(111)
          count += 1  #先执行 = 右边的内容
          if count == 5:
              print(count)
              break #有限循环
      ```

    + continue：跳出本次循环继续下次循环（continue 就是伪装成循环体中最后一行代码）

      ```
      count = 0
      while True:  #死循环
          count += 1  #先执行 = 右边的内容
          if count == 5:
              print(111)
              continue
          print(count)
      ```

    + 注：continue 和 break 下方的代码都不会被执行

  + 通过条件控制循环次数

    + 计数器

      ```
      count = 0
      while count <2:
          print(count)
          count += 1
      ```

    + 练习题

      打印4-67

      ```
      count = 4
      while count <68:
          print(count)
          count += 1
      ```

      打印100-6

      ```
      count = 100
      while count >= 6:
          print(count)
          count -= 1
      ```

      打印1,3,5,7,9

      ```
      count = 1
      while count < 10:
          print(count)
          count += 2
      ```

  + while else:与if else相似，是一体的

    理解为while最后一次判断不满足条件时执行

    + 