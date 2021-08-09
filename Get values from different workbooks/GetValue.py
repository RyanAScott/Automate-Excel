import openpyxl

# specify the file's path
excel_files = ['/Users/ryanscott/Documents/Python Practice/Automate-Excel/SampleData.xlsx', '/Users/ryanscott/Documents/Python Practice/Automate-Excel/SampleData2.xlsx']

# create an empty list to append values later on
values = []

# loop through the files in the "excel_files" list
for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    # specify worksheet to select
    worksheet = workbook['SalesOrders']
    # locate cell and get its value
    cell_value = worksheet['G11'].value
    # append valie to "values" list
    values.append(cell_value)

    # print totals 
    print(cell_value)