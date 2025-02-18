from openpyxl import load_workbook

#載入現有的Excel文件
workbook = load_workbook('example.xlsx')
sheet = workbook.active

#修改特定單元的數據
sheet['B2'] = 27.00     #將Widget A的價格從25.5改為27.00

#保存修改後的工作簿
workbook.save('example_modified_openpyxl.xlsx')