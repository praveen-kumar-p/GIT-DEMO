# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f'execting parent google {self.value}')
#         print('spam')
#
#     def apple(self):
#         print('executing parent apple')
#         self.google()
#
# #child class having a separate method
# class child1(parent):
#     def demo(self):
#         print('executing demo')
#
# #child overriding parent class method
# class child2(parent):
#     def hello_world(self):
#         print('hello world')
#
#     def google(self):          #google is delete in parent and adding google in child2 we can use present google
#         print('executing child2 google {self.value}')
#
# #child adding extra functionality and re-using the original functionality of the parent class
# class child3(parent):
#     def google(self):
#         print('executing child3 google!!!', self.value)
#         super().google()
#
# #child class having an extra attribute
# class child4(parent):
#     def __init__(self, value, name):
#         self.name = name
#         super().__init__(value)    #calling parent class constructor
#
#
# # c = child1(10)
# # c.apple()
# # c.google()
# # c.demo()
# # c.google()
# c = child4(10, 'praveen')
# print(c.__dict__)
# print(c.name)
# print(c.value)
#
# #
# class A:
#     def demo(self):
#         print('class A demo')
# class B(A):
#     def demo(self):
#         print('class B demo')
# class C(B):
#     def demo(self):
#         print('class c demo')
#
# c = C()
# print(c.demo())

# class bankaccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposite(self, amount):
#         if amount < 0:
#             raise ValueError('amount should be greater than 0')
#         self.balance += amount
#
#     def withdrawn(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return amount
#         else:
#             raise ValueError('insuffient fund')
#
#     def roi(self):
#         interest = self.balance * self.__class__.interest_rate
#         self.balance

# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f'executing parent google {self.value}')
#
#     def apple(self):
#         print(f'executing parent apple {self.value}')
#         self.google()
#
# class child(parent):
#     def demo(self):
#         print('executing demo')
#
# c = child(100)
# print(c.demo())
# print(c.google())

# class one:
#     def __init__(self, b):
#         self.b = b
#
#     def func(self):
#         print('func is here')
# class two(one):
#     def __init__(self, b, d):
#         super().__init__(b)
#         self.d = d
#     def func2(self):
#         print('func2 is here', self.d)
#
# hi = two(10, 20)
# print(hi.func2())
# print(hi.d)
# print(hi.b)

# class school:
#     clgid = '001'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class child(school):
#     def __init__(self, name, age, rollno):
#         super().__init__(name, age)
#         self.rollno = rollno
#
# st = child('go', 42, 526)
# emp = child('praveen', 25, 60)
# print(st.name)
# print(st.age)
# print(st.rollno)
# print(st.__dict__)
# print(st.clgid)
# print(st.__dict__)
# print(emp.__dict__)

# class bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         print(f'{name} as this much {balance}')
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'{amount}')
#
# per = bank('po', 1000)
# per2 = bank('ro', 1002)
# print(per.__dict__)
# print(per.name)
# print(per.balance)

# class parent:
#     def __init__(self, value, quantity, name):
#         self.value = value
#         self.quantity = quantity
#         self.name = name
#
#     def apple(self):
#         print('parent apple', self.value)
#
# e =parent(200, 2, 'opiu')
# print(e.__dict__)

# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
# p1 = point(1, 2)
# p2 = point(3, 4)
# print(p1.a)
# print(p2.a)
# print(p1.__dict__)
# p1.c = 1
# print(p1.__dict__)

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#
#
#     def circumference(self):
#         return 2 * 3.142 * self.radius
#
# c = circle(5)
# print(c.radius)
# print(c.circumference())

# class Person:
    # def __init__(self, fname , lname , age):
    #     self.fname = fname
    #     self.lname = lname
    #     self.age = age
    # @property
    # def fname(self):
    #     print('getting')
    #     return self._fname
    # @fname.setter
#
# c = Person('run', 'on', 12)
# print(c.__dict__)
#
# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def apple(self):
#         print('parent apple', self.value)
#
#     def google(self):
#         print('parent google', self.value)

# class child1(parent):
#     def apple(self):
#         print('child1.apple')

# c = parent(20)
# print(c.__dict__)
# c.apple()
# c.google()
# c = child1(20)
# c.apple()

# class child2(parent):
#     def __init__(self, value, extra):
#         def _

# single level inheritance
# class parent:
#     def spam(self):
#         print('class parent spam')

# class child(parent):
#     def demo(self):
#         print('class child demo')

# c = child()
# print(c.spam())
# print(c.demo())

# multi level inheritance
# class parent:
#     def spam(self):
#         print('class')
# class child(parent):
#     def demo(self):
#         print('class child demo')
# class gchild(child):
#     def new(self):
#         print('class gchild new')
#
# c = gchild()
# print(c.spam())
# print(c.demo())
# print(c.new())

# class dad:
#     def spam(self):
#         print('class dad spam')
# class mom:
#     def demo(self):
#         print('mom method')
# class child(dad, mom):
#     def new(self):
#         print('child method')
#
# c = child()
# print(c.spam())
# print(c.demo())
# print(c.new())

# class parent:
#     def spam(self):
#         print('parent method')
# class child(parent):
#     def demo(self):
#         print('child method')
#         super().spam()
# class mom(child, parent):
#     pass
#
# c = mom()
# print(c.demo())

# class parent:
#     def __init__(self, value):
#         self.value = value
#     def google(self):
#         print(f'executing {self.value}')
#     def apple(self):
#         print(f'executing apple')
#         self.google()
# class child(parent):
#     def demo(self):
#         print('method demo')
# c = child(100)
# print(c.google())
# print(c.apple())