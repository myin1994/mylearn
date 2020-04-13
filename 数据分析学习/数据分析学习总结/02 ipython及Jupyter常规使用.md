## Ipython

IPython(Interactive Python),是一款增强型Python解释器，在Python的基础上，提供了很多额外的功能。IPython可以使用如下命令安装：
`pip install ipython`
Anaconda集成了IPython解释器，只需在控制台上输入ipython即可启动IPython。

### 查看帮助

+ ?
+ ??

### 命令补全

+ Tab

### 魔法命令

+ 分类

  魔法命令分为%与%%两种形式，即在相应的命令前使用%或%%前缀。**但并非所有的魔法命令都支持这两种形式。**

  + % 行模式
  + %% 单元格模式

+ 常用魔法命令

  + lsmagic 

    显示所有可用的魔法命令

    <img src="./asserts/image-20191223084711120.png">

  + run

    运行外部python文件，运行结束后，外部文件中定义的名称会得到保留。格式为%run文件路径。

    + 相当于在当前的ipython解释器上执行（理解为复制到当前环境执行）
    + 外部文件中的对象可继续使用

    ```python
    #test.py
    %run C:\xxx\test.py
    a = 1
    b = 2
    def func():
        print(a)
        return b
    ```

    <img src='./asserts/image-20191223085558240.png'>

  + who

    + 显示当前自定义的变量，方法等名称，不会显示IPython解释器内建的名称。
    + 当指定类型列表时，仅类型匹配类型列表中的名称才会显示。
    + 以对象为单位（函数内部的变量不会显示）

    ![image-20191223090349134](.\asserts\image-20191223090349134.png)

  + whos

    + 与who类似，但是会显示当前名称的详细信息。

    ![image-20191223090550135](.\asserts\image-20191223090550135.png)

  + time

    执行语句计时功能。语句只执行一次。计算总消耗时间

    ![image-20191223090925182](.\asserts\image-20191223090925182.png)

  + timeit

    虽然time能够执行计时功能，但是如果语句过于简单，很可能计时结果为0。此时，我们可以使用循环多次执行。但更方便的方式是，使用timeit来完成多次执行的操作。

    + timeit支持行模式与单元格模式。
    + 在单元格模式下，第一行语句（与魔法命令在同一行的语句）为设置（初始化）语句，作用是可以用来定义变量供后续的代码使用。设置语句会执行，但是不参与计时。第二行至整个单元格末尾的语句会执行并参与计时。
      + n来指定每轮测试执行的次数（默认会选择最佳的次数）
      + -r指定执行的测试轮数（默认为7）。
    + timeit的单元格中，如果需要对外面的变量进行修改，需要使用global。

    ![image-20191223091332513](.\asserts\image-20191223091332513.png)

  + automagic

    + automagic命令用来设置在使用魔法命令时，是否需要使用%前缀。默认情况下，automagic是开启的，使用魔法命令可以不用使用%前缀。每次执行automagic命令时，就会切换开启 / 关闭状态。其行为类似于toggle button。
    + 当automagic处于开启状态，如果我们定义了与魔法命令相同名称的变量（或方法，类）时，访问的将是我们自定义的名称。为了避免不必要的混淆，建议在使用魔法命令时，总是使用%前缀。

  + history

    显示IPython的命令执行历史记录。

  + writefile（file）

    + 格式： %%writefile [-a] filename
    + 将单元格的内容写入到文件中。如果文件不存在则创建，如果文件存在，则覆盖文件。如果指定-a选项，则追加内容（不覆盖）。
    + writefile以前命名为file，为了兼容，file命令依然还能够使用。

  + prun

    通过Python的代码分析器，来分析程序（语句）的执行时间。结果会根据total time（花费时间）进行倒序排列。通过prun分析功能，我们就可以发现程序中最耗时的部分，进而可以针对性的进行优化。

    + ncalls 函数调用次数。
    + tottime 总共调用消耗的时间（不包括子函数调用消耗的时间）。
    + percall 每次调用消耗的时间。
    + cumtime 总共调用消耗的时间（包括子函数调用消耗的时间）。
    + percall 每次调用消耗的时间。
    + filename:lineno(function) 文件名：行号（函数名）

    ![image-20191223093404334](.\asserts\image-20191223093404334.png)

  + lprun

    + lprun不是IPython内置的，需要安装line_profiler模块。
    + 安装后，需要通过%load_ext line_profiler载入，才能使用。
    + lprun可以逐行对程序进行分析，相对与prun的函数分析，会更加细致。
    + 格式：%lprun -f 函数1 [-f 函数2， ……] <执行语句>
    + 其中-f指定执行时要分析的函数。分析结果列如下：
      + Timer unit 执行单位
      + Line # 行号。
      + Hits 执行次数。
      + Time 总共消耗时间。
      + Per Hit 单次执行消耗的时间。
      + % Time 消耗的时间百分比。
      + Line Contents 行内容。

    ![image-20191223100005648](.\asserts\image-20191223100005648.png)

  + memit

    + 分析语句的内存使用情况。
    + memit支持行模式与单元格模式。
    + 在单元格模式下，第一行语句（与魔法命令在同一行的语句）为设置（初始化）语句，作用是可以用来定义变量供后续的代码使用。设置语句会执行，但不参与计算内存使用。第二行至整个单元格末尾的语句会参与计算内存。
    + memit不是IPython内置的，需要安装memory_profiler模块。
    + 安装后，需要通过%load_ext memory_profiler载入，才能使用。

    ![image-20191223101057865](.\asserts\image-20191223101057865.png)

    ​	![image-20191223101627945](.\asserts\image-20191223101627945.png)

  + mprun

    + 格式：%mprun -f 分析函数1 -f 分析函数2 ……启动语句

    + 逐行分析语句的内存使用情况。分析结果列如下

      + Line # 行号。
      + Mem usage 内存使用大小。
      + Increment 内存增量。
      + Line Content 代码内容。

    + 说明

      + mprun不是IPython内置的，需要安装memory_profiler模块。

      + 安装后，需要通过%load_ext memory_profiler载入，才能使用。

      + mprun测试的函数必须定义在独立的模块中，不能定义在交互式环境中。

        ![image-20191223103019974](.\asserts\image-20191223103019974.png)

      + 如果需要重新加载模块，可以调用importlib模块提供的reload函数来实现。

        + ```
          import importlib
          importlib.reload(model)
          ```

        + 当前貌似不再需要，自动更新

