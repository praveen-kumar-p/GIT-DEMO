'''l = [1, 2, 3, 4, 5]
r = []
for item in l:
    r.append(item**2)
print(r)
l = [1, 2, 3, 4, 5]
r = []
for index, item in enumerate(l):
    r.append(item)
print(r)

l = [1, 2, 3, 4, 5]
r = []
r = [(index, item) for index, item in enumerate(l)]
print(r)

l = [1, 2, 3, 4, 5]
r = [item for item in l if item % 2 == 0]
print(r)

l = [1, 2, 3, 4, 5]
r = []
p = []
for item in l:
    if item % 2 == 0:
        r.append(item)
    else:
        p.append(item)
print(p)

l = ['amazon', 'flipkart', 'gamil', 'yahoo']
r = [item for item in l if item[0] in 'aeiou']
print(r)
l = {'java', 'python', 10, True, 1.4, 'c++', 'ruby'}
r = set()
for item in enumerate(l):
    r.add((item))
print(r)

s = ['amazon', 'flipkart', 'gamil', 'yahoo']
set = {(item, len(item)) for item in s}
print(set)

l = [1, 2, 3, 4, 5]
r = [item ** 2 for item in l]
print(r)

l = [1, 2, 3, 4, 5]
r = [(item) for item in enumerate(l)]
print(r)

l = [1, 2, 3, 4, 5]
r = [item for item in l if item % 2 != 0]
print(r)

l = [1, 2, 3, 4, 5]
r = []
p = []
for item in l:
    if item % 2 == 0:
        r.append(item)
    else:
        p.append(item)
print(r, p)

l = ['python', 'node js', 'selenium', 'java']
r = []
for item in l:
    if len(item) % 2 == 0:
        r.append(item)
    else:
        r.append(item[::-1])
print(r)

r = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(r)

l = ['java', 'python', 10, True, 1.4, 'c++', 'ruby']
r = []
for item in l:
    if not isinstance(item, str):
        r.append(str(item)[::-1])
    else:
        r.append(item)
print(r)

r = [str(item)[::-1] if not isinstance (item, str) else item for item in l]
print(r)

y = 'hello world'
count = 0
for item in y:
    count += 1
print(count)

n = 'hello0123 hai 4% 978'
for item in n:
    if '0' <= item <= '9':
        print(item)

n = 1234
d = str(n)
if int(d[0]) % 2 == 0:
    print('is even')
else:
    print('is odd')
i = [10, 20, 30, 40]
if len(i) % 2 == 0:
    print('is even')
else:
    print('is odd')

n = 10
while n > 0:
    print(n)
    n -= 1

l = [1, 2, 3, 4, 5]
r = [item ** 2 for item in l]
print(r)

l = [1, 2, 3, 4, 5]
r = [(item) for item in enumerate(l)]
print(r)

l = [1, 2, 3, 4, 5]
r = [(item) for item in l if item % 2 == 0]
print(r)

l = ['java', 'python', 'insta', 'node js']
r = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(r)

l = ['java', 'python', 'insta', 'node js', 10, 2+9j, 2.6]
r = []
for item in l:
    if not isinstance(item, str):
        r.append(str(item)[::-1])
    else:
        r.append(item)
print(r)

r = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
print(r)


l = ['amazon', 'flipkart', 'oppo', 'java']
r = []
for item in l:
    if item[0] in 'aeiou':
        print(r)

s = {1, 2, 3, 4, 5}
r = {item ** 2 for item in s}
print(r)

s = {'java', 'python', 10, True, 2.4, 'c++', 'ruby'}
r = {item for item in enumerate(s)}
print(r)

file = 'she sells sea shells on the sea shore'
for item in file:
    print((item, len(item)))

s = [python]
r = [item for item in s]
print(r)

s = {'python'}
r = {item for item in s}
print(r)

s = ['python']
r = [item for item in enumerate(s)]
print(r)

s = ['hai']
r = [item[::-1] for item in s]
print(r)

s = ['hai']
r = [index for index, item in enumerate(s)]
print(r)

l = ['python', 'java', 10, 3.4, 'selenium']
r = [item for item in l]
print(r)

l = ['python', 'java', 10, 3.4, 'selenium']
r = [index for index, item in enumerate(l)]
print(r)

l = ['python', 'java', 'selenium']
r = [item[::-1] for item in l]
print(r)

l = ['python', 'java', 'selenium']
r = [item for item in l[::2]]
print(r)

l = ['python', 'java', 'selenium']
r = [len(item) for item in l if len(item) % 2 == 0]
print(r)

l = ['python', 'java', 'selenium', 'insta', 'kit']
r = [item for item in l if len(item) % 2 == 0]
print(r)


l = ['python', 'java', 'selenium', 'insta', 'kit']
r = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(r)

l = ['python', 'java', 'selenium', 'insta', 'kit']
r = [item for item in l if item[0] in 'aeiou']
print(r)

l = ['python', 'java', 'selenium', 'insta', 'kit']
for index, item in enumerate(l):
    print(index, item)

l = ['python', 'java', 'selenium', 'insta', 'kit']
for item in range(len(l)-1, -1, -1):
    print(l[item])

l = ['python', 'java', 'selenium', 'insta', 'kit']
for item in range(0, 5, 2):
    print(l[item])

l = ['python', 'java', 'selenium']
for item in l:
    print(item, len(item))

l = ['python', 'java', 'insta', 'selenium']
for item in l:
    if len(item) % 2 == 0:
        print(item)

l = ['python', 'java', 'insta', 'selenium']
for item in l:
    if len(item) % 2 == 0:
        print(item)
    else:
        print(item[::-1])
l = ['python', 'java', 'insta', 'selenium', 7.8, 4+5j]
for item in l:
    if not isinstance(item, str):
        print(str(item)[::-1])
    else:
        print(item)

l = ['amazon', 'flipkart', 'oppo', 'java', 'gmail']
for item in l:
    if item[0] in 'aeiou':
         print(item)

z = [10, 40, 20, 80, 20, 40, 30]
a = 40
for index, item in enumerate(z):
    if item == a:
        print(index)
        break

n = 5
for item in range(2, n):
    if n % item == 0:
        print('not a prime number')
        break
else:
    print('is prime')

a = [10, 40, 20, 80, 20, 40, 30]
n = 20
for item in a:
    if n == item:
        continue
print(a)

l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
for item in l:
    if item == item[::-1]:
        print(item)

l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
for item in l:
    print(item)

l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
for index, item in enumerate(l):
    if item == item[::-1]:
        print(index)

s = 'hello'
dict_ = {item: index for index, item in enumerate(s)}
print(dict_)

s = 'hi welcome to python'
m = s.split()
d = {item: s.count(item) for item in m}
print(d)

s = 'hi welcome to python'
d = {}
m = s.split()
for item in m:
    d[item] = s.count(item)
print(d)

d = {item: s.count(item) for item in m if len(item) % 2 == 0}
print(d)

s = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d = {value: key for key, value in s.items()}
print(d)

s = ['hi', 'welcome', 'to', 'python', 10, 2+8j]
d = {index: item[::-1] if not isinstance (item, str) else item for index, item in enumerate(s)}
print(d)

s = 'hello world wel come to python'
m = s.split()
d = {item: m.count(item) for item in m if len(item) % 2 == 0}
print(d)

s = 'hello world wel come to python'
m = s.split()
d = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(m)}
print(d)

s = 'hello world wel come to python onion'
m = s.split()
d = {item: len(item) for item in m if item[0] in 'aeiou'}
print(d)

s = ['hello', 'world', 10, True, 3.4]
d = {index: item if isinstance(item, str) else item[::-1] for index, item in enumerate(s)}
print(d)

l = ['python', 'dad', 'hai', 'malayalam', 'madam']
r = set()
for item in l:
    if item == item[::-1]:
        r.add(item)
print(r)

l = ['python', 'dad', 'hai', 'malayalam', 'madam']
for item in l:
    if item == item[::-1]:
        print(f'{item} is palindrome')

numbers = [10, 40, 20, 80, 20, 40, 30]
n = 20
for num in numbers:
    if n == num:
        continue
print(numbers)

l = [1, 2, 3, 15, 25, 17, 19]
for n in l:
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n)
l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
for item in l:
    a = item.split('.')
    print(a[0])

a = [10, 20, 40, 30, 80, 20, 10, 40]
n = 20
for item in a:
    if n == item:
        continue
    print(item)

l = ['python', 'node js', 'selenium', 'insta']
for item in l:
    if item[0] in 'aeiou':
        print(item)

l = {'python', 'dad', 'hai', 'malayalam', 'madam', 'mom'}
k = 'hai'
for item in l:
    if item == k:
        l.discard(k)
        break
print(l)

d = {"a": 1, "b": 2}
print(d)

d = dict(a=1, b=2)
print(d)

l = [('hai', 3), ('hello', 2)]
print(dict(l))

d = {'a': 1, 'b': 2, 'c': 3}
for item in d.keys():
    print(item)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value, sep='-')

for index, (key, value) in enumerate(d.items()):
    print(index, (key, value))


s = 'hello world'
d = {}
for item in s:
    d[item] = s.count(item)
print(d)

from collections import defaultdict
dd = defaultdict(int)
for item in s:
    dd[item] = dd[item] + 1
print(dd)

s = 'hello world welcome to python programming hi there'
d = {}
l = s.split()11
for item in s:
    d[item[0]] = item
print(d)

s = 'python is easy language welcome to python'
from collections import defaultdict
l = s.split()
dd = defaultdict(int)
for item in l:
    dd[item] = dd[item] + 1
print(dd)

s = 'python is easy language welcome to python'
from collections import defaultdict
l = s.split()
dd = defaultdict(list)
for item in l:
    dd[item[0]] += [item]
print(dd)

s = 'python'
d = {}
for item in s:
    if 'a' <= item <= 'z':
        print(chr(ord(item)-32))


def f(a, b, /):
    c = a + b
    return c
print(f(1, 2))

def f(*, a, b):
    c = a + b
    return c
print(f(a=1, b=2))

def f(a, /, *, b):
    c = a + b
    return c
print(
    f(1, b=2))

def prime():
    for n in range(2, 50):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n)

print(prime())

n = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
m = []
for item in n:
    if len(item) % 2 == 0:
        m.append(item)
print(m)

n = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
m = []
for item in n:
    if len(item) % 2 == 0:
        print(item)
    else:
        print(item[::-1])

l = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++', 'python', 'ruby']
r = set()
for item in l:
    if item[0] in 'pP':
        r.add(item)
print(r)

i = ['apple', 1.2, 'google', '12.6', 26, '100']
l = []
for item in i:
    if isinstance(item, (int, float, complex)):
        print(item)

for n in range(1, 100):
    if n > 1:
        for item in range(2, n):
            if n % item == 0:
                break
        else:
            print(n, end=' ')

w = ['hi', 'hello', 'python']
r = []
for item in w[::-1]:
    r.append(item[::-1])
print(r)

l = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++', 'python', 'ruby']
r = []
for item in l:
    if item not in r:
        r.append(item)
print(r)

s = 'hello 123 world567 welcome to 9724 python'
sum = []
for item in s:
    if 'a' <= item <= 'z' and not int(item) % 2 == 0:
        sum += int(item)
print(sum)
def r(name, age):
    print(f'{name} is {age} year old')
r(25, 'ram')

def r(name, age):
    print(f'{name} is {age} years old')
r(name = 'ram', age = 25)
r(age = 25, name = 'ram')

def r(name, age):
    print(f'{name} is {age} years old')
r('ram', 25)
r(name = 'ram', age = '25')
r('ram', age = 25)

def f(a, b, c, d, /):
    print(a, b, c, d)
f(1, 2, 3, 4)

def f(a, b, *, c, d):
    print(a, b, c, d)
f(1, 2, c=3, d=4)

def u(a, /, *, b):
    c = a + b
    return c
print(u(1, b=2))

def u(a, b, /):
    c = a + b
    return c
print(u(10, 20))

def u(a, *, b):
    c = a + b
    return c
print(u(1, b=2))

a = 'banglore'
print(a * 10)

a_ = 0
b_ = 0
s = 'hai 1234 python23'
for item in s:
    if 'A' <= item <= 'Z' or 'a' <= item <= 'z':
        a_ += 1
    elif '0' <= item <= '9':
        b_ += 1
print(a_, b_)

s = 'HeLlo WorLD'
r = ''
for item in s:
    if item.lower() not in 'aeiou':
        r += item
print(r)

s = 'hello world'
y = 'l'
for index, item in enumerate(s):
    if y == item:
        print(f'{y} is present at index{index}')
        break

for item in range(len(s)):
    if y == s[index]:
print(f'{y} is present at {index}')

s = 'hello'
for item in s:
    if item.lower() in 'aeiou':
        print(chr, ord(item))

s = 'hello world'
l = s.split()
for item in l:
    print(item, len(item))

s = 'hai everyone, welcome to python class'
l = s.split()
for item in l:
    if item[0] in 'aeiou':
        print(l)

s = 'hello world'
for item in s:
    if item not in 'aeiou':
        print(item, end=' ')
n = 4
if n % 2 == 0:
    print('n is present')
else:
    print('not present')

v = 'l'
if 'a' <= v <= 'z':
    print('v is present')
else:
    print('not present')

l = ['python', 'java', 'insta', 'selenium']
h = 'c++'
if h in l:
    print('h is present')
else:
    print('h is not present')

p = '*'
if 'a' <= p <= 'z':
    print('is lower')
elif 'A' <= p <= 'z':
    print('is upper')
else:
    print('special character')

o = 0
if o:
    print('true')
else:
    print('false')

s = 'apple'
if s[0] in 'aeiou':
    print('is present')
else:
    print('not present')

c = 'python'
if c == c[::-1]:
    print('is palindrome')
else:
    print('not palindrome')

a = 0
b = 1
i = 0
i = 10
while i <= 10:
    i = 10
    print(a)
    c = a + b
    a = b
    b = c
    i += 1

s = 'hello'
d = {}
for i, j in enumerate(s):
    d[j] = i
print(d)

d = {j: i for i, j in enumerate(s)}
print(d)

d = 'hi welcome to python'
l = d.split()
p = {item: len(item) for item in l}
print(p)

def spam(*args):
    print(args)


spam(1, 2, 3.3)

def f(a,b):
    return (count(f))
f(1, 2, 3)

def function(*args):
    for item in args:
        if isinstance(item, str):
            print(item[::-1])

function('python', 'java', 10, 2.2, 'selenium')

def fun(n):
    for item in range(2, n):
        if n % item == 0:
            return "no is not prime"
    return 'it is prime'

print(fun(6))

def f(*args):


    for item in f:
        return [-1]


print(f(100))

def isperfectsquare(n):


    for i in range(n):
        if i * i == n:
            return True
    return False

print(isperfectsquare(5))


def function(*args):
    for item in args:
        if isinstance(item, (str, list, tuple, set, dict)):
            return item
        return len(item)
print(function('apple', 10, [1, 2, 3], {"table"}))

def is_fibo(num):
    a = 0
    b = 1
    while a <= num:
        if a == num:
            return f'{num} is a fibonacci number'
        c = a + b
        a = b
        b = c
    return f'{num} is not a fibonacci number'
print(is_fibo(4))

def func(string, n):
    if n == 0:
        return string [1::2]
    elif n == 1:
        return string [::2]
    else:
        'n value is invalid'
print(func('TRACXN', 1))

def isperfectsquare(n):
    for item in range(n):
        if item * item == n:
            return True
    return False
print(isperfectsquare(4))

l = ['amazon', 'flipkart', 'walmart', 'gmail', 'onion']
m = [item for item in l if item[0] in 'aeiouAEIOU']
print(m)

l = ['java', 'python', 10, True, 1.3, 9+3j, 'ruby']
m = [item if isinstance (item, str) else str(item[::-1]) for item in l]
print(m)

l = [1, 2, 3, 4, 5]
p = [item * item for item in l]
print(p)

l = [1, 2, 3, 4, 5]
p = [(item) for item in enumerate(l)]
print(p)

l = [1, 2, 3, 4, 5]
p = [item for item in l if item % 2 == 0]
print(p)

l = ['python', 'onion', 'pretty', 'men', 'run']
h = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(h)

l = ['java', 'python', 10, True, 1.3, 9+3j, 'ruby']
h =[str(item)[::-1]if not isinstance(item,str) else item for item in l]
print(h)

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
p = {item * item for item in s}
print(p)

l = ['python', 'onion', 'pretty', 'men', 'run']
p = {(item) for item in enumerate(l)}
print(p)

l = ['python', 'onion', 'pretty', 'men', 'run']
p = {(item, len(item)) for item in l}
print(p)

s = 'hello'
d = {item: index for index, item in enumerate(s)}
print(d)

s = 'hi welcome to python'
l = s.split()
p = {item: len(item) for item in l}
print(p)

s = 'hello world'
p = {item: s.count(item) for item in s}
print(p)

s = 'python is a language, python programming is easy'
l = s.split()
p = {item: s.count(item) for item in l}
print(p)

s = 'python is a language, python programming is easy'
l = s.split()
p = {item: s.count(item) for item in l if len(item) % 2 == 0}
print(p)

s = 'python is a language, python programming is easy'
l = s.split()
p = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(l)}
print(p)

s = 'python is a language, python programming is easy'
l = s.split()
p = {item: len(item) for item in l if item[0] in 'aeiouAEIOU'}
print(p)

l = ['java', 'python', 10, True, 1.3, 9+3j, 'ruby']
p = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(l)}
print(p)
l = ['java', 'python', 10, True, 1.3, 9+3j, 'ruby']
p = {index: str(item)[::-1] if not isinstance(item, str) else item for index, item in enumerate(l)}
print(p)

l = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
p = {value: key for key, value in l.items()}
print(p)

n = ['apple', 'google', 'apple', 'yahoo', 'google']
p = {item: len(item) for item in n if }
print(p)

s = ['apple', 'java', 'onion', 'uniform']
p = {item for item in s if item[0] in 'aeiouAeiou'}
print(p)

l = 'praveen'
p = {index: item for index, item in enumerate(l) if item in 'aeiouAEIOU'}
print(p)


def function():
    l = []
    for item in range(1, 50):
        if item % 2 == 0:
          l.append(item)
    return l


print(function())

a = 0
b = 1
i = 0
while i < 50:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1

def f(*args):
    sum = 0
    for item in args:
        if isinstance(item, (int, float)):
            sum += 1
    return sum


print(f(7, 7 , 8 , 5))

def f(*l, **kwargs):
    count = 0
    for item in l, kwargs:
        count += 1
    return l, kwargs
print(f('python', 10, 5+7j, 'run'))


def f(*l):
    for item in l:
        if len(l) > 5:
            return 'l > 5'
    return 'l < 5'
print(f(1, 2, 3, 4))
def f(n):
    for item in range(2, n):
        if n % item == 0:
            return 'not prime'
    return 'prime'


print(f(7))

def f(*l):
    for i in l:
        return l[-1]


print(f(1, 2, 3, 4, 4, 5))
def f(n):
    for item in range(n):
        if item * item == n:
            return 'is perfect square'
    return 'not perfect square'


print(f(4))

def f(*l):
    for item in l:
        return l[-1]


print(f('squence', 'n'))


def f(string, n):


        if n == 0:
            return string[1::2]
        elif n == 1:
            return string[::2]
        else:
             return 'special symbol


print(f('TRACXN', 0))
def f(c):
    a = 0
    b = 1
    while a <= c:
        if a == c:
            return 'fibonacci no'
        c = a + b
        a = b
        b = c
    return 'f{c} i not fibonacci no'
print(f(26))

def f(*l):
    for item in l:
        return item[::-1]


print(f('hai', 'python', 'men'))

def f(*s):
    count = 0
    for item in s:
        count += 1
    return count


print(f('hello world', 10, True))

def f(start, end):
    if start < end:
        return
    print(start)
    f(start-1, end)


print(f(10, 1))
n = 123
d = str(n)
sum = 0
for i in d:
    sum += int(i)
print(sum)


def s(num, sum=0):
    if num > 0:
        last = num % 10
        sum += last
        num = num // 10
        return s(num, sum)
    else:
        return sum


print(s())

def f(n, c=0):
    if n > 0:
        c += 1
        n = n // 10
        return f(n, c)
    return c
print(f(4))

def r(string, i = 0, res = ''):
    if i < len(string):
        res = string[i] + res
        return r(string, i + 1, res)
    return res


print(r('hello'))

def f(i):
    for item in i:
        return i
print(f('python'))

def f(*s):
    for i, j in enumerate(s):
        print(i, j, end=' ')


print(f('p', 'y', 't', 'h', 'o', 'n'))
def f(s):
    for item in s[::-1]:
        print (item, end=' ')


print(f('hai'))

def f(s):
    count = 0
    for item in s:
        count += 1
    print (count, end=' ')

print(f('hello world'))
def f(s):
    for item in s:
        return s[::2]

print(f('praveen'))

def f(*l):
    for item in l:
        isinstance(item, int)
    print (item)


print(f('hello 123 hai 4 % 973'))

def f(*l):
    for index, item in enumerate(l):
        print(index, item)


print(f('python', 'java', 10, 'selenium'))
def f(*l):
    for item in l:
        print(l[::-1])
        # print(item[-1])


f('praveen', 'selenium', 'java', 'men', 'madam')


def f(*l):
    for item in l:
        return l[::2]


print(f('python', 'java', 'men'))


def f(*l):
    for item in l:
        isinstance(l, int)
    print (l)

print(f('python', 'java', 10, 2.3, 'men'))


def f(*l):
    for item in l:
        return len(l)


print(f('python', 'node js', 'selenium', 'java'))


def f(*l):
    for item in l:
        print (len(item) % 2 == 0)


print(f('python', 'node js', 'selenium', 'java'))

def f(*l):
    for item in l:
        return item[0] in 'aeiouAEIOU'
    return l


print(f('python', 'node js', 'selenium', 'insta'))
def f(a, /, *, b):
    c = a + b
    return c


print(f(1, b=2))


def f(start, end):
    l = []
    for item in range(start, end):
        if item % 2 == 0:
            l.append(item)
    return l

print(f)


l = [1, 2, 3, 4]
m = lambda l: f'{item} is even' item % 2 == 0 else f'{item} is odd'
a = map(m, l)
print(list(a))

def f(*l):
    t = []
    for item in l:
        t += [item[::-1]]
    return t


print(f('python', 'java', 'selenium'))


def f(*l):
    res = []
    for item in l:
        if isinstance(item, int):
            res.append(item)
    return res

print(f('python', 'java', 10, 3+8j, 298))

l = ['python', 'java']
res = []
for i in l:
    for j in i:
        res.append(ord(j))
print(res)


l = ['python', 'java', 'men']
n = 3
for item in l:
    if len(item) - 1 =
        # print(item)
name = ['apple', 'leap', 'dense', 'apple', 'leap']
from collections import defaultdict
d = defaultdict(list)
for index,item in enumerate(name):
    d[item] = d[item] + [index]
print(d)


l = 'hello'
m = lambda item: (item, ord(item))
p = map(m, l)
print(list(p))

def func(*string):
    l = []
    for item in string:
         if len(item) % 2 == 0:
             l.append(item)
    return l



print(func('gmail', 'flipkart', 'google', 'yahoo', 'rediff'))'''



