import openpyxl

#創建一個新的Excel工作簿
workbook = openpyxl.Workbook()  #workbook = Workbook()
sheet = workbook.active

#設置標題行
sheet['A1'] = 'Product Name'        #sheet['A1] = 'Product Name'
sheet['B1'] = 'Sale Price'          #sheet['B1'] = 'Sale Price'
sheet['C1'] = 'Quantitiy Sold'     #sheet['C1'] = 'Quantitiy Sold'

#添加數據
data = [
    ['Widget A', 25.5, 100],
    ['Widget B', 15.75, 200],
    ['Widget C', 30.0, 150],
    ['Widget D', 10.0, 300]
]

#把矩陣後面的資料夾在first row後面
for row in data:                    #將data中的每一行數據逐行添加到Excel工作表中
    sheet.append(row)
    #print(row)                   #把row輸出

#保存工作簿
workbook.save('example.xlsx')       #workbook.save('example.xlsx')

