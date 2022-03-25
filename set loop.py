'''s = {'python', 'dad', 'hai', 'malayalam', 'madam', 'mom'}
for item in s:
    print(item, end=' ')

s = {'python', 'dad', 'hai', 'malayalam', 'madam', 'mom'}
key = 'hai'
for ele in s:
    s.discard(key)
    break

print(s)
s = {'python', 'dad', 'hai', 'malayalam', 'madam', 'mom'}
r = set()
for item in s:
    if item == item[::-1]:
        r.add(item)
        print(r)

for n in range(1,11):
    print(n)
for n in range(10,0,-1):
    print(n)
for n in range(-1, -10, -1):
    print(n)
for n in range(-10, 0):
    print(n)

for n in range(10, 0, -1):
   if n % 2 == 0:
       print(n,end=' ')

k = {'python'}
for n in k:
    print(n)

d = {'a':1, 'b':2, 'c':3}
for i in d:
    print(i, d[i])

e = 'python'
for n in range(len(e)):
    print(n, e[n])

s = [1, 2, 3]
s1 = [4, 5, 6]
print((*s, *s1))

n = 'praveen kumar p iyli'
for i in n[::-1]:
    print(i, end=' ')

n = 'praveen$%^ it !@'
count = 0
for i in n:
    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9'):
        count += 1
        print(count, end=' ')

h = 'PRaveEn'
d = 0
f = 0
for t in h:
    if 'a' <= t <= 'z':
        d += 1
    elif 'A' <= t <= 'Z':
        f += 1
        print(d, f)

t = ['python', 10, 3.2, 'selenium', 'java']
for index, item in enumerate(t):
    print(index, item)

t = ['python', 10, 3.2, 'selenium', 'java']
for item in t[::-1]:
    print(item)
t = ['python', 10, 3.2, 'selenium', 'java']
for index, item in enumerate(t):
    if index % 2 != 0:
        print(index)
t = ['python', 10, 3.2, 'selenium', 'java']
for m in t:
    if isinstance(m,(int)):
        print(m)

t = ['python','node js', 'selenium', 'java']
count = 0
for m in t:
    if len(m) % 2 == 0:
        print(m)
        count += 1

t = ['python','node js', 'selenium', 'java']
for m in t:
    if len(m) % 2 == 0:
        print(m)
    else:
        print(m[::-1])

t = ['python','node js', 10, 5+7j, 'selenium', 'java']
for m in t:
    if isinstance(m, str):
        print(m[::-1])
    else:
        print(m)'

z = ['apple', 'run', 'onion', 'tree', 'python']
for h in z:
    if h[0] in 'aeiouAEIOU':
        print(h)

c = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for n in c:
    a = n.split('.')
    print(a)

n ='praveen'
i = 0
while i < len(n):
    print(n[i], end=' ')
    i += 1

w = ['p', 'r', 'a', 'v', 'e', 'e', 'n']
i = 0
while i < len(w):
    print(w[i])
    i += 1

w = ['p', 'r', 'a', 'v', 'e', 'e', 'n']
i = -1
while i < len(w):
    print(w[i], end=' ')
    i -= 1

r = 'hai'
t = 'hello'
from itertools import zip_longest
for i1,i2 in zip_longest(r, t):
    print(i1,i2)

s = {'python', 'dad', 'hai', 'malayalam', 'mom', 'madam'}
key = 'hai'
for ele in s:
    s.discard(key)
    break
    print(s)

s = {'python', 'dad', 'hai', 'malayalam', 'mom', 'madam'}
r = set()
for item in s:
    if item == item[::-1]:
        r.add(item)
        print(item)

a = [10, 20, 40, 60, 20, 40, 10]
n = 20
for b in a:
    if n == n:
        continue
        print(a)'''

# d = {'a':1, 'b':2, 'c':3}
# for value in d.values():
#     print(values, end=' ')

# def fun(name):
#     return (f'{name} is ')
#
#
# print(fun('python'))

# def func(name, age):
#     return (f'{name} is {age} year old')
#
#
# print(func(name = 'ram', age = 25))
# print(func(age = 25, name = 'ram'))

# def func(a, b, c, d):
#     return (a, b, c, d)
#
#
# print(func(1, 2,c=3, d=4))

# def func(a, b, /, c, d):
#     return (a, b, c, d)
#
#
# print(func(1, 2, c=3, d=4))
# print(func(1, 2, 3, 4))
# print(func(a=1, b=2, 3, 4))

