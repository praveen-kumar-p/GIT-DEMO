'''iterable='hai'

if iterable:
    print('iterable is not empty')
else:
    print('iterable is empty')


s=[]
if s:
    print('it is a not default value')
else:
    print('it is default value')


p='H'
if p.islower():
    print(p.upper())
elif p.isupper():
    print('p.lower()')
else:
    print('special character')

if 'a' <= o <= 'z'
    upper=o.upper()
    print(upper)
elif 'A' <= 0 <

number=1221
str_num=str(number)

if str_num == str_num[::-1]:
    print(f'{number} is palindrom')
else:
    print(f'{number}is not palindrom')

# number = 123
# str_num = str(number)
#
# if str_num == str_num[::-1]:
#     print(f'{number} is palindrom')
# else :
#     print(f'{number} is not palindrom')


p = 'hai'
if bool(p):
    print('p is not

a = 10
b = 20


a = 'hello,how are you'
b = 'i am fine'

print(a + ' ' + b)
print('hi'* 10)
print(a[0:5])
print(a[-1])
print(b)
x = 10
x = x+5
x+=5
print(x)

a = 3
if a>2:
    print('True')
else:
    print('false')

e = int(input("4"))
print(e)
if e % 2 == 0:
    print('e is even')
else:
    print('e is odd')

g = '%'
if 'a' <= g <= 'z':
    print(f'{g} is lower')
elif 'A' <= g <= 'Z':
    print(f'{g} is upper')
else:
    print('is special charaters')

c = 'Mom'
a = c.lower()
if c == c[::-1]:
    print('c is palindrom')
else:
    print('c is not palindrom')

q = 123
str_q = str(q)
if int(str_q[0])%2 == 0:
    print('q is even')
else:
    print('q is odd')


i = 1234
if len('list') % 2 == 0:
    print('i as even no')
else:
    print('i is odd no')

c = 'mom'
if c == c[::-1]:
    print(c, "is palindrom")
else:
    print(c, "is not palindrom")


a = 10
b = 20
c = 15
if (a>b) and (a>c):
    print(a)
elif (b>c):
    print(b)
else :
    print(c)'''



# n = 1
# while n <= 50:
#     if n % 2 == 0:
#        print(n)
#     n +
import sys

'''for n in range(1,11):
    if n % 2 == 0:
        print(n)

f = 'python'
for item in range (len(f)):
    print(f[item])

f = ['p', 'y', 't', 'h', 'o', 'n']
for t in range(len(f)):
    print(f[t], end=' ')
f = ('p', 'y', 't', 'h', 'o', 'n')
for u in range(len(f)):
    print(f[u], end=' ')






k = {'python'}
for o in k:
    print(o)


d = {'e': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key]

s = 'python'
for n in range(s):
    print()

s = 'hai'
for d in s[::-1]:
    print()
s = 'hello'
count = 0
for item in s:
    count += 1
    print(count, end=' ')


p = 'praveen'
for i in p[::2]:
    print(i,end=' ')


d = 'hello123 hai 983'
for m in d:
    if m. isdigit():
        print(m, end='@')


v = 'hello 123 and 489'
count = 0
for m in v:
    if m.isdigit():
        count += 1
        print(count, end=' ')

a = '!@#$true 89 we %^'
count

n = 1
while n <= 10:
    print(n, end=' ')
    n += 1

n = 10
while n > 0:
    print(n, end=' ')
    n -= 1
n = -1
while n >= -10:
    print(n)
    n -= 1

n = -10
while n < 0:
    print(n, end=' ')
    n += 1

n = 1
while n <= 50:
        print(n, end=" ")
        n += 2
w = 'hello'
i = 0
while i < len(w):
    print(w[i], end=' ')
    i -= 1


k = 25
if k % 2 == 0:
    print(f'{k} is even')
else:
    print(f'{k} is not even')

j = {1, 2,  3, 4}
ele = 2
if ele in j:
    print('ele is present')
else:
    print('ele is not present')

a = 9
if (a!=9):
    print('not equal')
else:
    print('equal')


h = 10
if h % 2 == 0:
    print(f'{h} is even')
else:
    print(f'{h} is odd')

l = '^'
if 'a' <= l <= 'z':
    print('l is lower')
elif 'A' <= l <= 'Z':
    print('l is upper')
else:
    print('l is special symbol')

x = 0
if x:
    print('is value')
else:
    print('is not value')

s = 
if s:
    print('s is not default')
else:
    print('s is default')

v = '#'
if v.islower():
    y = v.upper()
    print('y is upper')
elif v.isupper():
    y = v.lower()
    print('y is lower()')
else:
    print('y is not upper or lower')

c = 'Mom'
y == c.lower()
if y == c[::-1]:
    print(f'{c} is palindrom')
else:
    print(f'{c} is not palindrom')

o = 2345678
p = str(o)
if int(p[0]) % 2 == 0:
    print('o is even')
else:
    print('o is odd')

a = 1221
b = str(a)
if b == b[::-1]:
    print('is palindrom')
else:
    print('is not palindrom')


c = 'M0M'
a = c.lower()
if a == a[::-1]:
    print('is palindrom')
else:
    print('is not palindrom')

print()

u = 'apple'
if u[-1] in 'aeiou':
    print('u is vowel')
else:
    print('u is not vowel')

e = 'adyuhg@#$% *! b'
count = 0
for m in e:
    count += 1
    print(count, end=' ')
p = ['python', 10, 3.4, 'selenium', 'java']
for i in p:
    print(i)

p = ['python', 10, 3.4, 'selenium', 'java']
for i in p[1::2]:
    print(i)

p = ['python', 10, 3.4, 'selenium', 'java']
for i in range(0, len(p), 2):
    print(i)

p = ['python', 10, 3.4, 'selenium', 'java']
t = 'selenium'
for t in p:
    print(t)

p = ['python', 10, 3.4, 'selenium', 'java']
for i in range(len(p)-1, -1, -1):
    print(p[i])

p = ['python', 10, 3.4, 'selenium', 'java']
for item in p:
    if isinstance(item, int):
        print(item)

p = ['python', 10, 3.4, 'selenium', 'java']
for i in range (len(p[0])):
    print(p[0][i])

d = 'hai#@y 4*&'
count = 0
for n in d:
    if not ('a' <= d <= 'z' or 'A' <= d <= 'Z' or '0' <= d <= '9'):
        count += 1
        print(d)
p = ['python', 'node js', 'selenium', 'insta']
for i in p:
    if len(i) % 2 == 0:
        print(i)
    else:
        print(i[::-1])

l = ['java', 'python', 10, True, 1.4, 'c++', 'ruby']
for m in l:
    if isinstance(m, str):
        print(m[::-1])
    else:
        print(m, end=' ')

m = ['amazon', 'flipkart']
for n in m:
    if n[0] in 'aeiouAEIOU':
        print(n)

f = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for m in f:
    a = m.split('.')
    if len(a[0]) % 2 == 0:
        pass

    else:
        print(a[0])

n = 5
for i in range(2, n):
    if n % i == 0:
        print('nota prime')
        break
else:
    print('it is a prime')

a = [10, 40, 20, 80, 20, 40, 30]
n = 20
for b in a:
    if n % i == 0:


s = 'hello world'
d = {}
for char in s:
    d[char] = s.count(char)
    print(d)


s = {'a': 1, 'b': 2, 'c': 3}
for key, value in s.items():
    print(value)

s = {'a': 1, 'b': 2, 'c': 3}
for index, item in enumerate(s):
    print(index)

sentence = 'python is a language, python programming is easy'
d = {}
list_ = sentence.split()
for word in list_:
    if len(word) % 2 == 0:
        d[word] = len(word)
print(d)

sentence = 'python is a language, python programming is easy'
list_ = sentence.split()
d = {}
for word in list_:
    if word[0] in 'aeiouAEIOU':
        d[word] = len(word)
print(d)
sentence = 'python is a language, python programming is easy'
list_ = sentence.split()
d = {}
for word in list_:
    if list_count(word) == 1:
        d[word] = list_.count(word)
print(d)

d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
for key, value in d.items():
    if isinstance(value, str):
        d[key] = value[::-1]

print(d)

names = ['apple', 'google', 'gmail', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
d = {}
from collections import defaultdict
dd = defaultdict(list)
for index, element in enumerate(names):
    dd[element] += [index]
print(dd)

d = {'a': 'hello', 'b': '100', 'c': '10.2', 'd': 'world'}
d2 = {}
for key, value in d.items():
    d2[value] = key
print(d2)

n = 4
if n % 2 == 0:
    print('n even')
else:
    print('odd')

x = 'm'
if 'a' <= x <= 'z':
    print('is present')
else:
    print( 'not present')

m = ['python', 'java', 'selenium','insta']
p = 'insta'
if p in m:
    print('p is present')
else:
    print('p is not present')

a = 'k'
if a != 9:
    print('not present')
else:
    print('present')

n = 7
if n % 2 == 0:
    print('n is even')
else:
    print('n is odd')

c = '#'
if 'a' <= c <= 'z':
    print('r is lower')
elif 'A' <= c <= 'z':
    print('r is upper')
else:
    print('is special character')

iterable = 2.2
if iterable:
    print('iterable is not empty')
else:
    print('iterable is empty')

s = 0
if s:
    print('s is not empty')
else:
    print('s is empty')

a = 'n'
if 'a' <= a <= 'z':
    u_a = a.isupper()
    print('u_a')
elif 'A' <= a <= 'Z':
    l_a = a.islower()
    print('l_a')
else:
    print('special character')

string = 'apple'
if string[0] in 'aeiouAEIOU':
    print('is vowel')
else:
    print('is not vowel')

s = 'python'
if s[-1] in 'aeiouAEIOU':
    print('is vowel')
else:
    print('is not vowel')

string = 'mom'
if string[::-1]:
    print('is palindrome')

else:
    print('is not palindrome')

n = 1221
list_ = str(n)
if list_ == list_[::-1]:
    print('is palindrome')
else:
    print('is not palindrome')

iterable = 'python'
if len(iterable) % 2 == 0:
    print('is even element')
else:
    print('is not even element')

n = [10, 20, 15, 30, 40]
m = 15
if m % 2 == 0:
    print('m is even')
else:
    print('m is not even')

n = [1, 2, 3]
m = 3
if m > n:
    print('is greater')
else:
    print('is not greater')

n = 'a'
d = {}
if n in 'aeiou':
    d[n] = ord(n)
    print(d)

s = ['p', 'y','t', 'h', 'o', 'n']
i = 0
while i < len(s):
    print(s[i])
    i += 1

for n in range(1, 11):
    if n % 2 != 0:
        print(n)

s = 'python'
for item in s:
    print(item)
s = 'python'
for item in s:
    print(s)

s = {'python'}
for n in s:
    print(n)

s = 'python'
for index, item in enumerate(s):
    print(index, item)

l = [1, 2, 3]
l1 = [4, 5, 6]
print([*l, *l1])

n = [1, 2, 3, 4, 5, 6, 7, 8]
n1 = n[-1]
n2 = n[0]
n3 = *rest
print(n1, n2, *rest, sep='-')

s = 'hello'
for item in s[::-1]:
    print(item)

s = 'hello world'
count = 0
for item in s:
    count += 1
    print(count)

s = 'hello world'
for item in s[::2]:
    print(item, end=' ')

s = 'hello123 hai4 py7'
for item in s:
    if item.isdigit():
        print(item, end=' ')


s = 'hello123 hai4 py7'
count = 0
for item in s:
    if '0' <= item <= '9':
        print(count)
        count += 1

s = '!@#efjrh$$#%&('
count = 0
for item in s:
    if not 'a' <= item <= 'z':
        count += 1
        print(count, end=' ')

l = ['python', 10, 3.4, 'selenium', 'java']
for index, item in eumerate(l)[::2]:
    print(index)

l = ['python', 10, 3.4, 'selenium', 'java']
for item in l:
    if isinstance(item, int):
        print(item)

l = ['python', 'selenium', 'java']
for item in l:
    if len(item) % 2 == 0:
        print(item)

l = ['python', 'selenium', 'java', 'praveen', 'kumar']
for item in l:
    if len(item) % 2 == 0:
        print(item)
    else:
        print(item[::-1])

l = ['python', 10, 2+8j, 'selenium', 'java']
for item in l:
    if isinstance(item, str):
        print(item[::-1])
    else:
        print(item)

l = ['apple', 'eight', 'java', 'union']
for item in l:
    if item[0] in 'aeiouAEIOU':
        print(item)

l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for item in l:
    a = item.split('.')
    print(a)

l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for m in l:
    a = m.split('.')
    if len(a[0]) % 2 == 0:
        pass
    else:
        print(a[0])

z = [10, 40, 20, 80, 20, 40, 30]
i = 40
for index, item in enumerate(z):
    if item == i:
        print(index)
        break
l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for item in l:
    a = item.split('.')
    print(a)
l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for item in l:
    a = item.split('.')
    if len(a[0]) % 2 == 0:
        pass
    else:
        print(a[0])

z = [10, 40, 20, 80, 20, 40, 30]
m = 100
for index, item in enumerate(z):
    if item == m:
        print(index)
        break
else:
    print('element is not found')


l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for item in l:
    a = item.split('.')
    print(a[0])

l = [1, 2, 3, 4, 5]
n = 5
for i in range(2, n):
    if n % 2 == 0:
        print('not a prime')
        break
else:
    print('is prime')

n = 10
for n in range(10):
    if n > 1:
        for i in range(2, n):
            if n % 2 == 0:
                break
        else:
            print('n')

a = [10, 40, 20, 80, 20, 40, 30]
n = 20
for item in a:
    if  n == num:
        continue
        print(n)

m = 'a'
if 'a' <= m <= 'z':
    print(chr(ord(m)-32))
else:
    print(' m is not alphabet')

n = '12 alpha 78 python'
sum = []
for item in n:
    if item.isdigit():
        sum += int(item)
print(sum)
s = 'python'
count = 0
for item in s:
    count += 1
    print(item)


s = 'python'
for item in range(len(s)-1, -1, -1):
    print(item)
s = '!@#eat+*'
for item in s:
    if not 'a' <= item <= 'z':
        print(item)

s = 'praveen'
m = 'a'
for index, item in enumerate(s):
    if item == m:
        print(index, item)

d = {'a': 1, 'b': 2, 'c': 3}
for index, item in enumerate(d.items()):
    print(index, item)

s = 'hello world'
from collections import defaultdict
dd = defaultdict(int)
for item in s:
    dd[item] = dd[item] + 1
    print(dd)

s = 'python is a language, python programming is easy'
d = {}
l_ = s.split()
for word in l_:
    d[word] = l_.count(word)
print(d)

s = 'python is a language, python programming is easy'
from collections import defaultdict
dd = defaultdict(int)
p = s.split()
for word in p:
    dd[word] = dd[word] + 1
print(dd)

s = 'hello'
d = {}
for char in s:
    d[char] = s.count(char)
print(d)

s = 'python is a language, python programming is easy'
d = {}
l = s.split()
for word in l:
    d[word] = l.count(word)
print(d)

s = 'python is a language, python programming is easy'
from collections import defaultdict
d = {}
l = s.split()
dd = defaultdict(int)
for word in l:
    dd[word] = dd[word] + 1
print(dd)
s = 'python is a language, python programming is easy'
d = {}
l = s.split()
for word in l:
    if len(word) % 2 == 0:
        d[word] = len(word)
print(d)

s = 'python is a language, python programming is easy'
d = {}
l = s.split()
for word in l:
    if word[0] in 'aeiouAEIOU':
        d[word] = len(word)
print(d)
s = 'python is a language, python programming is easy'
d = {}
l = s.split()
for word in l:
    if l.count(word) == 1:
        d[word] = l.count(word)
print(d)

d = {'a':'hello', 'b': '100', 'c': 'member', 'd': 'world'}
for key, value in d.items():
    d[key] = value[::-1]
print(d)

names = ['apple', 'google', 'gmail', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
d = {}
for name in names:
    d[name] = names.count(name)
print(d)

s = 'hello world welcome to python programming hi there'
d = {}
l = s.split()
for word in l:
    if l.count(word) == 1:
        d[word] = l.count(word)
print(d)

s = 'hello world hello to python programming hi there'
d = {}
l = s.split()
for word in l:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
print(d)
s = 'hello world hello to python programming hi there'
from collections import defaultdict
d = {}
l = s.split()
dd = defaultdict
for word in l:
    dd[word[0]] = dd[word[0]] 
print(dd)

d = {'a':'hello', 'b': '100', 'c': 'member', 'd': 'world'}
d1 = {}
for key, value in d.items():
    d1[value] = key
print(d1)

s = 'hello'
for index, item in enumerate(s):
    print((index, item))

y = 'hello world'
count = 0
for item in y:
    count += 1
print(count)'''

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     l = []
#     for line in file:
#         l.append(len(line))
#     print(l)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log'
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             res = line.split()
#             l.append(res[2])
#
# print(l)


# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     l = []
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             l.append(res[1])
#     print(l)

# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

# def test(i, j):
#     if i == 0:
#         return j
#     else:
#         return test(i-1, i+j)
# 
# print(test(4, 7))

# import sys
# print(sys.setrecursionlimit(10000))

# sys.getrecursionlimit()

# import sys
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())

# s = 'hellohai'
# m = '-'
# for item in s:
#     if item in 'aeiouAEIOU':
#         repla
#     else:
#         print(s)

# s = 'hello'
# p = 'l'
# for i, item in enumerate(s):
#     if item == p:
#         print(f'{item} is at {i}')
#         break

# i = 'madam'
# if i == i[::-1]:
#     print(f'{i} is palindrome')
# else:
#     print(f'{i} not palindrome')

# l = [1, 2, 3]
# l2 = ['hai', 'hello']
# print(l + l2)
# print(*l, *l2)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files'
# n = 2
# from collections import deque
# with open(path) as file:
#     lines = deque(file, 2)
#     print(list(lines))

# s = 'hello world hi welcome to python'
# l = s.split()
# from collections import defaultdict
# dd = defaultdict(list)
# for item in l:
#     dd[item[0]] += item
#
# print(dd)

# l = [1, 2, 3, 4, 5]
# for i, j in enumerate(l):
#     print(i, j)
#
# res = [(i, j) for i, j in enumerate(l)]
# print(res)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# res = [item for item in l if item % 2 == 0]
# print(res)

# l = ['python', 'node js', 'men' 'java', 'perl']
# res = [i if len(i) % 2 == 0 else i[::-1] for i in l]
# print(res)

# l = ['perl', 10, 2+9j, 'java', 3.4]
# res = [item if isinstance(item, str) else str(item)[::-1] for item in l]
# print(res)

# l = ['onion', 'men', 'java', 'ice', 'eat']
# res = [item for item in l if item[0] in 'aeiou']
# print(res)

# s = {1, 2, 3, 4, 5}
# res = {(i * i) for i in s}
# print(res)

# s = 'hello'
# res = {j: i for i, j in enumerate(s)}
# print(res)

# s = 'hi welcome to python'
# l = s.split()
# res = {i: len(i) for i in l}
# print(res)

# s = 'hello world'
# res = {item: s.count(item) for item in s}
# print(res)

# s = 'hi welcome to python'
# l = s.split()
# res = {item: l.count(item) for item in l}
# print(res)

# s = 'hi welcome to python'
# l = s.split()
# res = {item: l.count(item) for item in l if len(item) % 2 == 0}
# print(res)

# s = 'python is a language, python progamming is easy'
# l = s.split()
# res = {i: j if len(j) % 2 == 0 else j for i, j in enumerate(l)}
# print(res)

# c = ['mumbai', 'mp', 'up', 'karnataka']
# p = [10, 20, 30, 40]
# for i, j in zip(c, p):
#     print(i, j, end=' ')

# l = ['madam', 'java', 'mom']
# m = lambda item: item == item[::-1]
# p = filter(item)
# print(list(p))

# l = [1, 2, 3, 4, 5, 6]
# def even(num):
#     if num % 2 == 0:
#         return num
#
# evens= filter(even, l)
# print(list(evens))

# l = ['madam', 'mom', 'eat', 'ice']
# def ex(args):
#     if args == args[::-1]:
#         return args
#
#
# p = filter(ex, l)
# print(list(p))
#
# l = ['onion', 'eat', 'pen', 'men', 'perl', 'ice']
# def func(*args):
#     for item in args:
#         if item[0] not in 'aeiou':
#             return item
#
# p = filter(func, l)
# print(list(p))

# l = [1, 2, 3, 4]
# def func(*args):
#     for item in args:
#         return (item * item)
#
# p = map(func, l)
# print(list(p))

# l = ['onion', 'eat', 'pen', 'men', 'perl', 'ice']
# def func(*args):
#     for item in args:
#         if item[0] in 'aeiou':
#             return item
#
# p = map(func, l)
# print(list(p))

# l = ['onion', 'eat', 'pen', 'men', 'perl', 'ice']
# p = lambda item: f'{item.upper()}'
# m = map(p, l)
# print(list(m))

# l = ['ONION', 'EAT', 'PEN', 'MEN', 'PERL', 'ICE']
# m = lambda item: f'{item.lower()}'
# p = map(m, l)
# print(list(p))

# l = [-1, -2, -3, -4]
# m = lambda item: abs(item)
# p = map(m, l)
# print(list(p))

# l = ['ONION', 'EAT', 'PEN', 'MEN', 'PERL', 'ICE']
# def func(*args):
#     for item in args:
#         return len(item)
#
# p = map(func, l)
# print(list(p))

# l = 'hello world'
# def func(a):
#     for i in a:
#         return (i, ord(i))
#
# p = map(func, l)
# print(list(p))

# res = lambda a, b: a + b
# print(res(1, 2))

# m = lambda item: item % 2 == 0
# print(m(3))

path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
#
# with open(path) as file:
#     for line in file:
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

# with open(path) as file:
#     for i, j in enumerate(file, start=1):
#         print(j, i)

# with open(path) as file:
#     count = 0
#     for line in file:
#         l = line.split()
#         for p in l:
#             count += 1
#     print(count)

path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line in reversed(file):
#         print(line)

# s = 'hello123 hai3 true937'
# for i in s:
#     if '0' <= i <= '9':
#         print(i)

# s = 'hello123 hai3 true937'
# for m in s:
#     if not 'a' <= m <= 'z':
#         print(m)
# s = 'hai#$ *07++^'
# for char in s:
#     if not ('a' <= char <= 'z' or '0' <= char <= '9'):
#         print(char)

# l = [1, 2, 3, 4, 5]
# def func(*args):
#     for i in args:
#         if i % 2 == 0:
#             return i
# p = filter(func, l)
# print(list(p))

# l = [1, 4, 5, 6, 8, 64, 9, 12]
# p = lambda item: item * item
# m = map(p, l)
# print(list(m))

# l = ['python', 10, 6.4, 'java']
# for item in l:
#     if isinstance(item, (int, float)):
#         print(item)

# s = 'hello123 hai47 pyhton2936'
# for item in s:
#     if item.isdigit():
#         print(item, end=' ')

# s = 'hello123 hai47 pyhton2936'
# count = 0
# for i in s:
#     if i.isdigit():
#         count += 1
# print(count)

# p = 'piyb@#$%mdnk##$%%^&(+(*&^%$'
# count = 0
# for i in p:
#     if not 'a' <= i <= 'z':
#         count += 1
# print(count)

# n = ['apple', 'java', 'google', 'instagram', 'yelp', 'flipkart']
# l = []
# for item in n:
#     if len(item) % 2 == 0:
#         l.append(item)
# print(l)

# n = ['apple', 'java', 'google', 'instagram', 'yelp', 'flipkart']
# l = []
# for item in n:
#     if len(item) % 2 != 0:
#         l.append(item[::-1])
# print(l)

# for n in range(1, 100):
#     if n > 1:
#         for item in range(2, n):
#             if n % item == 0:
#                  break
#         else:
#             print(n)

# n = ['apple', 'java', 'google', 'instagram', 'yelp', 'flipkart', 'google', 'java', 'yelp']
# l = []
# for item in n:
#     if item not in l:
#         l.append(item)
# print(l)

# s = 'hello123 hai457 python98421634'
# sum = 0
# for i in s:
#     if '0' <= i <= '9' and int(i) % 2 == 0:
#         sum +=int(i)
# print(sum)

# n = ['apple', 'java', 'google', 'instagram', 'yelp', 'flipkart', 'google', 'java', 'yelp']
# for i in range(3):
#     i = n.pop()
#     n.insert(0, i)
# print(n)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i, j in d.items():
#     print(j, end='')

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i, j in d.items():
#     print(i, j, end=' ')

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i, (k, v) in enumerate(d.items()):
#     print(i, (k, v), end=' ')

# h = 'hellopython'
# d = {}
# for i in h:
#     d[i] = h.count(i)
# print(d)

# h = 'hellopython'
# count = 0
# for i in h:
#     count += 1
#     print(count)

# h = 'hellopython'
# from collections import defaultdict
# dd = defaultdict(int)
# for i in h:
#     dd[i] += 1
# print(dd)

# s = 'hi python welcome to banglore'
# l = s.split()
# d = {}
# for w in l:
#     d[w] = l.count(w)
# print(d)

# s = 'hi python welcome to banglore'
# from collections import defaultdict
# dd = defaultdict(int)
# l = s.split()
# for w in l:
#     dd[w] += 1
# print(dd)

# s = 'hi python welcome to banglore'
# l = s.split()
# d = {}
# for w in l:
#     d[w] = len(w)
# print(d)
# s = 'hi python welcome to banglore'
# d = {}
# l = s.split()
# for w in l:
#     if len(w) % 2 == 0:
#         d[w] = len(w)
# print(d)

