## 类之间的关系

+ 类之间的关系要做到 **高内聚**（封装），**低耦合**（有必要的时候才建立联系）

+ 依赖关系（关联）

  + 使用其他类的方法实现自己的功能（在某个方法中调用其他类的方法或属性）
  + 将一个类的对象或者类名传到另一个类的方法使用
  + 此时关系是最轻的，随时可以更换其他对象（因为使用的是其他类创建的对象，所以方便更换）

  ```
  定义一个英雄类和一个反派类
  • 两个类都包含名字、血量，攻击力（ATK），和一个技能（skill）
  • 两派对象互殴
  • 血量为0死亡，删除对象（del 对象名）
  
  class Heros:
      def __init__(self,name,hp,mp,ATK):
          self.name = name
          self.hp = hp
          self.mp = mp
          self.ATK = ATK
  
      def skill(self,tools):
          tools.hp -= self.ATK
          self.mp -= 10
          print(f"{self.name} 攻击 {tools.name} 造成{self.ATK}点伤害-{self.name}当前HP:{self.hp} {tools.name}当前HP:{tools.hp}")
  
  class Enemys:
      def __init__(self, name, hp, mp, ATK):
          self.name = name
          self.hp = hp
          self.mp = mp
          self.ATK = ATK
  
      def skill(self, tools):
          tools.hp -= self.ATK
          self.mp -= 10
          print(f"{self.name} 攻击 {tools.name} 造成{self.ATK}点伤害-{self.name}当前HP:{self.hp} {tools.name}当前HP:{tools.hp}")
  
  mingRen = Heros("鸣人",1000,1000,100)
  zuoZhu = Enemys("佐助",800,500,124)
  a = mingRen
  b = zuoZhu
  while True:
      a, b = b, a
      a.skill(b)
      if mingRen.hp <= 0:
          print(f"{mingRen.name}死了")
          del mingRen
          break
      elif zuoZhu.hp <= 0:
          print(f"{zuoZhu.name}死了")
          del zuoZhu
          break
  
  try:
      print(mingRen.name)
  except NameError:
      print("鸣人已经死了")
  
  try:
      print(zuoZhu.name)
  except NameError:
      print("佐助已经死了")
  ```

+ 组合关系（聚合）

  + 使用多个类

  + 在对象里面包含对象

  + 将一个类的对象封装到另一个类的对象的属性中（私有属性）

    ```
    class Person:
        def __init__(self,friend):
            self.friend = friend
    
    class Women:
        def __init__(self):
            self.name = "xiaoli"
    
    xiaoli = Women()
    xiaoming = Person(xiaoli)
    print(xiaoming.friend.name) #xiaoli
    ```

  + 一对一关系(使用一个其他类的实例对象)

    ```
    class BigB:
        def __init__(self,name,friend = None):
            self.name = name
            self.friend = friend
    
        def eat(self):
            if self.friend:
                print(f"{self.name}带着{self.friend.name}去吃饭")
            else:
                print("吃狗粮")
    
    class Girl:
        def __init__(self,name):
            self.name = name
    
    xiaoli = Girl("唐艺昕")
    baoyuan = BigB("宝元",xiaoli)
    baoyuan2 = BigB("宝元")
    baoyuan.eat() #宝元带着唐艺昕去吃饭
    baoyuan2.eat() #吃狗粮
    ```

  + 一对多关系(使用多个其他类的实例对象)

    ```
    class Boy:
        def __init__(self):
            self.girl_list = []
    
        def baMei(self,girl):
            self.girl_list.append(girl)
    
        def happy(self):
            for i in self.girl_list:
                i.play()
    
    class Girl:
        def __init__(self, name):
            self.name = name
    
        def play(self):
            print(f"{self.name}和你一起玩")
    
    bao = Boy()
    friend1 = Girl("张三")
    friend2 = Girl("李四")
    friend3 = Girl("王五")
    bao.baMei(friend1)
    bao.baMei(friend2)
    bao.baMei(friend3)
    bao.happy()
    ```

+ 继承关系（）