s = 'python is easy language'
# l = s.split()
# for word in l:
#     print([word, len(word)])

l = ['well', 'men']

# def func(word):
#     for word in l:
#         return word
#
# res = list(map(list, l))
# print(res)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# def add_(a, b):
#     return a + b
#
# res = map(add_, a, b)
# print(list(res))



# a = [1, 2, 3, 4]
# def square(a):
#     return a ** 2
#
# res = map(square, a)
# print(list(res))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def square(item):
#     if item % 2 == 0:
#         return item ** 2
#
#
# num = list(filter(square, a))
# res = map(square, num)
# print(list(res))

# m = lambda item: item % 2 == 0
# print(m(9))

# m = lambda a, b:  a * b
# print(m(1, 2))

# m = lambda item: item[::-1]
# print(m('python'))

# m = lambda item: item == item[::-1]
# print(m('pen'))

# m = lambda item: f'{item} is even' if item % 2 == 0 else f'{item} is odd'
# print(m(111))

# p = ['python', 'onion', 'eat', 'universe']
# m = lambda item: item[0] in 'aeiouAEIOU'
# k = map(m, p)
# print(list(k))

# m = lambda a: len(a) % 2 == 0
# print(m('python'))
#
# m = lambda item: item
# print(m('python'))
# b = 'python'
# m = lambda (index, item): (index, item) in enumerate(b)
# print(m)