# s = 'python is a language, python programming is easy'
# l = s.split()
# d = {}
# for w in l:
#     if w[0] in 'aeiouAEIOU':
#       d[w] = len(w)
# print(d)

# s = 'python is a language, python programming is easy'
# l = s.split()
# d = {}
# for w in l:
#     if l.count(w) == 1:
#         d[w] = l.count(w)
# print(d)

# d = {'a': 'hello', 'b': 10, 'c': 'hai', 'd': 'perl'}
# for k, v in d.items():
#     if isinstance(v, str):
#         d[k] = v[::-1]
# print(d)

# n = ['apple', 'java', 'google', 'python', 'java', 'apple']
# d = {}
# for i in n:
#     count = n.count(i)
#     if count > 1:
#         d[i] = n.count(i)
# print(d)

# s = 'python is a language, python programming is easy'
# l = s.split()
# d = {}
# for i in l:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]
# print(d)

# from collections import defaultdict
# dd = defaultdict(list)
# for i in l:
#     dd[i[0]] += [i]
# print(dd)
#
# s = 'hello world'
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)

# n = ['apple', 'java', 'google', 'python', 'perl', 'ice', 'onion']
# d = {}
# for i, j in enumerate(n):
#     d[j] = i
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'r': 672}
# p = {}
# for i, j in d.items():
#     p[j] = i
# print(p)

# s = 'hello'
# res = {j: i for i, j in enumerate(s)}
# print(res)

# d = 'hi welcome to python'
# l = d.split()
# res = {i: len(i) for i in l}
# print(res)

# s = 'hello python welcome'
# res = {i: s.count(i) for i in s}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {i: l.count(i) for i in l}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {i: l.count(i) for i in l if len(i) % 2 == 0}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {j: i if len(j) % 2 == 0 else j[::-1] for i, j in enumerate(l)}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {i: len(i) for i in l if i[0] in 'aeiouAEIOU'}
# print(res)

# s = 'helloworld'
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)

# n = ['apple', 'java', 'google', 'python', 'java', 'apple']
# from collections import defaultdict
# dd = defaultdict(list)
# for i, j in enumerate(n):
#     dd[j] += [i]
# print(dd)

# f = ['amazon.in', 'apple.txt', 'yahoo.in', 'google.txt', 'face.txt']
# d = {}
# for i in f:
#     l = i.split('.')
#     if l[1] not in d:
#         d[l[1]] = [l[0]]
#     else:
#         d[l[1]] += [l[0]]
# print(d)

# s = 'hello world welcome to python'
# d= {}
# for i in s:
#     if s.count(i) > 1:
#         d[i] = s.count(i)
# print(d)

# n = ['apple', 'java', 'google', 'python', 'java', 'apple']
# d = {}
# for item in n:
#     if n.count(item) > 1:
#         d[item] = n.count(item)
# print(d)

# s = 'hello'
# print(sorted(s))

# s = [5, 4, 8, 6, 11, 24, 0, 8, 1, 2, 3]
# print(sorted(s))

# l = ['python', 'java', 'ruby', 'perl']
# print(sorted(l, key= lambda item: item[-1]))

# set = {'python', 'c', 'men', 'perl', 'ice'}
# print(sorted(set, key= lambda item: item[-1]))

# d = {'a': 3, 'b': 7, 'c': 9, 'd': 0.7}
# print(sorted(d.items(), key= lambda item: item[-1]))

# l = ['python', 'java', 'c', 'perl', 'true']
# print(sorted(l, key= lambda item: len(item)))

# l = ['python', 'java', 'c', 'perl', 'true']
# print(sorted(l, key= len, reverse= True))

# s = 'python is a programming language'
# l = s.split()
# m, *rest,  n = sorted(l, key=len)
# print(m, n)

# s = 'python is a programming language'
# l = s.split()
# m, *rest, n = sorted(l, key= len)
# print((m, len(m)), (n, len(n)))

# l = ['python', 'java', 'c', 'perl', 'true']
# print(sorted(l, key= lambda item: item[-1]))

# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.items(), key= lambda item: item[-1]))

# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.items(), key = lambda item: item[-1]))

# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.values(), key = lambda item: item))

# l = [('delhi', 32), ('mumbai', 27), ('kolkata', 30)]
# print(sorted(l, key= lambda item: item[-1]))

# s = 'hi how are you how is your health'
# l = s.split()
# d = {item: l.count(item) for item in l}
# res = (sorted(d.items(), key= lambda item: item[-1]))
# print(res[-1])

# s = 'hi how are you how is your health'
# l = s.split()
# d = {item: len(item) for item in l}
# res = (sorted(d.items(), key= lambda item: item[-1]))
# print(res[-1])

# s = 'hi how are you how is your health'
# l = s.split()
# d = {item: len(item) for item in l if l.count(item) == 1}
# res = (sorted(d.items(), key= lambda item: item[-1]))
# print(res[-1])

# l = ['hello', 'ball', 'zebra', 'yak', 'apple']
# print(sorted(l))

# s = 'this world is not enough'
# l = s.split()
# print(sorted(l, key= len))

# l = ['hello', 'ball', 'zebra', 'yak', 'apple']
# print(sorted(l, key= lambda item: item[-1]))

# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.items(), key= lambda item: len(item[0])))
#
# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.items(), key= lambda item: item[-1]))

# s = 'hi hello hi hi hiiiiii'
# l = s.split()
# d = {item: s.count(item) for item in l}
# res = sorted(d.items(), key= lambda item: item[-1])
# print(res[-1])

# p = {'acm': 45.6, 'aapl': 612.7, 'ibm': 204.6, 'hpq': 37.4, 'fb': 10.75}
# res = {k: v for k, v in p.items() if v > 40.0}
# print(sorted(res, key= lambda item: item[-1]))

# s = 'this is a programming language and programming is fun'
# l = s.split()
# d = {item: len(item) for item in l if l.count(item) == 1}
# res = sorted(d.items(), key= lambda item: item[-1])
# print(res[-1])

# d = {'gmail': 5, 'apple': 3, 'walmart': 8, 'flipkart': 7}
# print(sorted(d.items(), key= lambda item: len(item[0])))

# n = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'apple', 'gmail', 'gmail', 'gmail']
# for i, j in enumerate(n):
#     d[j] += [i]

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for item, value in d.items():
#     if isinstance(value, str):
#         d[item] = value[::-1]
#     else:
#         d[item] = value
# print(d)

# n = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'apple', 'gmail', 'gmail', 'gmail']
# d = {}
# for item in n:
#     if n.count(item) > 1:
#         d[item] = n.count(item)
# print(d)

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# d1 = {}
# for k, v in d.items():
#     d1[v] = k
# print(d1)

# l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 88, 99, 100]
# e = [index for index, item in enumerate(l) if item % 2 == 0]
# o = [index for index, item in enumerate(l) if item % 2 != 0]
# d = {item1: item2 for item1, item2 in zip(e, o)}
# print(d)

# l = ['python', 'java', 'perl', 'PHP', 'python', 'js', 'c++', 'js', 'python', 'ruby']
# r = (item for item in l if item[0] in 'pP')
# print(r)

# l = 'madam'
# for item in l:
#     if item == reversed(item):
#         print('is palindrome')
# def func(args):
#     l = ''
#     for i in args:
#         l = i + l
#     if l == args:
#         print('palindr')
#     else:
#         print('not palinf')
#
#
# func('mom')

# print even no from 1 to 50
# def func(s,e):
#     for i in range(s, e):
#         if i % 2 == 0:
#             print(f"{i} is even")
#         else:
#             print(f'{i} is odd')
#
#
# func(1, 50)

# print prime no from 2 to 10
# def func(s, e):
#     l = []
#     for n in range(s, e):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             l.append(n)
#     return l
#
#
# print(func(2, 10))

"waf to print index, char of a string"
# def func(string):
#     for index, item in enumerate(string):
#         print(item, index)
#
#
# func('helloworld')

