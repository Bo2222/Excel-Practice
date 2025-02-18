import openpyxl

#讀取Excel工作簿
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active

#將數據存儲成二維陣列
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(list(row))

print(data)