# list_ = ['hai', 'mom', 'dad', 'hello']
# palindrome = lambda item: item == item[::-1]
# res = map(palindrome, list_)
# print(list(res))

# l = [1, 2, 3, 4]
# even = lambda item: f'{item} is even' if item % 2 == 0 else f'{item} is odd'
# res = map(even, l)
# print(list(res))

# l = ['python', 'onion', 'oppo', 'c++', 'eat']
# string = lambda item: f'{item}' if item[0] in 'aeiouAEIOU' else f'{item} is not vowel'
# res = map(string, l)
# print(list(res))

# l = ['python', 'onion', 'oppo', 'c++', 'eat']
# upper_ = lambda item: f'{item.upper()}'
# res = map(upper_, l)
# print(list(res))

# l = [-1, -2, -3]
# conv = lambda item: l[::2]
# res = map(conv, l)
# print(list(res))

# l = [1, 2, 3]
# power = lambda i, j: j ** i
# res = map(power, enumerate(l))
# print(list(res))

# l = 'PYHTON IS LANGUAGE'
# s = l.split()
# low = lambda item: f'{item.lower()}'
# res = map(low, s)
# print(list(res))

# s = 'python is easy language'
# l = s.split()
# lth = lambda item: (item, len(item))
# res = map(lth, l)
# print(list(res))
#
# l = 'hello'
# m = lambda item: (item, ord(item))
# res = map(m, l)
# print(list(res))

