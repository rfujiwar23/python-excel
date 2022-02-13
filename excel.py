import openpyxl as excel
book = excel.Workbook()
sheet = book.active
sheet["A1"] = "Hello, My Name is Ryo"
book.save("hello.xlsx")