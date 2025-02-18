import pandas as pd

#讀取Excel文件並轉換成DataFrame
df = pd.read_excel('example.xlsx')

#顯示DataFrame的內容
print(df)

#獲取某一列的最大值
max_value = df['Sale Price'].max()              #熊貓處理二維數據的專業可以快速獲取最大值
print(f'Max Sale Price is {max_value}')