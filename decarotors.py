# def outer(func):
#     def wrapper(*args, **kwargs):
#         func(*args,**kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(1, 2)

# def log(func):
#     def wrapper(*args, **kwargs):
#         print('hi python')
#         func(*args, **kwargs)
#     return wrapper
#
# @log
# def display():
#     print('in display')
#
# display()

import time
# def outer(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(5)
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print (a + b)
#
# add(1, 2)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
# @outer
# def ex(string):
#     return string
#
# print(ex('python'))

# def in_(func):
#     def c(*args, **kwargs):
#         print('*some*')
#         func(*args, **kwargs)
#         print('*some*')
#     return c
# def inn_(func):
#     @in_
#     def c(*args, **kwargs):
#         print('*more*')
#         func(*args, **kwargs)
#         print('*more*')
#     return c
# @in_
# @inn_
# def d(a):
#     print(a)
#
# d('hello')

# def outer(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def ex(a, b):
#     print(abs(a * b))
#
# ex(2,-5)

# from time import time
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         func(*args, **kwargs)
#         end = time()
#         print (f'execution time of function {func.__name__} is {end - start} seconds')
#     return wrapper
#
# @outer
# def greet(name):
#     print (f'hi {name}')
#
#
# greet('praveen')
import time
from collections import defaultdict
# _count = defaultdict(int)
# def func_count(func):
#     def wrapper(*args, **kwargs):
#         _count[func.__name__] += 1
#         print(_count)
#         return func(*args, **kwargs)
#     return wrapper
# @func_count
# def ex(name):
#     return f'hey {name} welcome to python world'
#
# print(ex('praveen'))
#
# @func_count
# def mul(a, b):
#     time.sleep(3)
#     return a * b
#
# print(mul(3,5))

# def maxcall(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         if func.count > 5:
#             raise 'valueError'
#         return func(*args, **kwargs)
#     return wrapper
#
# @maxcall
# def greet(name):
#     return 'hi {name}'
#
# print(greet('praveen'))

import time
# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             func(*args, **kwargs)
#             time.sleep(2)
#     return wrapper
#
# @repeat
# def add(a, b):
#     print (a + b)
#
# add(2, 3)
#
# @repeat
# def greet():
#     print('hello world')
#
# greet()

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res.upper()
#     return wrapper
# @outer
# def ex(args):
#     return args
#
# print(ex('hello'))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res.lower()
#     return wrapper
#
# @outer
# def ex(a):
#     return a
#
# print(ex('HELLO'))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
# @outer
# def x(a, b, c):
#     return a + b + c
#
# print(x(3, -6, 4))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return (res % 2 == 0)
#     return wrapper
#
# @outer
# def x(*args):
#     return args
#
# print(x(1, 2, 3, 4, 5, 6))

# class Log:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs)
#
# @Log
# def add(a, b):
#     return a + b
#
# print(add(1, 2))