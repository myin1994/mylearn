## Numpy应用案例 

### 图像的读取和显示

+ 导入  matplotlib.pyplot

  ```
  import matplotlib.pyplot as plt
  ```

+ plt.imread:读取图像，返回图像的数组

  + imread方法默认只能出路png格式的图像，如果要处理其他格式的图片，需要安装pillow库
  + 图像可以有两种表示方式
    + 一种是使用无符号的np.uint8，取值为0-255
    + 一种是使用float类型表示，取值为0.0-1.0
    + 其中float的0.0对应整数类型的0,1.0对应255

  ```python
  a = plt.imread('1.jpg')
  print(type(a))#<class 'numpy.ndarray'>
  print(a.shape)#(500, 500, 3)对应像素（高度，宽度 ）及通道数（RGB）
  ```

+ plt.imshow:显示图像（传递表示图像的ndarry数组对象）

  ```python
  plt.imshow(a)
  ```

+ plt.imsave:保存图像

  ```python
  plt.imsave('2.jpg',a)
  ```

  <img src='.\04 Numpy应用案例.assets\image-20191226134322204.png'>

### 显示纯色图像

+ 显示白色图像

  即对应元素均为1.0或255

  ```
  plt.imshow((a*0+1)*255)
  
  x = np.ones((100,100,3))
  plt.imshow(x)
  
  x = np.full((100,100,3),255,dtype=np.uint8)
  plt.imshow(x)
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226135319855.png">

+ 显示黑色图像

  即对应元素均为0

  ```
  plt.imshow(a*0)
  
  x = np.zeros((100,100,3))
  plt.imshow(x)
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226135358844.png">

+ 显示指定颜色图像

  使用切片的方法来指定固定颜色
  
  ```
  #绿色	0 255 0
  x = (a*0+1)*255
  y = np.array([0,255,0])
  plt.imshow(x*y)
  #(228,238,249)
  x = np.full((100,100,3),1,dtype=np.uint8)
  y = np.array([228,238,249])
  
  plt.imshow(x*y)
  --------------------------
  
  x = np.full((100,100,3),1,dtype=np.uint8)
  #x[:] = [228,238,249]
  x[:,:] = [228,238,249]
  plt.imshow(x)
  ```

<img src=".\04 Numpy应用案例.assets\image-20191226140516582.png">

### 转换为灰度图

灰度图的数据可以看成是二维数组，元素取值为0 ~ 255，其中，0为黑色，255为白色。从0到255逐渐由暗色变为亮色。

+ 灰度图转换（ITU-R 601-2亮度变换）：L = R * 299 / 1000 + G * 587 / 1000 + B * 114 / 1000，R,G,B为最低维的数据。
+ 显示灰度图时，需要在imshow中使用参数：`cmap="gray"`

```python
x = a
y = np.array([0.299,0.574,0.114])
plt.imshow(np.dot(x,y),cmap="gray")
----------------
plt.imshow(np.dot(a,[0.299,0.574,0.114]),cmap="gray")
```

<img src=".\04 Numpy应用案例.assets\image-20191226141747623.png">

### 灰度图（2）

以上转换为标准的公式，我们也可以采用不正规的方式：

- 使用最大值代替整个最低维

  ```
  plt.imshow(np.max(a,axis=2),cmap="gray")
  ```

- 使用最小值代替整个最低维

  ```
  plt.imshow(np.min(a,axis=2),cmap="gray")
  ```

- 使用平均值代替整个最低维

  ```
  plt.imshow(np.mean(a,axis=2),cmap="gray")
  ```

- 放在一起进行展示

  ```python
  fig, ax = plt.subplots(2,2)
  fig.set_size_inches(10,10)
  ax[0,0].imshow(np.dot(a,[0.299,0.574,0.114]),cmap="gray")
  ax[0,1].imshow(np.max(a,axis=2),cmap="gray")
  ax[1,0].imshow(np.min(a,axis=2),cmap="gray")
  ax[1,1].imshow(np.mean(a,axis=2),cmap="gray")
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226143111893.png">

### 图像颜色通道

对于彩色图像，可以认为是由RGB三个通道构成的。每个最低维就是一个通道。分别提取R，G，B三个通道，并显示单通道的图像。

+ RGB图像可以认为是R,G,B三个通道构成（3张胶片叠加在一起显示的）

+ 如果要提取某一个通道，就是让其他通道的值全是0

  ```python
  b = a.copy()
  b[:,:,1:3]=0#R
  c = a.copy()
  #c[:,:,0:3:2]=0#G
  c[:,:,[0,2]] = 0
  d = a.copy()
  d[:,:,0:2]=0#B
  fig, ax = plt.subplots(2,2)
  fig.set_size_inches(10,10)
  ax[0,0].imshow(b)
  ax[0,1].imshow(c)
  ax[1,0].imshow(d)
  ax[1,1].imshow(b+c+d)#叠加
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226153435680.png">

