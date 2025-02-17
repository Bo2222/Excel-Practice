import openpyxl

#創建一個新的Excel工作簿
workbook = openpyxl.Workbook()
sheet = workbook.active

#設置標題行
sheet['A1'] = 'Product Name'
sheet['B1'] = 'Sale Price'
sheet['C1'] = 'Quantitiy Price'

#添加數據
data = [
    ['Widget A', 25.50, 100]
    ['Widget B', 15.75, 200]
    ['Widget C', 30.00, 150]
    ['Widget D', 10.00, 300]
]

#把矩陣後面的資料夾在first row後面
for row in data:
    sheet.append(row)

#保存工作簿
workbook.save('example.xlst')