# l = [10, 20, 30, 40]
# def func(item):
#     return item[1] ** item[0]
# res = map(func, enumerate(l))
# print(list(res))

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# def func(a, b):
#     return a + b
#
# res = map(func, a, b)
# print(list(res))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def even(num):
#     if num % 2 == 0:
#         return num
#
#
# evens = filter(even, l)
# print(list(evens))

# l = ['python', 'men', 'women', 'onion', 'universe']
# def fun(item):
#     if item[0] in 'aeiou':
#         return item
#
# res = filter(fun, l)
# print(list(res))

# l = ['gmail', 'flipkart', 'google', 'yahoo', 'rediff']
#
# def fun(item):
#     if len(item) % 2 != 0:
#         return item
#
# res = filter(fun, l)
# print(list(res))
#
# odd = lambda item: len(item) % 2 != 0
# res = filter(fun, l)
# print(list(res))

# s = 'hello hai how are you'
# l = s.split()
# def fun(item):
#     if item[0] in 'aeiou':
#         return item
#
# res = filter(fun, l)
# print(list(res))

# a = [1, 2, 3, 4]
# def func(item):
#     return item ** 2
#
# res = map(func, a)
# print(list(res))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def func(item):
#     if item % 2 == 0:
#         return item
#
# res = filter(func, enumerate(l))
# print(list(res))