# path = r"C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#     for line in file:
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(line_no, line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         l = line.split()
#         for line in l:
#             count += 1
#     print(count)

# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         l = line.count(' ')
#         count += l
#     print(count)

# with open(path) as file:
#     count = 0
#     for line in file:
#         for l in line.split():
#             if l[0] in 'aeiouAEIOU':
#                 count += 1
#     print(count)

# with open(path) as file:
#     from collections import defaultdict
#     dd = defaultdict(int)
#     for line in file:
#         for l in line.split():
#             dd[l] += 1
#     # print(dd)
#
# l = ['line', 'pen', 'men', 'hugs', 'men']
# from collections import defaultdict
# dd = defaultdict(int)
# for i in l:
#     dd[i] += 1
# print(dd)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\access-log.txt'
# with open(path) as file:
#     l = []
#     for line in file:
#         word = line.split()
#         l.append(word[0])
#     print(l)

# with open(path) as file:
#     from collections import Counter
#     l = []
#     for line in file:
#         if line.strip():
#             list = line.split()
#             l.append(list[0])
#     ip = Counter(l)
#     print(ip)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\data.txt'
# with open(path) as file:
#     from collections import Counter
#     l = []
#     for line in file:
#         if line.strip():
#             word = line.split()
#             l.append(word[1])
#     p = Counter(l)
#     # print(p)
#
# with open(path) as file:
#     from collections import defaultdict
#     dd = defaultdict(int)
#     for line in file:
#         if line.strip():
#             word = line.split()
#             dd[word[1]] += 1
#     print(dd)
#
# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\football.txt'
# with open(path, encoding= 'UTF-8') as file:
#     from collections import Counter
#     l = []
#     for line in file:
#         if line.strip():
#             word = line.split()
#             l.append(word[1])
#     p = Counter(word[1])
#     print(p)

path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log'
# with open(path) as file:
#     l = []
#     from collections import Counter
#     for line in file:
#         if line.strip():
#             p = line.split()
#             for i in p:
#                 l.append(i)
#     res = Counter(l)
#     print(res)
# l = [1, 2, 3, 4, 5]
# res = [(i, j) for i, j in enumerate(l)]
# print(res)

# l = [1, 2, 3, 4, 5]
# res = [item for item in l if item % 2 == 0]
# print(res)

# l = [1, 2, 3, 4, 5]
# p = []
# o = []
# for item in l:
#     if item % 2 == 0:
#         p.append(item)
#     else:
#         o.append(item)
# print(p, o)

# l = ['python', 'node js', 'men', 'pen', 'java', 'selenium']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)

# l = ['java', 'python', 10, True, 3+6j]
# res = [item if isinstance(item, str) else str(item)[::-1] for item in l]
# print(res)

# l = ['python', 'onion', 'men', 'eat', 'envi', 'apple', 'aero', 'engine']
# res = [item if item[0] in 'aeiou' else item[::-1] for item in l]
# print(res)

# s = {1, 2, 3, 4, 5, 6, 7, 8}
# res = {(item * item) for item in s}
# print(res)

# s = 'helloworld'
# res = {index: item for index, item in enumerate(s)}
# print(res)

# s = 'hello python welcome to python'
# res = {item: len(item) for item in s}
# print(res)

# s = 'helloworld'
# res = {item: s.count(item) for item in s}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {item: l.count(item)for item in l if l.count(item) == 1}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {item: l.count(item) for item in l if len(item) % 2 == 0}
# print(res)

# s = 'python is a language, python programming is easy'
# l = s.split()
# res = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(l)}
# print(res)

# l = ['apple', 'google', 'yahoo', 'facebook', 'men', 'pen', 'java']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)

# l = ['python', 'java', 'pen', 'phone', 'PUP', 'perl']
# res = [item for item in l if item[0] in 'pP']
# print(res)

# l = ['apple', 'google', 'yahoo', 'facebook', 'men', 'pen', 'java']
# res = [item for item in l if len(item) < 6]
# print(res)
# l = ['apple', 'google', 'yahoo', 'facebook', 'men', 'pen', 'java']
# res = [(item, len(item)) for item in l]
# print(res)

# l = ['apple', 10, '90', 'google', True, 9+76j]
# res = [item for item in l if isinstance(item, (int, float, complex))]
# print(res)

# l = [1, 2, 3, 4, 5]
# res = [(j ** i) for i, j in enumerate(l)]
# print(res)

# l = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# p = 4
# res = [item for item in l if item == p]
# print(res)

# res = [item for item in range(1, 40) if item % 2 == 0]
# print(res)

# l = ['apple', 'google', 'men', 'pen']
# n = 3
# for i in range(n):
#     x = l.pop()
#     l.insert(0, x)
# print(l)
# l = [1, 2, 3, 4]
# m = lambda item: item % 2 == 0
# p = map(m, l)
# print(list(p))
# import re
# s = 'hello hi wel come to hospet'
# l = s.split()
# r = re.findall(r'\bh\w\b', s)
# print(r)
#
# l = [1, 2, 3, 4, 5, 6, 7]
# def even(num):
#     if num % 2 == 0:
#         return num
#
# p = filter(even, l)
# print(list(p))

# l = ['pen', 'mom', 'union', 'madam', 'anna', 'eat']
# def fun(*args):
#     for item in args:
#         if item == item[::-1]:
#             return item
#
# p = filter(fun, l)
# print(list(p))

# l = ['pen', 'mom', 'union', 'madam', 'anna', 'eat']
# def func(*args):
#     for item in args:
#         if item[0] in 'aeiou':
#             return item
#
# p = filter(func, l)
# print(list(p))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def func(*args):
#     for item in args:
#         if item % 2 == 0:
#             return item * item
#
#
# p = filter(func, l)
# print(list(p))

# n = ['apple', 'google', 'java', 'gmail', 'flipkart', 'instagram', 'microsoft']
# l = []
# for item in n:
#     if len(item) < 6:
#       l.append(item)
# print(l)

# for item in n:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

# p = 3
# for item in range(p):
#     x = n.pop()
#     n.insert(0, x)
# print(n)

#wap to print nth line
# n = 5
# with open(path) as file:
#     for i, j in enumerate(file):
#         if i == n:
#             print(j)

# by using islice
#
from itertools import islice
# n = 3
# with open(path) as file:
#     res = islice(file, n, n+1)
#     print(list(res))

#wap to print n lines
# with open(path) as file:
#     res = islice(file, n)
#     print(list(res))

#wap to print last n lines using normal method(islice)
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         pass
#     file.seek(0)
#     res = islice(file, line_no-3, line_no)
#     print(list(res))

#wap to print last n lines using normal method(deque)
# n = 4
# from collections import deque
# with open(path) as file:
#     res = deque(file, n)
#     print(list(res))

# def func(*args):
#     for i in args:
#         if isinstance(i, int):
#             print(i)
#
# func('hello', 10, 29, 'pen', 'len')
# def func(*args):
#     for _ in args:
#         print(_[::-1])
#
# func('hello', 'pen', 'men')

# def func(*args):
#     return len(args)
#
# print(func(1, 2, 3, 4, 5, 6,))

# d = {'a': 1, 'b': 4, 'c': 9, 'd': 2}
# r = sorted(d.items(), key= lambda item: item[-1])
# print(r)

# s = 'hi how are you how is your heaith'
# d = {item: s.count(item) for item in s if s.count(item) > 1}
# p = sorted(d.items(), key= lambda item: item[-1])
# print(p[-1])
#
# l = 'this world is not enought'
# s = l.split()
# print(sorted(l, key=len))

# l = ['hello', 'pen', 'one', 'men']
# print(sorted(l, key= lambda item: item[-1]))

# d = {'pen': 10, 'women': 2, 'live': 9}
# print(sorted(d.items(), key= lambda item: len(item[0])))

# def func(*args):
#     count = 0
#     for _ in args:
#         count += 1
#     return count
#
# print(func('hai', 'pen', 'kite', 'we', 'one'))

# def func(*args):
#     l = []
#     for item in args:
#         if item[0] in 'aeiou':
#             l.append(item)
#     return l
#
# print(func('eat', 'pen', 'men', 'one', 'apple'))

# n = 7
# def func(n):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#         else:
#             print(f'{n} is prime no')

#decorators
# import time
# def outer(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         print('base case is done')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print (a + b)
#
# add(2, 3)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = abs(func(*args, **kwargs))
#         return res
#     return wrapper
# @outer
# def fun(a, b):
#     print(a - b)
#
# fun(-2, 5)

# s = 'hello welcome to python'
# l = s.split()
# print(l, end=',')

# s = 'hello'
# r = ''
# for i in s:
#     r = i + r
# print(r)

# s = 'pen'
# if s == s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print('not palindrome')

# s = 'hello world, welcome to python'
# l = s.split()
# p = (sorted(l, key=len))
# print(p[-1])

# import re
# s = 'sony12india567pvt2ltd'
# sum = 0
# for item in s:
#     sum += 1
# p = (re.findall(r'[0-9]', s))
# print(sum)

# d = {'a': 'hello', 'b': 10, 'c': 2.4, 'd': 'java'}
# # k = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = (value[::-1])
#     else:
#         d[key] = (value)
# print(d)

# n = ['apple', 'yahoo', 'google' 'gmail', 'yahoo', 'walmart']
# d = {}
# p = {((i: len(i)) for i in n if len(i) % 2 == 0)}
# print(p)

# s = 'HaLlo wORld'
# print(s.lower())

# s = 'APPLE IF fRuit'
# print(s.upper())

# m = 'hello world, hello universe'
# print(m.count('e'))

# s = 'hello world'
# print(s.replace('world', by 'universe'))

# s = 'hello world'
# count = 0
# for i in s:
#     count += 1
# print(count)

# s = 'helo world welcome to python'
# r = ''
# for i in s:
#     r = i + r
# print(r)
# print(len(s))

# s = 'hello world'
# print(s.replace('world', 'universe'))

# s = 'hello'
# print(list(s))
# print(''.join(s))

# s = 'hello world welcome to python'
# l = s.split()
# print(l, end=',')
# print(' '.join(l))

# s = 'hello world'
# for item in s[::2]:
#     print(item, end='')
#
# print(s[::2])

# s = 'hello'
# for i in s:
#     print(ord(i))

# a, b = 2, 4
# b, a = a, b
# print(b)
# print(a)

# a =[1, 2, 3,4]
# b = ['hi', 'hello', 'pen', 'madam']
# print(*a, *b)

# s = 'madam'
# if s == s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')

# s = 'praveen'
# o = 'e'
# for index, item in enumerate(s):
#     if item == o:
#         print(f'{item} is in {index} index')
#         break

# s = 'hello world wecome to python programming hi there'
# l = s.split()
# from collections import defaultdict
# dd = defaultdict(list)
# for i in l:
#     dd[i[0]] += [i]
# print(dd)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
# @outer
# def sub(a, b):
#     return(a - b)
#
#
# print(sub(10, -3))

# num = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# num.sort()
# print(num[-1])

# def func(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item)
#         else:
#             print(str(item)[::-1])
#
# func('pen', 'home', 2.89, 10.98, 'men', 'madam')

# s = 'hi how are you'
# l = s.split()
# res = [item[::-1] for item in l]
# print(res)

# s = 'hi how are you'
# l = s.split()
# res = [item[::-1] for item in l]
# print(res[::-1])

# res = lambda a, b: (a + b)
# print(res(1, 2))

# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

# l = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# d = []
# for item in l:
#     if item not in d:
#         d.append(item)
# print(d)

# s = 'hello world, welcome to python'
# l = s.split()
# res = sorted(l, key=len)
# print(res[-1])

# d = {'a': 'hello', 'b': 10, 'c': 96.3, 'd': 'world'}
# re = {k: v[::-1] if isinstance(v, str) else v for k, v in d.items()}
# print(re)

# t = ['1', '2', '3', '4']
# print(''.join(t))

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# for i in b:
#     if i not in a:
#         print(i)

# def func(*args):
#     if len(args) > 5:
#         print('len of argument is > 5')
#     else:
#         print('len of arguments is < 5')
#
#
# func('hello', 'welcome', 'colour')

# a = [1, 2, 3, 4, 5, 6]
# for i in a[::-1]:
#     print(i)

# def func(string, n):
#     if n == 0:
#         return string[1::2]
#     elif n == 1:
#         return string[::2]
#     else:
#         return 'not found'
#
#
# print(func('TRACXN', 1))

# import re
# s = "Sony12India567Pvt3ltd"
# r = re.findall(r'[0-9]', s)
# sum = 0
# for i in r:
#     sum += 0
# print(sum)
#
# sum = 0
# for i in s:
#     if '0' <= i <= '9':
#         sum += 1
# print(sum)

#
# import re
# s = "Sony12India567Pvt2ltd"
# rr = re.findall(r'[\d]+', s)
# total = 0.00
# for item in rr:
#     total += int(item)
# print(total)

# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isnumeric():
#         print(i)

# s = 'helloworld'
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)

# s = 'helloworld'
# r = {i: s.count(i) for i in s if s.count(i) > 1}
# print(r)

# s = 'hello world welcome to python'
# r = [item for item in s[::2]]
# print(r)


# a = [1, 2, 3, 4, 5]
# res = lambda number: number * number
# b = [res(item) for item in a]
# print(b)

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# re = [item for item in names if len(item) % 2 == 0]
# print(re)

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {item: len(item) for item in names if len(item) % 2 == 0}
# print(d)

# a = [1, 2, 3, 4, 5]
# p = lambda item: item * item
# res = map(p, a)
# print(list(res))

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# e_sum = 0
# for i in l:
#     in_sum = 0
#     for item in i:
#         in_sum += item
#         e_sum += item
#     print(in_sum)
# print(e_sum)

# words = ["hi", "hello", "python"]
# for item in words[::-1]:
#     print(item[::-1])

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# print(t1 + t2)
# print((*t1, *t2))

# res = [item for item in range(1, 50) if item % 2 == 0]
# print(res)

# s = "This is a Programming language and Programming is fun"
# l = s.split()
# d = {item: len(item) for item in l if l.count(item) == 1}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])
#
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# d = {item: names.count(item) for item in names if names.count(item) > 1}
# print(d)

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# from collections import defaultdict
# dd = defaultdict(int)
# for i in names:
#     dd[i] += 1
# print(dd)

# def func(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return f'{n} is not prime'
#             break
#         else:
#             return f'{n} is prime'
#
#
# print(func(5))

# numbers = [10, 20, 30, 40, 50]
# res = max(numbers)
# print(res)
#
# p = 50
# for item in numbers:
#     if item == p:
#         print(item)
#         break

# p = 3572
# o = str(p)
# print(o)
# l = o.split()
# for i in l:
#     print(i[-1])

# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
# res = {item: words.count(item) for item in words if words.count(item) > 1}
# print(res)

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d = {i: names.count(i) for i in names if names.count(i) > 1}
# print(d)

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for i in items:
#     if isinstance(i, (int, float)):
#         print(i)

# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# n = 3
# for i in range(n):
#     x = names.pop()
#     names.insert(0, x)
# print(names)

# import re
# sentence = """Hello world welcome to Python Hi  How are you. Hi how are you"""
# r = re.findall(r'\s', sentence)
# print(r)
# print(len(r))

# s = 'helloworld'
# d =  [i for i in s if s.count(i) == 1]
# print(d)

# s = 'helloworld'
# d = [i for i in s if not i in 'aeiouAEIOU']
# print(d)

# import re
# sentence = "Hi How are You WelCome to PytHon"
# p = re.findall(r'[A-Z]', sentence)
# print(len(p))

# s = 'helloworld'
# p = 'o'
# for index, item in enumerate(s):
#     if item == p:
#         print(f'The {item} is in index {index}')
#         break

# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# x = []
# y = []
# for i in a:
#     if i % 2 != 0:
#         x.append(i)
#     else:
#         y.append(i)
# print(x)
# print(y)

# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# res = sorted(a)
# print(res)
# p = [i for i in res if i % 2 != 0]
# o = [i for i in res if i % 2 == 0]
# print(p)
# print(o)

# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
#dought
# count = 0
# for i in s:
#     if 'a' <= i <= 'z':
#         count += 1
# print(count)
#
# import re
# r = re.findall(r'\w', s)
# d = {i: s.count(i) for i in r}
# print(d)

# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = {}
# for i in items:
#     l = i.split('-')
#     if l[1] not in d:
#         d[l[1]] = [l[0]]
#     else:
#         d[l[1]] += [l[0]]
# print(d)

# s = '@hello12world34welcome!123'
# res = [i for i in s if not '0' <= i <= '9']
# print(res)

# s = "Hi there! How are you:) How are you doing today!"
# l = s.split()
# d = {}
# for i in l:
#     if 'a' <= i <= 'z' and 'A' <= i <= 'Z':
#         d[i] = l.count(i)
#         print(d)

# import re
# r = re.findall(r'\w+', s)
# p = {i: len(i) for i in r}
# print(len(p))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# l = []
# l.append(max(numbers))
# print(l)

# s = 'HellO WOrlD'
# l = ''
# for i in s:
#     if 'a'<= i <= 'z':
#         l += chr(ord(i)-32)
#     elif 'A' <= i <='Z':
#         l += chr(ord(i)+32)
#     else:
#         l += i
# print(l)

# a = 10
# b = 90
# a, b = b, a
# print(a, b)

# p = [1, 2,3]
# o = [2, 3, 4]
# print(p + o)
# print(*p, *o)

# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(9, line)

# s = 'madam'
# if s ==s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} not palindrome')

# s = 'hello'
# p = 'l'
# for index, i in enumerate(s):
#     if i == p:
#         print(f'{i} is in {index} index')
#         break

# s = 'hello world hi weilcome'
# l = s.split()
# d = {}
# for i in l:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]
# print(d)