# def func(*, a, b, c, d):
#     return (a, b, c, d)
#
#
# print(func(a=1, b=2,c=3,d=4))
# print(func(1, 2, c=3, d=4))

# def func(a, b, /, *, c, d):
#     return (a, b, c, d)
#
#
# print(func(1, 2, c=3, d=4))
# print(func(a=1, b=2, c=3, d=4))
# print(func(1, 2, 3, 4))

# def func(*, a, b):
    # return a + b


# print(func(2, 3))
# print(func(a=2, b=3))
# print(func(1,b=3))


# def even(start=1, end=50):
#     l = []
#     for item in range(start, end):
#         if item % 2 == 0:
#             l.append(item)
#     return l
#
#
# print(even(1, 50))


# def prime():
#     for n in range(20):
#         if n > 1:
#             for item in range(2, n):
#                 if n % item == 0:
#                     break
#             else:
#                 print(n, end=' ')
#
#
# print(prime())

#
# def prime(start, end=1):
#     res = []
#     for n in range(start, end=0):
#         if n > 1:
#             for item in range(2, n):
#                 if n % item == 0:
#                     break
#             else:
#                 res.append
#
#
# print(prime(start=1, end=50))

# a = 0
# b = 1
# i = 0
# while i<50:
#
#     c = a + b
#     a = b
#     b = c
#     i += 1
# print(a)

# def spam(*args):
#     print(args)
#
#
# print(spam('python', 'men', 'pen'))

# def sum(*args):
#     sum = 0
#     for item in args:
#         if isinstance(item, (int, float)):
#             sum += 1
#     return sum
#
#
# print(sum(1, 2))


# def function(*args):
#     for item in args:
#         if isinstance (item, int):
#             return item
#
#
# print(function('python', 'java', 10, 4.5))


# def function(*args):
#     for item in args:
#         if isinstance(item, str):
#             print (len(item[::-1]))
#
# function('python', 10, 2.4, 'c++', 'java')


# def count_(*args, **kwargs):
#     return len(args), len(kwargs)
#
# print(count_(1, 2, 3, a=5, r=9))

# def function(*args):
#     if len(args) > 5:
#         return 'number of args > 5'
#     return 'number of args < 5'
#
#
# print(function(1, 2, 3, 4, 5))


# def function(*args, **kwargs):
#     return len(args), len(kwargs)


# print(function(1, 2, 3, a=4, t=5, g=9, u=8))


# def prime(args):
#     for item in range(2,args):
#         if args % item == 0:
#             return 'not prime'
#         return 'is prime'
#
#
# print(prime(5))

# def function(*args):
#     s = str(args)
#     return args[-1]


# print(function(12345))
#
# def tail(sequence, n):
#     return sequence[-n]
#
# print(tail('hello', 1))

#
# def isperfectsquare(n):
#     for i in range(n):
#         if i * i == num:
#             return true
#     return false
#
# print(isperfectsquare(4))

# def func(string, n):
#     if n == 0:
#         return string[1::2]
#     elif n == 1:
#         return string[::2]
#     else:
#         return 'not found'
#
# print(func('TRACXN', 0))


# n = 8
# a = 0
# b = 1
# i = 0
# while i < 10:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1

# def fi(num):
#     a = 0
#     b = 1
#     while a < num:
#         if a == num:
#             return f'{num} is f number'
#         c = a + b
#         a = b
#         b = c
#     return f'{num} is not f number'
#
#
# print(fi(13))

# def f(*args):
#     for item in args:
#         if not isinstance(item, (str, tuple, list, set, dict)):
#             return (item)
#         return len(item)


# print(f('hello', ('hai', 10), 2.2))


# with open(path) as file:
#     d = {}
#     for line in file:
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#                 print(d)

# file = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\access-log.txt'

# with open(file) as file_:
#     l = []
#     for line in file_:
#         words = line.split()
#         l.append(words[0])

# print(l)


# with open(file) as file_:
#     d = {}
#     for line in file_:
#         if line.strip():
#             word = line.split()
#             if word[0] not in d:
#                 d[word[0]] = 1
#             else:
#                 d[word[0]] += 1
#     print(d)
# from itertools import islice
# with open (file) as file_:
#     res = islice(file_, 0, 3)
#     print(list(res))
#
# from itertools import islice
# n = 3
# with open(file) as file:
#

    # print(list(res))