s = ['python', 10, 3.2, 'selenium', 'java']
# for item in s:
#     isinstance(item, int)
#
# res = filter(isinstance(), s)
# print(list(item))

# m = lambda item: isinstance (item, int)
# res = filter(m, s)
# print(list(res))

# s = ['python', 'selenium', 'java']
# m = lambda item: (item, len(item))
# res = map(m, s)
# print(list(res))

# l = ['python', 'node js', 'men', 'java']
# m = lambda item: len(item) % 2 != 0
# res = filter(m, l)
# print(list(res))

# l = ['python', 'node js', 'men', 'java']
# m = lambda item: f'{item} is even' len(item) % 2 == 0 else f'{item} is odd'
# res = filter(m, l)
# print(list(res))

# l = ['python', 'node js', 'men', 'java']
# m = lambda item: item[::-1]
# res = map(m, l)
# print(list(res))

# l = ['python', 'node js', 'men', 'java']
# m = lambda item: item[::-1]
# res = map(m, l)
# print(list(res))

# l = ['onion', 'ice', 'python', 'men', 'java']
# m = lambda item: item[0] in 'aeiou'
# res = filter(m, l)
# print(list(res))

# l = ['youtube.txt', 'amazon.in', 'flipkart.in', 'apple.txt']
# m = lambda item: item.split('.')
# res = map(m, l)
# print(list(res))

# l = ['youtube.txt', 'amazon.in', 'flipkart.in', 'apple.txt']
# def func(item):
#     s = l.split('.')
#     if s % 2 != 0:
#         return item
# # m = lambda item: item.split('.')
# res = map(func, l)
# print(list(res))

list_ = ('hello')
# for index, item in enumerate(list_):
#     print(index, item)

# m = lambda item: item
# res = map(m, enumerate(list_))
# print(list(res))

# list_ = ('hello')
# m = lambda item: list_.count(item)
# res = map(m, list_)
# print(list(res))

# sen = ['python is easy language python']
# m = lambda item: len(item.split())
# res = map(m, sen)
# print(list(res))

# def func(items):
#     for key, item in items:
#         d[key] = item
#
# res = map(func, items)
# print(func('a': 1, 'b': 2))




































































































































































