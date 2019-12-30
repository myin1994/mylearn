import xlrd
book = xlrd.open_workbook('test.xlsx')
sheet1 = book.sheets()[0]
rows = sheet1.nrows
cols = sheet1.ncols
title = sheet1.row_values(0)
print(title)
#将每行都和首行组成字典，存放在一个列表中
# l = []
# for row in range(1,rows):
#     l.append(dict(zip(title,sheet1.row_values(row))))
#
# print(l)
# lst = [dict(zip(title,sheet1.row_values(row))) for row in range(1,rows)]
# print(lst)
for i in sheet1.row_values:
    print(i)
