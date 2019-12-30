## 相关模块

+ 对比

  + xlrd 用于读excel（xls/xlxs 格式）

  + xlwt 用于写excel（xls/xlxs 格式）

    不能写入超过65535行、256列的数据

  + oppenpyxl 可读可写（只支持 xlxs 格式的excel,）

  + xlrd/xlwt相较于openpyxl而言读写效率更高

### xlrd模块使用

+ 下载

  ```
  pip install xlrd
  ```

+ 获取excel对象

  ```python
  import xlrd
  
  # 首先拿到book对象
  book = xlrd.open_workbook('./a1.xlsx')
  ```

+ 取到Excel中的sheet(对象)

  + 通过索引：`sheet_by_index(0)`。

  + 通过sheet名称：`sheet_by_name('自动化')`。

  + 通过索引顺序获取：`sheets()[0]`

    ```
    # sheet_by_index = book.sheet_by_index(0)
    sheet_by_name = book.sheet_by_name('sheet1')
    sheet1 = book.sheets()0]
    ```

  + 获取所有工作表的名字：`sheet_names()`

    ```
    book.sheet_names()
    ```

  + 检查某个sheet是否导入完毕

    ```
    print(book.sheet_loaded('Sheet1'))#表名或索引
    ```

  + 获取sheet总数：`nsheets`

  

+ 获取sheet内的汇总数据

  + 表名：`sheet1.name`
  + 有效行数：`sheet1.nrows`
  + 有效列数：`sheet1.ncols`

+ 对行进行操作

  + 获取该行中所有的单元格对象组成的列表

    + row(rowx)/row_slice(rowx)-读取类型及数据

    + row_values(rowx, start_colx=0, end_colx=None)-可指定读取列数，返回列表

      ```python
      print(sheet1.row(0))
      print(sheet1.row_values(0,0,2))
      >>>
      [text:'title1', text:'title2', text:'title3', text:'title4', text:'title5', text:'title6', text:'title7', text:'title8']
      ['title1', 'title2']
      ```

  + row_types(rowx, start_colx=0, end_colx=None)返回由该行中所有单元格的数据类型组成的数组

+ 对列进行操作

  + 获取该列中所有的单元格对象组成的列表

    + col(colx)/col_slice(colx)-读取类型及数据

    + col_values(colx, start_colx=0, end_colx=None)-可指定读取行数，返回列表，若是合并单元格 首行显示值 其它为空

      ```python
      print(sheet1.col(0))
      print(sheet1.col_values(0,0,2))
      >>>
      [text:'title1', text:'value1', text:'value2', text:'value3', text:'value4', text:'value5', text:'value6', text:'value7', text:'value8', text:'value9', text:'value10']
      ['title1', 'value1']
      ```

  + col_types(colx, start_colx=0, end_colx=None)返回由该行中所有单元格的数据类型组成的列表

+ 对单元格进行操作

  + cell(rowx, colx)  - 返回单元格对象
  + cell_type(rowx, colx)  - 返回单元格中的数据类型
  + cell_value(rowx,colx)   -返回单元格中的数据

  ```python
  #取值
  print(table1.cell(1,2).value)
  print(table1.cell_value(1,2))
  print(table1.row(1)[2]).value
  print(table1.col(2)[1]).value
  #取类型
  print(table1.cell(1,2).ctype)
  print(table1.cell_type(1,2))
  print(table1.row(1)[2].ctype)
  ```

+ 常用技巧（0,0）转换成A1

  ```python
  print(xlrd.cellname(0,0))#A1
  print(xlrd.cellnameabs(0,0))#$A$1
  print(xlrd.colname(0))#A
  ```

+ 将每行都和首行组成字典，存放在一个列表中

  ```python
  rows = sheet1.nrows
  title = sheet1.row_values(0)
  lst = [dict(zip(title,sheet1.row_values(row))) for row in range(1,rows)]
  print(lst)
  ```

  

