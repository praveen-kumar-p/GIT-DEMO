import re
# s = 'hello world welcome to python hello'
# print(re.findall(r'.', s))
# print(re.findall(r'h.', s))
# print(re.findall(r'^hello', s))
#
# s = 'ana hello word axa'
# print(re.findall(r'a.a', s))
#
# print(re.findall(r'an*a', 'annnnnna'))

# print(re.findall(r'[^0-9]+', 'the cost of book is 100'))
# print(re.findall(r'[a-z]', 'the cost of book is 100'))

# print(re.findall(r'\D', 'the cost of book is $100'))

# s = 'Hello World Welcome To Python'
# u = len(re.findall(r'[A-Z]', s))
# l = len(re.findall(r'[a-z]', s))
# print(u, l)

# d = '''
#         downloading file archive.zip to downloads folder
#         downloading file image.jpeg to downloads folder
#         downloading file index.xhtml to downloads folder
#         downloading file python.py to downloads folder
#     '''
# print(re.findall(r'\.[a-zA-Z]+', d))

# s = 'hello hi american engineers and indian writers officers united states'
# l = s.split()
# print(re.findall(r'\b[aeiou]\w+', s))
# print(re.findall(r'\b[^aeiou]\w+', s))
# p = lambda item: item[0] in 'aeiou'
# m = filter(p, l)
# print(list(m))

# print(re.findall(r'.', 'hello world hello python 123'))

# print(re.findall(r'h.', 'hello world hello python 123'))

# print(re.findall(r'a.b', 'ambndm'))

# print(re.findall(r'^hello', 'hello world hello'))
# l = 'hello world hello'
# s = l.split()
# p = []
# for item in s:
#     if item[0] in 'h':
#         p.append(item)
# print(p)
# print(re.findall(r'hello$', 'hello world hello'))

# s = 'hi python welcome to andamana'
# print(re.findall(r'an*a', s))

# print(re.findall(r'^praveen kumar$', 'praveen kumar'))

# print(re.findall(r'an+a', 'annnnna'))

# print(re.findall(r'color', 'this is red color'))
# print(re.findall(r'colou?r', 'this is red colour'))
# print(re.findall(r'colou?r', 'this is red color'))

# res = (re.findall(r'[aeiou]', 'helo world weilcome to python'))
# print(len(res))

# s = 'hello 123 hi 53 python welcome 3628'
# print(re.findall(r'[0-9]', s))
# print(re.findall(r'[0-9]+', s))

# s = 'hello 123 hi 53 python welcome 3628'
# print(re.findall(r'[^0-9]', s))

# s = 'helLO 123 Hi 53 PYthon WELcome 3628'
# print(re.findall(r'[^a-z]', s))
# print(re.findall(r'[^a-z]', s))

# s = 'hello 123 hi 53 python welcome 3628'
# res = (re.findall(r'\s', s))
# print(len(res))

# s = 'hello 123 hi 53 python welcome 3628'
# print(re.findall(r'\S', s))
# l = s.split(' ')
# count = 0
# for item in l:
#     count += 1
# print(count)

# s = 'hello 123 hi 53  *# python !+$%( welcome 3628'
# print(re.findall(r'\w', s))
# print(re.findall(r'\W', s))
# print(re.findall(r'\d', s))
# print(re.findall(r'\D', s))
# print(re.findall(r'\s', s))
# print(re.findall(r'\W', s))
# print(re.findall(r'\b[0-9]{3}\b', s))
# s = 'the pincode of banglore 560001 and the telephone code is 109238464765'
# print(re.findall(r'\b[0-9]+\b', s))

# s = 'i am travelling from BLR to DLI in JULY'
# print(re.findall(r'\b[A-Z]{3}\b', s))

# s = 'i am travelling from BLR to DLI in JULY'
# print(re.findall(r'\b[a-z]{2,5}\b', s))

# s = 'i am travelling from BLR to DLI in JULY'
# print(re.findall(r'[a-z]{3}', s))

# s = 'hello hi worl hello how are you'
# print(re.findall(r'h\w+', s))