f_path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'


# n = 4
# if n % 2 == 0:
#     print('it is even')
# else:
#     print('it is not even')

# o = 'A'
# if 'a' <= o <= 'z':
#     print('is present')
# else:
#     print('not present')

# l = ['python', 'java', 'selenium']
# h = 'kite'
# if h in l:
#     print('is present')
# else:
#     print('not present')


# char = '*'
# if 'a' <= char <= 'z':
#     print('it is present')
# elif 'A' <= char <= 'Z':
#     print('upper')
# else:
#     print('special character')


# n =
# if n:
#     print('value is found')
# else:
#     print('value not found')
#


# s = []
# if s:
#     print('value not')
# else:
#     print('value found')


# word = '*'
# if 'a' <= word <= 'z':
#     upper_ = word.upper()
#     print(upper_)
# elif 'A' <= word <= 'Z':
#     lower_ = word.lower()
#     print(lower_)
# else:
#     print('special character')


# string = 'python'
# if string[0] in 'aeiouAEIOU':
#     print('found')
# else:
#     print('not found')


# c = 'madam'
# if c == c[::-1]:
#     print('is palindrome')
# else:
#     print('is not palindrome')


# num = 1221
# d = str(num)
# if d == d[::-1]:
#     print('is palindrome')
# else:
#     print('is not palindrome')


# iterable = [10, 20, 30]
# if len(iterable) % 2 == 0:
#     print('is even')
# else:
#     print('is odd')

# iterable = [49, 20, 30]
# if iterable[0] % 2 == 0:
#     print('is even')
# else:
#     print('is odd')


# string = 'python'
# for item in string:
#     print(item, end=' ')


# for n in range(1, 10):
#     if n % 2 == 0:
#         print(n)


# s = 'string'
# for item in range(len(s)):
#     print(s[item])

# s = 'python'
# for index, item in enumerate(s):
#     print(item, index)

# s = 'hello'
# for item in s[::-1]:
#     print(item)


# s = 'hello world'
# count = 0
# for item in s:
#     count += 1
#     print(count)

# s = 'python'
# for item in s[::2]:
#     print(item)


# n = 'hello 123 hai 4 % 978'
# for item in n:
#     if item.isdigit():
#         print(item)

# n = 'hello 123 hai 4 % 978'
# count = 0
# for item in n:
#     if '0' <= item <= '9':
#         count += 1
# print(count)

# l = ['python', 10, 4.4, True, 'java']
# for i, j in enumerate(l):
#     print(i, j)

# l = ['python', 10, 4.4, True, 'java']
# for item in l[::-1]:
#     print(item)


# l = ['python', 10, 4.4, True, 'java']
# for item in l[::2]:
#     print(item)

# l = ['python', 10, 4.4, True, 'java']
# for item in l:
#     if isinstance(item, int):
#         print(item)

# l = ['python', True, 'java', 'node js']
# for item in range(len(l[0])):
#     print(l[0][item])

# l = ['python', 'java', 'node js']
# for item in l:
#     if len(item) % 2 == 0:
#         print(item)

# def count(n):
#     if n <= 10:
#         print(n)
#         n += 1
#         count(n)
#     else:
#         return


# count(1)

def count(n):
    if n > 10:
        return
    print(n)
    count(n+1)


# print(count(1))

# def f(n):
#     if 10 < n:
#         return
#     print(n)
#     f(n-1)


# print(1)

def sum_(num, sum = 0):
    if num > 0:
        last = num % 10
        sum += last
        num = num // 10
        sum_(num)
    else:
        return

# print(sum_(123))

l = ['python', 'node js', 'java', 'insta']
# for item in l
#     if len(item) % 2 == 0:
        # print(item)
    # else:
        # print(item[::-1])

# def f(*args):
#     for item in l:
#         if len(item) % 2 == 0:
#             return item
#         return (item[::-1])
#
#
# print(f('python', 'node js', 'java', 'insta'))

# p = ['java', 'python', 10, 'ruby', True, 3.4]
# def f(*args):
#     for item in p:
#         if isinstance(item, str):
#             print (item[::-1])
#
# f('java', 'python', 10, 'ruby', True, 3.4)

# l = ['amazon', 'onion', 'men', 'python']
# def f(*args):
#     for item in l:
#         if item[0] in 'aeiouAEIOU':
#             print(item)
#
# f('amazon', 'onion', 'men', 'python')

