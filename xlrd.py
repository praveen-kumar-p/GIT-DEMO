import xlrd

path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
open = xlrd.open_workbook(path)
xl_sheet = open.sheet_by_name('marks_sheet')
data = xl_sheet.get_rows()
print(data)