### 图像重复

​	只需要让数组的元素重复就可以（数组拼接）

- 将图像沿着水平方向重复三次。

  ```python
  plt.imshow(np.hstack((a,a,a)))
  plt.imshow(np.concatenate((a,a,a),axis=1))
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226153900651.png">

- 将图像沿着垂直方向重复两次。

  ```python
  plt.imshow(np.vstack((a,a,a)))
  plt.imshow(np.concatenate((a,a,a),axis=0))
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226153938452.png">

- 将图像沿着水平方向重复两次，垂直重复三次。

  ```python
  b = np.hstack((a,a))
  plt.imshow(np.vstack((b,b,b)))
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226154027460.png">

### 图像镜面对称

- 将图像水平镜面转换。(竖直方向-二维度)

  行保持不变，列进行颠倒

  ```python
  b = a.copy()
  plt.imshow(b[:,-1::-1])
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226162426093.png">

- 将图像垂直镜面转换。（第一维度）

  列保持不动，行进行颠倒

  ```python
  b = a.copy()
  plt.imshow(b[-1::-1])
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226162546537.png">

### 左右旋转

- 将图像向左旋转90 / 180度。

  - 将图像先转置，然后进行垂直方向的颠倒----左转90°

    ```python
    plt.imshow(a.transpose((1,0,2))[-1::-1])
    ```

  - 先进行水平镜像，再进行转置----左转90°

    ```python
    b = a.copy()
    plt.imshow(b[:,::-1].swapaxes(0,1))
    ```

  <img src=".\04 Numpy应用案例.assets\image-20191226165909349.png">

- 将图像向右旋转90 / 180度。

  - 将图像先转置，然后进行水平方向的颠倒----右转90°

  - 先进行竖直方镜像，再转置----右转90°

    ```python
    b = a.copy()
    plt.imshow(b[::-1].swapaxes(0,1))
    ```

- 两次镜像(水平，竖直)旋转180°

  ```python
  plt.imshow(b[::-1][:,::-1])
  plt.imshow(b[:,::-1][::-1])
  ```

```python
fig, ax = plt.subplots(2,2)
fig.set_size_inches(10,10)
ax[0,0].imshow(a.swapaxes(0,1)[::-1])#左
ax[0,1].imshow(a.swapaxes(0,1)[::-1].swapaxes(0,1)[::-1])#180
ax[1,0].imshow(a.swapaxes(0,1)[:,::-1])#右
ax[1,1].imshow(a.swapaxes(0,1)[:,::-1].swapaxes(0,1)[:,::-1])#180
```

<img src=".\04 Numpy应用案例.assets\image-20191226170755451.png">

### 颜色转换

在图像中，用绿色值代替以前的红色值，用蓝色值代替以前的绿色值，用红色值代替以前的蓝色值。

```python
plt.imshow(a[:,:,[1,2,0]])
```

<img src=".\04 Numpy应用案例.assets\image-20191226174753437.png">

### 颜色遮挡 / 叠加

- 在指定的区域使用特定的纯色去遮挡图像。

  ```python
  b = a.copy()
  b[600:800,550:800] = [0,255,0]
  plt.imshow(b)
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226175332854.png">

- 在指定的区域使用随机生成的图像去遮挡图像。

  ```python
  b = a.copy()
  x = np.random.randint(0,255,(200,200,3))
  b[600:800,550:750] = x
  plt.imshow(b)
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226175759811.png">

- 使用小图像放在大图像上。

  ```python
  b = a.copy()
  c = a.copy()[200:400,1000:1500]
  b[200:400,100:600] = c
  plt.imshow(b)
  ```

  <img src=".\04 Numpy应用案例.assets\image-20191226180039607.png">

### 图像分块乱序

将图像分成若干块子图像（例如10 * 10），然后打乱各子图像顺序（拼图）。

```python
splites = np.split(a,10,axis=0)
random.shuffle(splites)
plt.imshow(np.vstack(splites))
```

<img src=".\04 Numpy应用案例.assets\image-20191226190626254.png">

```
splites = np.split(a,10,axis=0)
random.shuffle(splites)
b = np.vstack(splites)
splites = np.split(b,10,axis=1)
random.shuffle(splites)
c = np.hstack(splites)
plt.imshow(c)
```

<img src=".\04 Numpy应用案例.assets\image-20191226190834374.png">

```python
splites = np.split(a,range(100,1080,100),axis=0)#指定序列
random.shuffle(splites)
plt.imshow(np.vstack(splites))
```

<img src=".\04 Numpy应用案例.assets\image-20191226191244940.png">