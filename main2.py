import pandas as pd

#創建數據
data = {
    'Product Name': ['Widget A', 'Widget B', 'Widget C', 'Widget D'],
    'Sale Price': [25.50, 15.75, 30.00, 10.00],
    'Quantity Sold': [100, 200, 150, 300]
}

#創建DataFrame
df = pd.DataFrame(data)

#保存DataFrame到Excel文件
df.to_excel('example.xlsx', index=False)