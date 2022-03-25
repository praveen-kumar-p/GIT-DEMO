from functools import singledispatch

# @singledispatch
# def add(a, b):
#     print('base function add')
#
# @add.register(int)
# def _(a, b):
#     print('caling int')
#     return a + b
# @add.register(float)
# def _(a, b):
#     print('calling float')
#     return a + b
# @add.register(list)
# def _(a, b):
#     print('calling list')
#     return sum(a) + b
#
# a = add([1, 2], 2)
# print(a)