# s = 'HelLO'
# l = []
# for i in s:
#     if 'a' <= i <= 'z':
#         up = i.upper()
#         l.append(up)
#     elif 'A' <= i <= 'Z':
#         lower = i.lower()
#         l.append(lower)
#     else:
#         l += i
# print(''.join(l))

# s = 'hellohai'
# c = ''.join(['-' if s.count(i) > 1 else i for i in s])
# print(c)

#get count of number of instance of a class that is being created
# class login:
#     login_count = 0
#     def __init__(self):
#         login.login_count+=1
# u1 = login()
# print(u1.login_count)
# u2 = login()
# print(u1.login_count)

#program to read a random line in a file
# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log'
# from itertools import islice
# with open(path) as file:
#     line = islice(file, 10, 12)
#     print(list(line))

#waf take list of string and integer, if string keep as it is and interger reverse
# def func(*args):
#     for i in args:
#         if isinstance(i, str):
#             print(i)
#         else:
#             print(str(i)[::-1])
#
# func('ear', 'python', 19, 2+7j)

#class name is simple and itertion capability
# class simple:
#     def __init__(self, items):
#         self.items = items
#
#     def __iter__(self):
#         return iter(self.items)
#
# s = simple([1, 2,3,4, 5])
# for i in s:
#     print(i)

#python program to get output
# s = 'Hi How are you'
# l = s.split()
# c = [i[::-1] for i in l]
# print(c)                 #['iH', 'woH', 'era', 'uoy']
# print(' '.join(c))        #iH woH era uoy

#python program to get o/p      #['uoy', 'era', 'woH', 'iH']
# s = 'Hi How are you'
# l = s.split()
# c = [i[::-1] for i in l]
# print(c[::-1])

#wap to add two numbers by lambda function
# res = lambda a, b: a + b
# print(res(2, 5))

#wap to get below o/p
# a = [1, 2, 3]
# b = [4, 5,6]
# print([a, b])      #[[1, 2, 3], [4, 5, 6]]
# print((a, b))     #([1, 2, 3], [4, 5, 6])

#wap to remove duplicates in below list
# i = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# l = []
# c = [l.append(item) for item in i if item not in l]
# print(l)       #[1, 2, 3, 4, 5]

#find longest word in sentence
# s = 'Hello world. welcome to python programing'
# l = s.split()
# d = {i: len(i) for i in l}
# res = sorted(d.items(), key= lambda item: item[-1])       #1
# res = sorted(d.items(), key=len)                          #2
# print(res[-1])     #('programing', 10)

#wap to reverse value, if value is string
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#        d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)                #{'a': 'olleh', 'b': 100, 'c': 10.1, 'd': 'dlrow'}

#wap to get 12345
# t = ['1', '2', '3', '4', '5']
# print(''.join(t))      #12345

#how to get values that are in list b but not in a
# a = [1, 2, 3]
# b = [1,2, 3, 4,5]
# for item in b:
#     if item not in a:
#         print(item, end=' ')            #4 5

#take function as variable number of positional arguments, how to check if the arguments that are more than 5
# def func(*args):
#     if len(args) > 5:
#         print('len of args > 5')
#     else:
#         print('len of args < 5')
#
#
# func(1, 2, 3, 4)         #len of args < 5
# func(1, 2, 3, 4, 5, 6, 7)     #len of args > 5

#128 Write a program to get the below output
# o/p should be ['b', 'd']
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# key = list(d.keys())
# print(key)
# res = [i for i in key[::2]]
# print(res)
# print(res)

#129 Can we have multiple init methods in a class
# class hello:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# res = hello(5, 2, 3)
# print(res.a)
# print(res.b)
# print(res.c)
# res = hello(2, 3)
# print(res)

#wa decorator to reverse string
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
# @outer
# def func(string):
#     return string
#
# print(func('hello'))

#127 Write a decorator to prefix +91 to the original phone numbers
# numbers = [1234567890, 123456790, 1234567890]
# def outer(func):
#     def wrapper(*args, **kwargs):
#         numbers, = args
#         res = ["+91-"+str(number) for number in numbers]
#         return func(res)
#     return wrapper
# @outer
# def hello(numbers):
#     for number in numbers:
#         print(number)

#125 What is the output of the below function call
# class demo:
#     def greet(self):
#         print("hello world")

    # def greet(self):
    #     print('hello univers')

# a = demo()
# print(a.greet())

#124 Write a python program to get the below output  # o/p ['Y3', 'c2', 'A4', 'a2']
# word = "AAAAaaccYYY"
# res = set(word)
# print(res)
# p = [''.join((i, str(word.count(i)))) for i in res]
# print(p)

#122 Print all the missing numbers from 1 to 20 in the below list
# l = [1, 4, 6, 8,12, 15, 20]
# for i in range(1,20):
#     if not i in l:
#         print(i, end=' ')      #2 3 5 7 9 10 11 13 14 16 17 18 19

# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1.copy()
# print(l2)
# res = [l1.remove(i) for i in l2 if l1.count(i) > 1]
# print(l1)

#120 Write a program to print all the number which are starting with 8
# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# import re
# for i in numbers:
#     r = re.findall(r'^8', i)
#     if r:
#         print(i)

#119 Write a program to filter out even and odd numbers in the given string
# sentence = 'hello 123 world 456 welcome to python498675634'
# import re
# r = re.findall(r'[0-9]', sentence)
# p = [i for i in r if int(i) % 2 == 0]
# o = [i for i in r if int(i) % 2 != 0]
# print(p)
# print(o)

# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# l = []
# import re
# w1 = re.findall(r'\d', word1)
# w2 = re.findall(r'\d', word2)
# for n, m in zip(w1, w2):
#     print(l.append(int(n) + int(m)))


# def anagram(str1, str2):
#     if str1.upper() == str2.upper():
#         return False
#     str1 = sorted(str1.upper())
#     str2 = sorted(str2.upper())
#     if str1 == str2:
#         return True
#     else:
#         return False
#
# print(anagram('ate', 'eat'))
# print(anagram('life', 'file'))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log'
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
# print(count)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log'
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(line_no, line)


# l = [[1,2,3],[4,5,6],[7,8,9]]
# e = 0
# for i in l:
#     i_ = 0
#     for item in i:
#         i_ += item
#         e += item
#     print(i_)
# print(e)

# r = [sum(i) for i in l]
# print(r)
# print(sum(r))

# words = ["hi", "hello", "python"]
# r = [i[::-1] for i in words[::-1]]
# print(r)

# t = (1, 2, 3)
# t2 = (10, 90)
# print(t + t2)

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = 'net'
# print(d)

# import os
# print('Enter Number of Seconds to shutdown system: ')
# sec = int(input())
# strone = 'shutdown /s /t'
# strTwo = str(sec)
# str = strone + strTwo
# os.system(str)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.log' \
#        r''
# import re
# with open(path) as file:
#     count = 0
#     for line in file:
#         r = re.findall(r'\s', line)
#         if r:
#             count += len(r)
# print(count)

#54 Grouping anagrams.
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# from collections import defaultdict
# dd = defaultdict(list)
# for item in words:
#     s = ''.join(sorted(item))
#     dd[s].append(item)
# print(dd)

# res = [i for i in range(1, 51) if i % 2 == 0]
# print(res)

# s = "This is a Programming language and Programming is fun"
# l = s.split()
# d = {i: len(i) for i in l if l.count(i) == 1}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

names = ['apple', 'google', 'apple', 'yahoo', 'google']
# d = {}
# d = {i for i in names if names.count(i) > 1}
# print(d)
# from collections import defaultdict
# dd = defaultdict(int)
# for i in names:
#     if names.count(i) > 1:
#         dd[i] += 1
# print(dd)
# for i in names:
#     if names.count(i) > 1:
#         print(i)

names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# from collections import defaultdict
# d = defaultdict(int)
# for i in names:
#     d[i] += 1
# print(d)
# d = {}
# for i in names:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

#prime number
# def func(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return f'{n} is not prime'
#             break
#     else:
#         return f'{n} is prime'
#
# print(func(7))

#max number of this
# numbers = [10, 20, 50, 40, 50]
# p = 50
# l = []
# for i in numbers:
#     if i == p:
#         l.append(i)
# print(l)

# numbers = sorted(numbers)
#
# print(numbers)
# l = []
# l.append(max(numbers))
# numbers.remove(max(numbers))
# for i in numbers:
#  if i in l:
#      l.append(i)
#
# print(l)


# for i in str(numbers):
#     s= int(i)
#     r = max(s)
#     l.append(r)
# print(l)

# r = 3572
# p = str(r)
# print(p[-1])
#
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
# d = {i: words.count(i) for i in words if words.count(i) > 1}
# print(d)

#69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.
# def is_perfect_square(n):
#     sq = int(n **0.5)
#     if sq * sq == n:
#         return True
#     return False
#
# print(is_perfect_square(16))

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d= {i: names.count(i) for i in names if names.count(i) > 1}
# print(d)


# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for i in items:
#     if isinstance(i, (int, float)):
#         print(i)

#triangle pattern
# for i in range(1, 6):
#     print(f"{'*'*i:<5}")

# for i in range(1, 6):
#     print(f"{'*'*i:>5}")

# for i in range(1, 6):
#     print(f"{'* '*i:^10}")

# for i in range(6, 0, -1):
#     print((f"{'*'*i:<5}"))

# for i in range(6, 0, -1):
#     print(f"{'*'*i:>6}")

# for  i in range(6, 0, -1):
#     print(f"{'* '*i:^12}")


# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
# a = {'iPhone', 'Mac', 'iWatch'}
# b = {'Gmail', 'Maps', 'Google Drive'}
# c = {'Windows', 'One Drive'}
# from collections import defaultdict
# d = defaultdict(list)
# for item in all_products:
#     if item in a:
#         d['apple'].append(item)
#     elif item in b:
#         d['google'].append(item)
#     elif item in c:
#         d['window'].append(item)
# print(d)

# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# n = 3
# for item in range(n):
#     x = names.pop()
#     names.insert(0, x)
# print(names)

# numbers = [10, 20, 50, 40, 50]
# res = max(numbers)
# print(res)

# for i in numbers:
#     if i == res:
#         print(i)

# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# k = 2
# for i in range(k):
#     x = names.pop()
#     names.insert(0, x)
# print(names)

# ce = """Hello world welcome to Python Hi  How are you. Hi how are you"""
# import re
# re = re.findall(r'\s', ce)
# print(len(re))

# s = 'helloworld'
# d = [i for i in s if s.count(i) == 1]
# print(d)

# s = 'helloworld'
# d = [i for i in s if not i in 'aeiou']
# print(d)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             if line.startswith('#'):
#                 count += 1
# print(count)

# import calendar
# print(calendar.isleap(2012))
# print(calendar.isleap(2018))

# ce = "Hi How are You WelCome to PytHon"
# import re
# res = re.findall(r'[A-Z]', ce)
# print(len(res))

# for i in range(1, 5):
#     print('* '*1)
#     j = i + 1
#     print('* '*j)

# s = 'helloworld'
# for i in s:
#     if s.count(i) > 1:
#         print(i)
#         break

# a = [1, 2, 3]
# b = [2, 3, 6]
# re = b.extend(a)
# print(b)

# l = [10, 20, 50, 30, 50, 40]
# r = sorted(l)
# print(r)
# p = 50
# for i in l:
#     if p == i:
#         print(i)
#         continue

# n = 6
# for i in range(2,n):
#     if i % n == 0:
#         print(f'{n} is prime number')
#         break
# else:
#     print(f'{n} is not prime')

# for n in range(1, 10):
#     if n > 1:
#         for item in range(2, n):
#             if n % item == 0:
#                 print(f'{n} is not prime')
#                 break
#         else:
#             print(f'{n} is prime')

# sentence = "Hi How are You WelCome to PytHon"
# count = 0
# for i in sentence:
#     if 'A' <= i <= 'Z':
#         count += 1
# print(count)

# s = 'helloworld'
# for i in s:
#     if s.count(i) > 1:
#         print(i)
#         break

# s = "hello world welcome to python hello hi how are you hello there"
# l = s.split()
# for index, item in enumerate(l):
#     print(item, index)

# for n in range(1, 51):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n, end=' ')

# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# p = [i for i in a if i % 2 != 0]
# o = [i for i in a if i % 2 == 0]
# print(sorted(p))
# print(sorted(o))

# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# res = [i for i in s if 'a' <= i <= 'z' or 'A' <= i <= 'Z']
# print(res)
# print(len(res))

# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = {}
# for i in items:
#     l = i.split('-')
#     if l[1] not in d:
#         d[l[1]] = l[0]
#     else:
#         d[l[1]] += l[0]
# print(d)

# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# d = {}
# for item in files:
#     l = item.split('.')
#     if l[1] not in d:
#         d[l[1]] = l[0]
#     else:
#         d[l[1]] += l[0]
# print(d)

