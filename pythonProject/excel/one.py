import openpyxl
wb=openpyxl.load_workbook(r"C:\Users\10756\Desktop\人教版初中英语.xlsx")
print(type(wb))
print(wb.get_sheet_names())
sheet=wb.get_sheet_by_name('七年级上册-Starter Unit 1')
print(sheet.cell(row=5,column=2).value)
