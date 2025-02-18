import openpyxl

#讀取Excel工作簿
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active

#將數據存儲成二維陣列
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(list(row))

#print(data)

#顯示數據
for row in data:
    print(row)

#獲取特定列的最大值（假設'Sale Price'在第二列）
sale_prices = [row[1] for row in data[1:]] #跳過標題行(['Product Name', 'Sale Price', 'Quantitiy Sold'])
max_sale_price = max(sale_prices)           #透過實作演算法(搜尋)去獲取最大值
print(f'Max Sale Price is {max_sale_price}')