# s = '@hello12world34welcome!123'
# res = [i for i in s if not '0' <= i <= '9']
# print(res)

# e = "Hi there! How are you:) How are you doing today!"
# import re
# r = re.findall(r'[a-zA-Z]+', e)
# print(r)
# print(len(r))

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = [i for i in num if i % 2 == 0]
# p = [i for i in num if i % 2 != 0]
# print(r)
# print(p)
# print(sorted(r))
# print(sorted(p))
# print({1: p})
# print({0: r})

# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# print(max(numbers))
# r = [i for i in numbers if i == max(numbers)]
# print(r)

# e = "hello world hi apple you yahoo to you"
# l = e.split()
# res = max(l, key=len)
# p = [i for i in res if len(i) == max(len(i))]
# print(list(p))

# def func(*
#     sum = 0
#     for _ in args:
#         sum += len(args)
#     return sum
# print(func([1, 2, 3], (4, 5)))
# print(func([1, 2, 3], (0, 8, 5), 'apple', 'run'))args):

# a = "python@#$%pool"
# import re
# r = re.findall(r'[A-Za-z]+', a)
# print(r)

# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for i in numbers:
#     if i.endswith('5'):
#         print(i)

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# from collections import defaultdict
# d = defaultdict(list)
# for i, j in enumerate(names):
#     d[j] += [i]
# print(d)


# print('banglore\n' *10)

# a = 'hello world hi hello universe how are you happy birthday'
# l = a.split()
# for i in l:
#     if i.startswith('h'):
#         print(i)

# a = 'hello 123 world 567 welcome to 9724 python'
# import re
# res = re.findall(r'[0-9]', a)
# print(res)
# c = [i for i in res if i % 2 == 0]

# ce = 'hello 123 world 456 welcome to python498675634'
# import re
# res = re.findall(r'[0-9]', ce)
# print(res)
# c = [i for i in res if int(i) % 2 == 0]
# p = [i for i in res if int(i) % 2 != 0]
# print(c)
# print(p)

# e = 'hello 123 world 567 welcome to 9724 python'
# import re
# res = re.findall(r'[0-9]', e)
# print(res)
# c = [i for i in res if int(i) % 2 == 0]
# print(c)

# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# c = [i for i in numbers if i.startswith('8')]
# print(c)

# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# res = sorted(l1)
# print(res)
# c = [l1.remove(i) for i in res if res.count(i) > 1]
# print(c)

# l = [1, 4, 8, 12, 14, 19]
# for i in range(1, 20):
#     if not i in l:
#         print(i)

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key in d.keys():
#     print(key, end=' ')
#     for i in key[1::2]:

# s = 'APPLE'
# print(s.lower())

# s= 'hello'
# r = ''
# for i in s:
#     r = i + r
# print(r)

# s = 'hello'
# print(s.upper())

# s = 'hello'
# print(s.count(s))

# s = 'hello'
# print(list(s))
# print(''.join(s))

# s = "Hello welcome to Python"
# l = s.split()
# print(l, end=',')

# s = 'hello world'
# d = [i for i in s[::2]]
# print(s[::2])

# a = 90
# p = 99
# a, p = p, a
# print(p)
# print(a)

# l = [1,3]
# p = [8, 6]
# print(l + p)

# ce = "hello world welcome to python programming hi there"
# l = ce.split()
# from collections import defaultdict
# d = defaultdict(list)
# for i in l:
#     d[i[0]].append(i)
# print(d)

# s = 'apple'
# for i, j in enumerate(s):
#     print(i, j)

# s = 'apple'
# for i in reversed(s):
#     print(i)

# l = ['python', 'java', 'madam', 'pen', 'kite']
# for item in l:
    # print(i)
    # if isinstance(i, int):
    #     print(i)
    # if i == i[::-1]:
    #     print(i)
    # print(i[::-1])
    # if isinstance(i, str):
    #     print(i)
    # else:
    #     print(str(i)[::-1])
    # print((item, index))
    # print(item)
    # print(len(item))
    # if len(item)%2==0:
    #     print(item)
    # else:
    #     print(item[::-1])

# l = ['python', 10, 'mom', 73, 9+6j, 'pen', 'madam']
# c = [i[::-1] if isinstance(i, str) else i for i in l]
# print(c)

# l = ['Amazon', 'madam', 'eat', 'once', 'pen', 'son', 'rice']
# c = [i for i in l if i[0] in 'AEIOUaeiou']
# print(c)

# l = ['youtube.txt', 'amazon.pdf', 'apple.txt', 'flipkart.pdf']
# d = {}
# for i in l:
#     s = i.split('.')
#     if s[1] not in d:
#         d[s[1]] = [s[0]]
#     else:
#         d[s[1]] += s[0]
# print(d)

# l = [10, 20, 30, 40, 20, 50, 40, 80]
# p = 40
# for i, j in enumerate(l):
#     if j == p:
#         print(i)
#         break

# n = 5
# for i in range(2, n):
#     if n% i ==0:
#         print('not prime')
#         break
# else:
#     print('prime')
# for n in range(1, 11):
#     if n > 1:
#         for i in range(2, n):
#             if n%i==0:
#                 break
#         else:
#             print(f'{n} is prime')

# l = [10, 30, 20, 50, 20, 90, 10]
# p = 20
# for i in l:
#     if i == p:
#         continue
#     print(i)

# l = ['madam', 'pen', 'men', 'mom', 'dad']
# p = []
# for i in l:
#     if i == i[::-1]:
#         p.append(i)
# print(p)

# l = {'madam', 'pen', 'men', 'mom', 'dad'}
# o = 'pen'
# for i in l:
#     l.discard(o)
#     break
# print(l)

# s = 'hai'
# p = 'mam'
# for i, j in zip(s, p):
#     print(i, j)

# ce = 'hello 123 world 567 welcome to 9724 python'
# for i in ce:
#     if '0' <= i <= '9':
#         print(i, end=' ')

# d = {'a': 1, 'b': 9, 'c': 4}
# for key, value in d.items():
#     print(key)
#     print(value)
# print(d.items())

# d = {'a': 1, 'b': 9, 'c': 4}
# for index, (key, value) in enumerate(d.items()):
#     print(index, (key, value))

# s = 'hello world'
# d = {i: s.count(i) for i in s}
# print(d)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {i: l.count(i) for i in l}
# print(d)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {i: len(i) for i in l}
# print(d)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {i: len(i) for i in l if len(i) % 2 == 0}
# print(d)
# p ={}
# for i in l:
#     if len(i) % 2 == 0:
#         p[i] = len(i)
# print(p)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {i: len(i) for i in l if i[0] in 'aeiou'}
# print(d)
# p = {}
# for i in l:
#     if i[0] in 'aeiou':
#         p[i] = len(i)
# print(p)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {i: s.count(i) for i in l if s.count(i) == 1}
# print(d)

# d = {'a': 'hello', 'b': 9, 'c': 4, 'd': 'madam'}
# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# d = {}
# for i in n:
#     if n.count(i) == 1:
    # if n.count(i) > 1:
    #     d[i] = n.count(i)
# print(d)

# s = 'python is a progreamming language is easy'
# l = s.split()
# d = {}
# for i in l:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]
# print(d)

# s = 'hello world welcome to python'
# res = {i: s.count(i) for i in s}
# print(res)

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# d = {}
# for index, item in enumerate(n):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

# d = {'a': 'hello', 'b': 9, 'c': 4, 'd': 'madam'}
# d1 = {}
# for key, value in d.items():
#
#     d1[value] = key
# print(d1)

# l = [1, 2, 3, 4, 5]
# c = [i * i for i in l]
# print(c)

# l = [1, 2, 3, 4, 5]
# c = [i for i in l if i % 2 == 0]
# print(c)

# l = [1, 2, 3, 4, 5]
# c = [i for i in l if i % 2 == 0]
# p = [i for i in l if i % 2 != 0]
# print(c)
# print(p)
#
# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# c = [i if len(i) % 2 == 0 else i[::-1] for i in n]
# print(c)

# n = ['apple', 'pen', 'java', 10, 'apple', 5.64, 'men', 4+9j, 'pen', 'java']
# c = [i if isinstance(i, str) else str(i)[::-1] for i in n]
# print(c)

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# c = [i for i in n if i[0] in 'aeiou']
# print(c)

# s = 'hello'
# d = {index: item for index, item in enumerate(s)}
# print(d)

# s = 'hello world welcome to python'
# l = s.split()
# d = {i: len(i) for i in l}
# print(d)

# s = 'hello world'
# d = {i: s.count(i) for i in s}
# print(d)

# s = 'hello world welcome to pythonhello how are you and how is your health'
# l = s.split()
# d = {i: l.count(i) for i in l}
# print(d)

# s = 'hello world welcome to pythonhello how are you and how is your health'
# l = s.split()
# d= {i: l.count(i) for i in l if len(i) % 2 == 0}
# print(d)

# s = 'hello world welcome to python hello how are you and how is your health'
# l = s.split()
# d= {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(l)}
# print(d)

# s = 'hello world welcome to python hello how are you and how is your health'
# l = s.split()
# d = {i: len(i) for i in l if i[0] in 'aeiou'}
# print(d)

# n = ['apple', 'pen', 'java', 19, 2964, 2022, 'apple', 'men', 'pen', 'java']
# d = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(n)}
# print(d)

# s = 'hello world'
# d = {i: ord(i) for i in s}
# print(d)

# l = ['hai', 'mom', 'dad', 'hello']
# p = lambda item: item == item[::-1]
# res = map(p, l)
# print(list(res))

# l = [1, 2, 3, 4, 5]
# p = lambda i: i % 2 == 0
# r = map(p, l)
# print(list(r))
#
# p = lambda i: i * i
# r = map(p, l)
# print(list(r))

# l = ['apple', 'open', 'java', 'pen', 'eat']
# l1 = ['APPLE', 'OPEN', 'JAVA', 'PEN', 'EAT']
# p = lambda i: i.lower()
# r = map(p, l1)
# print(list(r))
#
# p = lambda i: i.upper()
# r = map(p, l)
# print(list(r))
#
# p =lambda i: i[0] in 'aeiou'
# r = map(p, l)
# print(list(r))

# l = [-1, -10, -2022]
# p =lambda i: abs(i)
# r = map(p, l)
# print(list(r))

# l = [1, 2,3, 4]
# p = lambda item, index: item ** index
# r = map(p, enumerate(l))
# print(list(r))

# s = ['amazon.pdf', 'fb.txt', 'apple.txt', 'gmail.pdf']
# d = {}
# for i in s:
#     l = i.split('.')
#     if l[1] not in d:
#         d[l[1]] = l[0]
#     else:
#         d[l[1]] += l[0]
# print(d)

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# from collections import defaultdict
# d = defaultdict(list)
# for index, item in enumerate(n):
#     d[item] += [index]
# print(d)
#
# d = {}
# for i, j in enumerate(n):
#     if j not in d:
#         d[j] = [i]
#     else:
#         d[j] += [i]
# print(d)

# s = 'hello world welcome to python hello how are you and how is your health'
# l = s.split()
# d = {i: len(i) for i in l}
# print(d)

# for item in l:
    # print(item, len(item), end=' ')
    # p = lambda item: (item, len(item))
    # r = map(p, l)
# print(list(r))

# s = 'praveen'
# p = lambda item: (item, ord(item))
# r = map(p, s)
# print(list(r))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def func(*args):
#     for i in args:
#         if i % 2 == 0:
#             return i
# print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# s = 'hello'
# print(sorted(s))

# s = [9, 4, 2,4, 19, 38, 47, 72]
# print(sorted(s))

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# print(sorted(n))

# n = ('apple', 'pen', 'java', 'apple', 'men', 'pen', 'java')
# print(sorted(n))

# n = {'apple', 'pen', 'java', 'apple', 'men', 'pen', 'java'}
# print(sorted(n))

# d = {'a': 5, 'b': 2, 'r': 19}
# print(sorted(d.items()))

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# print(sorted(n, key=len))

# s = 'hello world welcome to python hello how are you and how is your health'
# l = s.split()
# s, *rest, l = sorted(l, key=len)
# print(s, l)
# print((s, len(s)), (l, len(l)))

# n = ['apple', 'pen', 'java', 'apple', 'men', 'pen', 'java']
# print(sorted(n, key=lambda item: item[0]))

# s = {'gmail': 4, 'apple': 2, 'walmart': 94, 'flipkart': 421}
# r = sorted(s, key= lambda item: item[0])
# print(r)

# s = {'gmail': 4, 'apple': 2, 'walmart': 94, 'flipkart': 421}
# r = sorted(s.items(), key= lambda item: item[-1])
# print(r)

# s = 'hi how are you how is your health'
# l = s.split()
# d = {i: l.count(i) for i in l if l.count(i) > 1}
# d = {i: l.count(i) for i in l if l.count(i) == 1}
# print(d)
# print(d)
# print(sorted(d.items(), key=lambda item: item[-1]))

