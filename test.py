import openpyxl as pyxl
wb = pyxl.load_workbook("test.xlsx")
print(wb.sheetnames)