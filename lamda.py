'''m = lambda item: item % 2 == 0
print(m(4))

m = lambda a, b: a * b
print(m(1, 2))

m = lambda s: s[-1]
print(m('python'))

m = lambda s: s if s == s[::-1] else 'not a palindrome'
print(m('mom'))

l = [1, 2, 3, 4, 5]
m = lambda n: f'{n} is even' if n % 2 == 0 else f'{n} is odd'
a = map(m, l)
print(list(a))

l = ['python', 'onion', 'oppo', 'eat', 'ice']
m = lambda n: n[0] in 'aeiouAEIOU'
a = map(m, l)
print(list(a))

l = ['python', 'onion', 'oppo', 'eat', 'ice']
m = lambda item: f'{item.upper()}'
p = map(m, l)
print(list(p))

l = [-1, -2, -3]
m = lambda item: f'{abs(item)}'
p = map(m, l)
print(list(p))

l = [1, 2, 3]
m = lambda i, j: i, j in enumerate(l)
p = map(m, l)
print(list(p))

l = 'PYTHON IS EASY LANGUAGE'
o = l.split()
m = lambda item: f'{item.lower()}'
p = map(m, o)
print(list(p))

def f(start, end):
    if start < end:
        return
    print(start)
    f(start - 1, end)
f(10, 1)'''

# def f(start, end = 10):
#     i = 0
#     if i < end:
#         c = start + end
#         start = end
#         end = c
#         i -= 1
#     return start
#
#
# print(f(0, 10))


# class employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#
# e1 = employee('praveen', 'kumar', 1000)
# e2= employee('ram', 'kumar', 5000)
# print(e1.__dict__)
#
# print(e1.__dict__['first_name'])
# print(e2.__dict__)
#
# print(e2.__dict__['salary'])
#
# def email(self):
#     return f'{self.first_name}.{self.last_name}@company.com'
#
# print(email(employee))




