# s = 'hi how are you how is your health'
# l = s.split()
# d = {i: len(i) for i in l}
# p = sorted(d.items(), key=lambda item: item[-1])
# print(p[-1])

# s = 'python is a programming language and programming is fun'
# l = s.split()
# d = {i: len(i) for i in l if l.count(i) == 1}
# print(d)
# r = sorted(d.items(), key=lambda item: item[-1])
# print(r[-1])

# s = 'hi how are you hi how is your health'
# l = s.split()
# # d = [i for i in l if i[0] in 'hH']
# # print(d)
# import re
# for i in l:
#     r = re.findall(r'^h', s)
#     if r:
#         print(r)

# s = 'hi how are you how is your health'
# import re
# d = re.findall(r'[aeiou]+', s)
# print(d)

# w = 'sony 12 india pvt 34 ltd 567 bnglore'
# sum = 0
# for i in w:
#     sum += 1
# import re
# r = re.findall(r'\d', w)
# print(sum)

# s = 'hi$ there how are you :) how is your health'
# import re
# r = re.findall(r'[a-z]+', s)
# print(r)
# print(len(r))

# e = 'hello 123 world 567 welcome to 9724 python'
# import re
# r = re.findall(r'[0-9]', e)
# print(r)
# p = [int(i) for i in r]
# print(p)
# o = [i for i in p if i % 2 == 0]
# print(o)
# print(sum(o))

# 21 Write a class named Simple and it should have iteration capability.
#
# class Simple:
#     def __init__(self, items):
#         self._items = items
#
#     def __iter__(self):
#         return iter(self._items)
#
# >>> s = Simple([1, 2, 3, 4, 5])
# >>>
# >>> for item in s:
# 	print(item)

# e = "Hi How are you"
# l = e.split()
# for i in l:
#     print(i[::-1], end=' ')
# c = e.split()
# print(e[::-1])

# 25 Write a lambda function to add two numbers (a, b)
# p = lambda a, b: (a+b)
# print(p(3, 5))

# for row in range(1, 5):
#     for col in range(1, row+1):
#         print('*', end=" ")
#     print()
#
# for row in range(4, 0, -1):
#     print(f'{"* "*row:<8}')

# for row in range(1, 5):
#     print(f'{"* "*row:^8}')

# for row in range(ord("a"), ord("d")+1):
#     for col in range(ord("a"), row+1):
#         print(chr(col), end=' ')
#     print()


# l = [1, 2,3, 4,1,2, 3, 4, 3, 4, 4]
# d = []
# for i in l:
#     if not i in d:
#         d.append(i)
# print(d)

# l = [2, 5,7,9]
# for i in range(1, 10):
#     if not i in l:
#         print(i)

# rs = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# for i in rs:
#     if i.startswith('8'):
#         print(i)

# import re
# res = re.findall(r'^8', rs)
# print(res)

# v = 'hello 123 world 456 welcome to python498675634'
# import re
# res = re.findall(r'\d', v)
# print(res)
# p = [i for i in res if int(i)%2==0]
# o = [i for i in res if int(i)%2!=0]
# print(o)
# print(p)

# v = 'hello 123 world 567 welcome to 9724 python'
# import re
# res = re.findall(r'[0-9]', v)
# print(res)
# p = [i for i in res if int(i)%2==0]
# print(p)

# v = 'hello world hi hello universe how are you happy birthday'
# l = v.split()
# for i in l:
#     if i.startswith('h'):
#         print(i)

# print('banglore /n' * 10)

# s = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(s):
#     dd[item] += [index]
# print(dd)
#
# d = {}
# for index, item in enumerate(s):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

# s = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for i in s:
#     if i.endswith('5'):
#         print(i)
# a = [1, 2, 3]
# b= [4, 5, 6]
# c = a+b
# print(a+b)

# e = "Hi How are you"
# l = e.split()
# c = [i[::-1] for i in l]
# # print(c)
# print(' '.join(c))
# print(c[::-1])

# v =  ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# for i in v:
#     if i.startswith('8'):
#         print(i)

# i = [1, 2, 3, 4, 1, 2, 4, 3, 5]
# for item in set(i):
#     print(item)

# s = 'hi python welcomes you'
# d = {}
# words=s.split()
# d={word:len(word) for word in words}
# print(d)
# print(sorted(d.items()[-1]))
# print(sorted(len(d)))
# shortest,*rest,longest=['hi', 'python', 'welcomes', 'you']
# print(longest)
# for item in words:
#     d[item] = len(item)
# print(d)
# r = sorted(d.items(), key=lambda item: item[-1])
# print(r[-1])

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# for item in b:
#     if item not in a:
#         print(item)

# def fun(*args):
#     if len(args) > 5:
#         return f'lenth is > 5'
#     return f'lenth is < 5'
#
# print(fun(1, 2, 3, 4, 5, 6, 7))

# a = [1, 2, 3, 4, 5]
# print(a[::-1])

# def func(string, n):
#     if n:
#         return string[0::2]
#     return string[1::2]
#
#
# print(func('TRAXCN', 1))

# s = "Sony12India567Pvt2ltd"
# sum = 0
# for item in s:
#     if '0' <= item <= '9':
#         sum += 1
# print(sum)

# s = 'hello world'
# r = ''
# for i in s:
#     r = i+r
# print(r)
# for item in reversed(s):
#     print(item)

# for i in s[::-1]:
#     print(i, end=' ')

s = 'hello world'
# count = 0
# for i in s:
#     count += 1
# print(count)

# print(len(s))

# v = "Hello world"
# print(v.replace('world', 'universe'))


# s = "Hello World"
# print(s.lower())
# print(s.upper())
# print(s.islower())
# print(s.isupper())

# s = 'hello world'
# print(s.count('l'))

# s = 'python'
# print(list(s))
# print(''.join(s))

# s = "Hello welcome to Python"
# # l = s.split()
# for i in s:
#     # print(i, end=',')
#     print(i, end=',')

# s = 'hello world'
# for i in s[::2]:
#     print(i)

# s = 'hello'
# for item in s:
#     print(chr(ord(item))

# v = 'PyThoN'
# r = ''
# for i in v:
#     if 'a' <= i <= 'z':
#         r+=chr(ord(i)-32)
#     elif 'A' <= i <= 'Z':
#         r+=chr(ord(i)+32)
#     else:
#         r+=i
# print(r)

# v = 'pYThon'
# p=''
# for i in v:
#     if 'a'<=i<='z':
#         p += i.upper()
#     elif 'A' <=i<='Z':
#         p += i.lower()
#     else:
#         p+=i
# print(p)

# a = 2
# m = 8
# a, m = m, a
# print(m)
# print(a)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# from itertools import islice
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             line = islice(file, 2, 5)
#             print(list(line))

# path = R'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# from collections import deque
# with open(path) as file:
#     for line in file:
#         l = deque(file, 3)
#         print(list(l))

# s = 'madam'
# if s == s[::-1]:
#     print(f'True')
# else:
#     print(f'False')

# s = 'praveen'
# o = 'e'
# for index,item in enumerate(s):
#     if o == item:
#         print(f'{item} is present in {index}')
#         break

# e = "hello world welcome to python programming hi there"
# l = e.split()
# d = {}
# for i in l:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]
# print(d)
#
# from collections import defaultdict
# dd =defaultdict(list)
# for item in l:
#     dd[item[0]] += [item]
# print(dd)

# s = 'hello world welcome to home'
# c = ''.join(['_' if s.count(i) >1 else i for i in s])
# print(c)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
# @outer
# def sub(string):
#     return string
# print(sub('python'))

# class login:
#     count = 0
#     def __init__(self, a):
#         self.a = a
#         login.count += 1
#
# p1 = login(2)
# print(p1.count)
# p2 = login(1)
# print(p2.count)

# def func(args):
#     for i in args:
#         if isinstance(i, str):
#             print(i)
#         else:
#             print(str(i)[::-1])
#
# func(['python', 'pen', 10, 9000, 2.94, 'madam'])
#
# e = "Hi How are you"
# l = e.split()
# c= [i[::-1] for i in l]
# print(c)
# # print(' '.join(c))
# print(e[::-1])

# res = lambda a, b: a+b
# print(res(3, 5))


# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# for i in set(items):
#     print(i)

# s = "Hello world. Welcome to Python"
# l = s.split()
# d = {i: len(i) for i in l}
# print(d)
# r= sorted(d.items(), key=lambda i: i[-1])
# print(r[-1])
# r= sorted(d.items(), key=lambda i: i[-1])
# print(r[0])

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# d1 = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d1)



# t = ('1', '2', '3', '4')
# print(''.join(t))

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# for i in b:
#     if i not in a:
#         print(i)

# def outer(*args):
#     if len(args) > 5:
#         return f'length is > 5'
#     return f'length is < 5'
#
# print(outer(12, 2, 3, 23))

# a = [1, 2, 3, 4, 5]
# print(a[::-1])

# def func(string, n):
#     if n:
#         return string[0::2]
#     return string[1::2]
#
# print(func('TRACXN', 0))
# print(func('TRACXN', 1))

# s = "Sony12India567Pvt2ltd"
# import re
# r = re.findall(r'\d', s)
# print(r)
# s = 0
# for i in r:
#     s += int(i)
# print(s)

# s = "Sony12India567Pvt2ltd"
# import re
# r = re.findall(r'\d+', s)
# print(r)
# s = 0
# for i in r:
#     s += int(i)
# print(s)

# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isnumeric():
#         print(i)

# s = 'helloworld'
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)
# r = sorted(d.items(), key= lambda item: item[-1])
# print(r)
# print(r[-1])

# s = 'helloworld'
# d = {}
# for i in s:
#     if s.count(i) == 1:
#         d[i] = s.count(i)
# print(d)

# s = 'hello world welcome to python'
# c = [i for i in s[::2]]
# print(c)

# a = [1, 2, 3, 4, 5]
# p = lambda i: i * i
# c = [p(i) for i in a]
# print(c)

# def func(a, b):
#     if a == b:
#         return False
#     sa = sorted(a.upper())
#     sb = sorted(b.upper())
#     if sa == sb:
#         return True
#     else:
#         return False
#
# print(func('ate', 'eat'))
# print(func('pen', 'men'))

# s = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# c = [i for i in s if len(i) % 2 == 0]
# print(c)

# s = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {i: len(i) for i in s if len(i) % 2 == 0}
# print(d)

# a = [1, 2, 3, 4, 5]
# p = lambda i: i * i
# r = map(p, a)
# print(list(r))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             count += 1
#     print(count)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(line_no, line)

# l = [[1,2,3],[4,5,6],[7,8,9]]
# ex = 0
# for i in l:
#     ine = 0
#     for item in i:
#         ine+=1
#         ex+=1
#     print(ine)
# print(ex)

# words = ["hi", "hello", "python"]
# r = [i[::-1] for i in words[::-1]]
# print(r)

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# print((*t1,*t2))

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = 'net'
# print(d)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# import re
# with open(path) as file:
#     r = re.findall(r'\s', file)
# print(r)

# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# from collections import defaultdict
# d = defaultdict(list)
# for word in words:
# 	s = ''.join(sorted(word))
# 	d[s].append(word)
#
# print(d)

# c = [i for i in range(1,51) if i % 2 ==0]
# print(c)

# s= 'helloworld'
# d = {}
# for i in s:
#     if s.count(i) > 1:
#         d[i] = s.count(i)
# print(d)

# s = 'hello world welcome to python'
# c = [i for i in s[::2]]
# print(c)

# a = [1, 2, 3, 4, 5]
# p = lambda i: i * i
# c= [p(i) for i in a]
# print(c)

# def func(a, b):
#     if a.upper() == b.upper():
#         return False
#     s_a = sorted(a.upper())
#     s_b = sorted(b.upper())
#     if s_a == s_b:
#         return True
#     else:
#         return False
#
# print(func('ate', 'eat'))
# print(func('pen', 'men'))

# s = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# c = [i for i in s if len(i) % 2 == 0]
# print(c)

# s = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {i: len(i) for i in s if len(i) % 2 == 0}
# print(d)

# a = [1,2,3,4,5]
# c = lambda i: i * i
# r = map(c, a)
# print(list(r))

# s = "This is a Programming language and Programming is fun"
# l = s.split()
# d = {i: len(i) for i in l if l.count(i) == 1}
# print(d)
# res = sorted(d.items(), key= lambda item: item[-1])
# print(res)
# print(res[-1])

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# res = set(names)
# print(res)

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d = {}
# for item in names:
#     d[item] = names.count(item)
# print(d)

# def func(n):
#     for i in range(2, n):
#         if n % i ==0:
#             print(f'not prime')
#         else:
#             print(f'is prime')
#
# func(3)

# t = tuple(range(10))
# print(t)

# rs = [10, 20, 30, 40, 50]
# print(max(rs))