## Jupyter

### 单元格

upyter notebook文档由一些列单元格组成，我们可以在单元格中输入相关的代码或者说明文字。单元格有以下几种类型

+ code 代码单元格，用来编写程序。
+ Markdown 支持Markdown语法的单元格，用来编写描述程序的文字。
+ Raw NBConvert 原生类型单元格，内容会原样显示。在使用NBConvert转换后才会显示成特殊的格式。
+ Heading 标题单元格，已经不在支持使用。

### 命令模式与编辑模式

jupyter notebook的单元格分为两种模式

+ 命令模式 单元格处于选中状态，此时单元格左侧为粗蓝色线条，其余为细灰色线条。
+ 编辑模式 单元格处于编辑状态，此时单元格左侧为粗绿色线条，其余为细绿色线条。（此时右上角会出现铅笔图标）

### 常用快捷键

可通过菜单Help -> Keyboard Shortcuts查看所有的快捷键。

+ 命令模式
  + Y 单元格转换成code类型。
  + M 单元格转换成Markdown类型。
  + R 单元格转换成Raw NBConvert类型。
  + Enter 进入编辑模式。
  + A 在当前单元格上方插入新单元格。
  + B 在当前单元格下方插入新单元格。
  + C 复制当前单元格。
  + D(两次）删除当前单元格。
  + V 粘贴到当前单元格的下方。
  + Shift + V 粘贴到当前单元格的上方。
  + Z 撤销删除。
+ 编辑模式
  + Tab 代码补全
  + Shift + Tab 显示doc文档信息。
  + Esc 进入命令模式。
+ 通用模式
  + Ctrl + Enter 运行单元格，然后该单元格处于命令模式。
  + Shift + Enter 运行单元格，并切换到下一个单元格，如果下方没有单元格，则会新建一个单元格。
  + Alt + Enter 运行单元格，并在下方新增一个单元格。