# f = ['youtube.txt', 'amazon.pdf', 'apple.txt', 'flipkart.in']
# def f(*args):
#     for item in f:
#         l = item.split('.')
#         print(l)
#
# f('youtube.txt', 'amazon.pdf', 'apple.txt', 'flipkart.in')

# f = ['youtube.txt', 'amazon.pdf', 'apple.txt', 'flipkart.in']
# for item in f:
#     l = item.split('.')
#     print(l[0])

# z = [10, 30, 40, 20, 30, 10, 60]
# p = 30
# for i, j in enumerate(z):
#     if p == j:
#         print(i)
#         break

# n = 5
# for item in range(2, n):
#     if n % item == 0:
#         print('not a prime')
#         break
#     else:
#         print('is prime')


# for n in range(10):
#     if n > 1:
#         for item in range(2, n):
#             if n % item == 0:
#                 break
#         else:
#             print(n)

# l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
# for item in l:
#     if item == item[::-1]:
#         print(item[::-1])

# s = {'python', 'dad', 'hai', 'madam'}
# g = 'hai'
# for ele in s:
#     s.discard(g)
#     break
# print(s)


# l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
# res = set()
# for item in l:
#     if item == item[::-1]:
#         res.add(item)
# print(res)

# s = 'hai'
# s1 = 'hello'
# from itertools import zip_longest
# for i1, i2 in zip_longest(s, s1):
#     print(i1, i2)

# d = {'a': 1, 'b': 2, 'c': 3}
# for i, j in d.items():
#     print(j)

# d = {'a': 1, 'b': 2, 'c': 3}
# for i, (j, k) in enumerate(d.items()):
#     print(i, (j, k))
# string = 'hello world'
# d = {}
# for item in string:
#     d[item] = string.count(item)
# print(d)

# s = 'python is easy language'
# d = {}
# l = s.split()
# for item in l:
#     d[item] = len(item)
# print(d)

def sentence(args):
    d = {}
    l = args.split()
    for item in l:
        d[item] = len(item)
    return d

# print(sentence('python is easy language'))


# wap to print a dict with index and word pair
# def func(args):
#     l = args.split()
#     d = {}
#     for index, item in enumerate(l):
#         d[index] = item
#     return d
#
# print(func('python is easy language'))


# wap to get longest word in sentence
s = 'python is easy language'
# l = s.split()
# max = ""
# for item in range(len(l)):
#     if len(l[item]) > len(max):
#         max = l[item]
# # print(max)
#
# l = s.split()
# l.sort(key=len)
# # print(l[-1])
#
# l = s.split()
# res = sorted(l, key=len)
# # print(res[-1])

# l = ['python', 'java', 'c', 'ruby', 'perl']
# print(sorted(l, key=len))

# s = 'python is a programming language'
# l = s.split()
# short, *rest, long = sorted(l, key=len)
# print(long, short)

s = 'python is a programming language'
# l = s.split()
# short, *rest, long = sorted(l, key=len)
# print((long, len(long)), (short, len(short)))

# l = ['python', 'java', 'c', 'ruby', 'perl']
# print(sorted(l, key= lambda item: item[-1]))

# l = ['python', 'java', 'c', 'ruby', 'perl']
# print(sorted(l, key= lambda item: item[0]))

# s = {'gmail': 5, 'apple': 3, 'walmart': 7, 'flipkart': 8}
# print(dict(sorted(s.items(), key=lambda item: item[0])))

# s = {'gmail': 5, 'apple': 3, 'walmart': 7, 'flipkart': 8}
# print(dict(sorted(s.items(), key=lambda item: item[-1])))

# temp = [('delhi', 32), ('mumbai', 27), ('kolkata', 30), ('chennai', 35)]
# print(sorted(temp, key=lambda item: item[-1]))

# s = 'hi how are you how is your health'
# l = s.split()
# d = {item: l.count(item) for item in l}
# res = sorted(l.count.items(), key= lambda item: item[-1])
# print(res[-1])

# for n in range(1, 50):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)


# n = 4
# for item in range(2, n):
#     if n % item == 0:
#         print('not prime')
#         break
#     else:
#         print('is prime')

# n = 'hello'
# print(n[::-1])
#
# for i in range(len(n)-1, -1, -1):
#     print(n[i], end='')
#
# for i in reversed(n):
#     print(i, end='')


