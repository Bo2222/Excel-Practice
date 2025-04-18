import pandas as pd 

#載入現有的Excel文件
df = pd.read_excel('example.xlsx')

#修改特定單元的值（假設'Product Name'在第一列，'Sale Price'在第二列）
df.loc[df['Product Name'] == 'Widget A', 'Sale Price'] = 27.00  #將Widget A的價格從25.5改為27.00
#pandas透過條件過濾快速找到並修改數據
#Pandas提供更高效和簡潔的數據操作方法，特別在處理大型數據集時

#保存修改後的DataFrame到Excel文件
df.to_excel('example_modified_pandas.xlsx', index=False)