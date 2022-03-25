import csv
path = r'C:\Users\admin\PycharmProjects\practice\files_directory\csv_files\employees.csv'
#using reader
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     for row in read_obj:
#         print(row)

#wap to print salary > 75000
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if int(row[3]) > 75000:
#             print(row[0])

from collections import defaultdict
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         dd[row[1]] += [row[0]]
#     print(dd)

#group employee based on team
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         dd[row[2]] += [row[0]]
#     print(dd)