# for item in n[::-1]:
#     print(item, end='')

# n = 'hello'
# count = 0
# for item in n:
#     count += 1
# print(count)

# s = 'hello welcome to python'
# print(s, end=',')
# l = s.split()
# for item in l:
    # print(item, end=',')

# s = 'hello world'.replace('world', 'universe')
# print(s)

# s = 'hello world'
# for item in s[::2]:
#     print(item)
# s = 'hello'
# for i in s:
#     print(ord(i))

# v = 'heLLo'
# res = ""
# for i in v:
#     if 'a' <= i <= 'z':
#         res += chr(ord(i) - 32)
#     elif 'A' <= i <= 'Z':
#         res += chr(ord(i) + 32)
#     else:
#         res += i
#
# print(res)

# l1 = [1, 2, 3, 4]
# l2 = ['hai', 'hello']
# print([*l1, *l2])

# p = 'mom'
# if p == p[::-1]:
#     print('is palindrome')
# else:
#     print('not palindrome')

# s = 'helloe'
# p = 'e'
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(s):
#     if p == item:
#         dd[p] += [index]
# print(dd)


# s = 'hello world python hi'
# l = s.split()
# from collections import defaultdict
# dd = defaultdict(list)
# for i in l:
#     dd[i[0]] += [i]
# print(dd)


# k = 'banglore\n'
# print(k * 10)

# s = 'hai1234 python23'
# count = 0
# for i in s:
#     if '0' <= i <= '9':
#         count += 1
# print(count)


# s = 'python selenium'
# for item in s:
#     if item not in 'aeiouAEIOU':
#         print(item, end='')

# s = 'python selenium'
# o = 'n'
# for i, item in enumerate(s):
#     if o == item:
#         print(f'{item} is in {i}')
#         break


# s = 'she sells sea shells on the sea shore'
# for item in s:
#     if item in 'aeiouAEIOU':
#         print(item, ord(item))

# s = 'she sells sea shells on the sea shore'
# l = s.split()
# for item in l:
#     print((item, len(item)))


# s = 'she sells sea shells on the sea shore'
# l = s.split()
# for item in l:
#     if item[0] in 'aeiouAEIOU':
#         print(item)

# s = 'hello world'
# count = 0
# for item in s:
#     count += 1
# print(count)

# s = 'hello world'
# res = ''
# for item in s:
#     res = item + res
# print(res)

# n = ['apple', 1.2, 'google', '12.6', 26, '100']
# for item in n:
#     if isinstance(item, (int, float, complex)):
#         print(str(item))

# s = 'hello 123 world 567 welcome to 9724 python'
# sum = 0
# for item in s:
#     if '0' <= item <= '9':
#         if int(item) % 2 == 0:
#             sum += int(item)
# print(sum)

# l = ['python', 'java', 'perl', 'PHP', 'python', 'js', 'c++', 'js', 'python', 'ruby']
# i = set()
# for item in l:
#     if item[0] in 'pP':
#         i.add(item)
# print(i)

# l = ['python', 'java', 'perl', 'PHP', 'python', 'js', 'c++', 'js', 'python', 'ruby']
# l1 = []
# for item in l:
#     if len(item) % 2 == 0:
#         l1.append(item)
# print(l1)

# l = ['python', 'java', 'perl', 'PHP', 'python', 'js', 'c++', 'js', 'python', 'ruby']
# for item in l:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

# for n in range(1, 10):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print(n, 'it is not prime')
                # break
        # else:
        #     print(n, end=' ')


# w = ['python', 'hello', 'hi']
# for item in w[::-1]:
#     print([item[::-1]], end=' ')

# y = 'hello python welcome'
# count = 0
# for item in y:
#     count += 1
#     print(count, end='')

# s = 'hello123 hai3 true937'
# count = 0
# for item in s:
#     if not isinstance(item, str):
#         count += 1
# print(count)

# def fun(*args):
#     for item in args:
#         if '0' <= item <= '9':
#             print(item)
#
# fun('hello 123 h72y 3 gsgsj8353')

# def func(*args):
#     for item in args:
#         r = reversed(item)
#     return r
#
# print(func('hello', 'hai', 'perl'))

# l = ['python', 'perl', 'madam', 'java']
# for item in reversed(l):
#     print(item[::-1])
#
# l = ['python', 'perl', 'madam', 'java']
# for i in l[::2]:
#     print(i)