# def func(n):
#     p = str(n)
#     return p[-1]
#
# print(func(3572))


# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']
# d = {i: words.count(i) for i in words if words.count(i) > 1}
# print(d)

# def tail(sequence, n):
#     return sequence[:n]
#
# print(tail('hello', 2))

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d = {i: names.count(i) for i in names if names.count(i) > 1}
# print(d)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         p = line.split()
#         for item in p:
#             count += 1
# print(count)      #34

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         p = line.split()
#         for item in p:
#             if item[0] in 'aeiou':
#                 count += 1
#
# print(count)  #7

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for i in items:
#     if isinstance(i, (int, float)):
#         print(i)

# for row in range(1, 5):
#     for col in range(1, row+1):
#         print(col, end='')
#     print()

# l = ['python', 'java', 'c++', 'mongoDB', 'perl', 'madam']
# l.sort(key=len)
# print(l)
# p = sorted(l, key=lambda i: len(i))
# print(p)

# s = 'python is easy language'
# l = s.split()
# print(l)
# s, *rest, l = sorted(l, key=len)
# print(s, l)

# s = 'python is easy language'
# le = s.split()
# s, *rest, l = sorted(le, key=len)
# print((l, len(s)), (s, len(s)))

# l = ['python', 'java', 'c++', 'mongodb', 'perl', 'madam']
# res = sorted(l, key=lambda item: item[-1])
# print(res)

# l = ['python', 'java', 'c++', 'mongoDB', 'perl', 'madam']
# res = sorted(l)
# print(res)

# d = {'gmail': 5, 'python': 8, 'apple': 5, 'walmart': 9}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res)

# d = {'gmail': 5, 'python': 8, 'apple': 5, 'walmart': 9}
# r = sorted(d.items(), key=lambda item: item[-1])
# print(r)

# T = [('delhi', 32), ('mumbai', 27), ('kolkata', 30), ('chennai', 35)]
# r = sorted(T, key=lambda i: i[-1])
# print(r)

# s= 'hi how are you how about health'
# l = s.split()
# d = {i: s.count(i) for i in l if s.count(i) > 1}
# print(d)
# r = sorted(d.items(), key=lambda i: i[-1])
# print(r[-1])

# s= 'hi how are you how about health'
# l = s.split()
# d = {i: len(i) for i in l}
# print(d)
# r = sorted(d.items(), key=lambda i: i[-1])
# print(r)
# print(r[-1])

# s= 'python is a programming language and programming is fun'
# l = s.split()
# d = {i: len(i) for i in l if l.count(i) == 1}
# print(d)
# r = sorted(d.items(), key=lambda i: i[-1])
# print(r)
# print(r[-1])

# l = ['hai', 'guys', 'welcome', 'to', 'my', 'channel']
# count = 0
# for i in l:
#     count += 1
# print(count)


# def func(s):
#     l = s.split()
#     for i in l:
#         if i[0] in 'aeiou':
#             return i
# print(func('please like, share and comment'))

# def func(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print(f'not prime')
#     else:
#         print(f'prime')
#
# func(7)

# def run(args):
#     r = ''
#     for i in args:
#         r = i+r
#     return r
#
# print(run('hello'))

# def fun(a=0, b=1):
#     i = 0
#     while i < 10:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         i += 1
#     return a
# print(fun())
#
# n = 10
# a = 0
# b = 1
# i = 0
# while i <= 10:
#     c = a + b
#     a = b
#     b = c
#     i += 1
#
# print(a)

# s  = 'it is a very good book and reading book is a good habit'
# l = s.split()
# d = {i: l.count(i) for i in l}
# print(d)
# r = sorted(d.items(), key= lambda i: i[-1])
# print(r)

# s = 'AppLE'
# for i in s:
#     if 'a'<=i<='z':
#         print(chr(ord(i)-32), end=' ')
#     elif 'A'<=i<='Z':
#         print(chr(ord(i)+32), end=' ')
#     else:
#         print('special symole')

# l = ['hello', 'ball', 'zebra', 'yak', 'apple', 'madam']
# l.sort()
# print(l)

# s = 'this world is not enough'
# l = s.split()
# r = sorted(l, key=lambda i: len(i))
# print(r)

# l = ['hello', 'ball', 'zebra', 'yak', 'apple']
# r = sorted(l, key=lambda i: i[-1])
# print(r)

# p = 12345
# o = str(p)
# print(o)
# for i in o[::-1]:
#     print(i, end=' ')

# p = 1234
# o = str(p)
# sum = 0
# for i in o:
#     sum += int(i)
# print(sum)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('hi hello how are you')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def func():
#     print('hi python')
# func()

# from time import sleep
# def outer(func):
#     def wrapper(*args, **kwargs):
#         sleep(2)
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def fun():
#     print('hello world')
# fun()

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
# @outer
# def fun(string):
#     return string
#
# print(fun('python'))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @outer
# def greet(string):
#     return string
#
# print(greet('hi python'))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, *kwargs)
#         return res.upper()
#     return wrapper
#
# @outer
# def fun():
#     return ('hello world')
#
# print(fun())
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res.lower()
#     return wrapper
#
# @outer
# def greet():
#     return ('HELLO WORLD')
#
# print(greet())

# class Employee:
#     def __init__(self, name, lname, pay):
#         self.name = name
#         self.lname = lname
#         self.pay = pay
#
# p = Employee('praveen', 'iyli', 1000)
# print(p.name)
# print(p.pay)


# s = 'hello world hello python'
# import re
# res = re.findall(r'.', s)
# print(res)
#
# res = re.findall(r'[h]+', s)
# print(res)

# import re
# res= re.findall(r'[89][0-9]{9}', 8197431230)
# print(res)

# s = 'hello world welcome to python'
# import re
# res = re.findall(r'[aeiou]', s)
# print(res)

# import re
# u = re.findall(r'[0-9]', 'the cost of book is $100')
# print(u)

# import re
# res = re.findall(r'[0-9]+', 'the cost of book is $1000')
# print(res)

# import re
# res = re.findall(r'[^0-9]', 'the cost of this book is 9250 and the cost is 250rs discount')
# print(res)

# import re
# res = re.findall(r'[\W]', 'the cost of this book is $900, & &250')
# print(res)

# s = 'hello hi world hello how are you'
# import re
# res = re.findall(r'\bh\w+\b', s)
# print(res)

# w = 'sony 12 india pvt 34 ltd567 banglore'
# import re
# r = re.findall(r'[0-9]', w)
# print(r)
# sum = 0
# for i in r:
#     sum += int(i)
# print(sum)

# w = 'sony 12 india pvt 34 ltd567 banglore'
# import re
# r = re.findall(r'[0-9]+', w)
# print(r)
# sum = 0
# for i in r:
#     sum += int(i)
# print(sum)

# s = 'hello hi world hello how are you'
# import re
# r = re.findall(r'\s', s)
# print(r)
# s = 0
# for i in r:
#     s += 1
# print(s)

# s = 'hello@ hi! world he$llo how a&&re you'
# import re
# r = re.findall(r'[a-zA-Z0-9]', s)
# print(r)
#
# w = 'the cost of this book is $900, & &250'
# import re
# r = re.findall(r'[0-9]', w)
# print(r)

# s = 'hello@ hi! world he$llo how a&&re you'
# import re
# r = re.findall(r'\w', s)
# print(r)
# s = 0
# for i in r:
#     s += 1
# print(s)

# s = 'HeLlo wORld WeLcOMe To PytHON'
# import re
# r = len(re.findall(r'[A-Z]', s))
# p = len(re.findall(r'[a-z]', s))
# print(r)
# print(p)

# s = 'hello hi american engineer and indian writer officers united states'
# import re
# r = re.findall(r'\b[aeiou]\w+', s)
# print(r)

# s = 'hello hi american engineer and indian writer officers united states'
# l = s.split()
# r = [i for i in l if i[0] in 'aeiou']
# print(r)

# s = 'hello@ hi! world he$llo how a&&re you'
# c = [i for i in s if not 'a' <= i <= 'z']
# print(c)
# p = 0
# for i in c:
#     p += 1
# print(p)

# w = 'the cost of this book is $900, & &250'
# import re
# c = re.findall(r'[0-9]+', w)
# print(c)
# p = 0
# for i in c:
#     p += int(i)
# print(p)

# def func():
#     l = []
#     for i in range(1, 50):
#         if i % 2 == 0:
#           l.append(i)
#     return l
#
#
# print(func())

# res = (i for i in range(1, 50) if i%2==0)
# print(list(res))

# n = ['onion', 'eat', 'java', 'pen', 'ice', 'python', 'madam']
# def func(args):
#     for item in args:
#         if item[0] in 'aeiou':
#             yield item
#
# p = func(['onion', 'eat', 'java', 'pen', 'ice', 'python', 'madam'])
# print(list(p))
#
# res = (i for i in n if i[0] in 'aeiou')
# print(list(res))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(line, len(line))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line in file:
#         print(line)
#
# with open(path) as file:
#     c = 0
#     for line in file:
#         c += 1
#     print(c)
#
# with open(path) as file:
#     for line, line_no in enumerate(file):
#         print(line_no, line)


# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         pen = line.split()
#         count += len(pen)
#     print(count)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line in list(file)[::-1]:
#         print(line)

path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

# import re
# p = 0
# with open(path) as file:
#     for line in file:
#         r = re.findall(r'\s', line)
#         if r:
#             p += len(r)
# print(p)
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         for item in line.split(' '):
#             count+=1
#     print(count)

# with open(path) as file:
#     count = 0
#     for line in file:
#         for i in line.split():
#             if i[0] in 'aeiou':
#                 count += 1
#     print(count)
#

# with open(path) as file:
#     d = {}
#     for line in file:
#         for i in line.split():
#             if i not in d:
#                 d[i] = i.count(i)
#             else:
#                 d[i] += i.count(i)
#     print(d)

# import os
# path = r"C:\Users\admin\Desktop\selenium_v9.pdf"
# print(os.path.exists(path))
#
# path = r"selenium_v9"
# print(os.path.exists(path))
#
# from time import sleep
# def outer(func):
#     def wrapper(*args, **kwargs):
#         sleep(3)
#         return func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     return a+b
#
# print(add(2,3))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         sleep(3)
#         print(f'executing wrapper')
#         return func(*args, **kwargs)
#     return wrapper
#
# @outer
# def greet(string):
#     return string
#
# print(greet('python'))

# s = 'hello'
# r = ''
# for i in s:
#     r = i + r
# print(r)

# s = 'hello'
# count = 0
# for i in s:
#     count += 1
# print(count)

# p = 'hello universe'
# print(p.replace('universe', 'worls'))

# s = 'hello world'
# print(list(s))
# print(''.join(list(s)))

# s = 'hello world welcome to python'
# l = s.split()
# print(l, end=',')

# s = 'hello world'
# for i in s[::2]:
#     print(i)

# s = 'hello'
# for i in s:
#     print(ord(i))

# s = 'HeLLo'
# r = ''
# for i in s:
#     if 'a'<=i<='z':
#         r+=chr(ord(i)-32)
#     elif 'A'<=i<='Z':
#         r+=chr(ord(i)+32)
#     else:
#         r+=i
# print(r)

# a = 10
# b = 20
# a, b = b, a
# print(b)
# print(a)

# a = [1, 2, 3]
# b= [3,4,  5]
# print(*a, *b)

# p = {'a': 1, 'b': 2}
# l = {'c': 3, 'd': 4}
# c = {**p, **l}
# print(c)

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# from itertools import islice
# with open(path) as file:
    # for line in file:
    # line = islice(file, 1, 5)
    # print(list(line))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             lines = islice(file, 2, 5)
#             print(list(lines))

# path = r'C:\Users\admin\PycharmProjects\practice\files_directory\txt_log_files\sample.txt'
# from collections import deque
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             lines = deque(file, 4)
#             print(list(lines))

# s = 'hello'
# p = 'mom'
# if p == p[::-1]:
#     print('True')
# else:
#     print('False')

# s = 'hello world'
# e = 'l'
# for index, item in enumerate(s):
#     if item == e:
#         print(f'{item} is at {index}')
#         break

# s = 'hello world welcome to python program hi there'
# l = s.split()
# from collections import defaultdict
# dd = defaultdict(list)
# for i in l:
#     dd[i[0]] += [i]
# print(dd)

# s = 'hellohai'
# c = ''.join(['-' if s.count(i) > 1 else i for i in s])
# print(c)

# def outer(fun):
#     def wrapper(*args, **kwargs):
#         res = fun(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @outer
# def sub(a, b):
#     return a+b
#
# print(sub(2, -4))

# def func(*args):
#     for i in args:
#         if isinstance(i, int):
#             print (str(i)[::-1])
#         else:
#             print (i)
#
# func('python', 10, 2022, 'java', 'mom', 2.5)

s = 'Hi How Are You'
a = s[::-1]
print(a)
# print(a[::-1])