# class employee:
#     def __init__(self, name, lname, age):
#         self.fname = name
#         self.lastname = lname
#         self.age = age
#
#     def email(self):
#         return f'{e2.fname}.{e2.lastname}@company.com'
#
# e1 = employee('praveen', 'kumar', 25)
# e2 = employee('steve', 'jobs', 30)
# print(e1.email())
# print(e2.email())
# print(e1.__dict__)
# print(e2.__dict__)
# print(e1.fname)
# print(e2.lastname)

    # def email():
    #     return f'{e1.fname}.{e1.lastname}@company.com'
# e1 = employee('praveen', 'kumar', 25)
# e2 = employee('steve', 'jobs', 30)
# print(e2.__init__)

# class employee:
#     def __init__(self, name, lname, salary):
#         self.fname = name
#         self.name = lname
#         self.pay = salary
#
# e1 = employee('steve', 'jobs', 1000)
# e2 = employee('sri', 'ram', 2000)
#
# print(e1.__dict__)
# print(e2.__dict__)
# print(e2.name)
# print(e1.name)
#
#     def payhike(self, percentagehike):
#         hike = self.pay * percentagehike
#         self.salary += hike
#         return self.salary
#
# e1 = payhike('steve', 'jobs', 1000)
# print(e1.payhike(0.1))

# class calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#
#     def mul(self, a, b):
#         return self.a * self.b
#
#     def sub(self, a, b):
#         return self.a - self.b
# c1 = calculator(a=2, b=5)
# c2 = calculator(10, 30)
# print(c1.__dict__)
# print(c2.__dict__)

# class player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
# p1 = player(1,2)
# p2 = player(3, 4)
# print(p1.__dict__)
# print(p2.x)

# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#
# p1 = point(1, 2)
# p2 = point(10,  20)
# print(p1.__dict__)
# print(p2.__dict__)

# class shopping:
#     def __init__(self):
#         self.cart = []
#
#     def add(self, name, quantity, price):
#         self.cart.append({'name': name, 'quantity': 1, 'price': price})
#
# c1 =

# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.salary = pay
#
# emp1 = Employee('steve', 'jobs', 10000)
# emp2 = Employee('bill', 'gates', 20000)
#
# print(Employee)
#
# print(dir(emp1))
# print(emp1.__dict__)
# print(emp2.__dict__)

# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.salary = pay
#     def email(self):
#         return f'{self.fname}.{self.lname}@company.com'
#
# e1 = Employee('steve', 'jobs', 1000)
# e2 = Employee('sri', 'ram', 2000)
#
# print(e1.__dict__)
# print(e2.__dict__)
# print(e1.__dict__['fname'])
# print(e2.__dict__['lname'])
# print(e2.__dict__['fname'])
# print(e2.__dict__['lname'])

# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.salary = pay
#     def email(self):
#         return f'{self.fname}.{self.lname}@company.com'
#     def payhike(self, percentagehike):
#         hikeamount = self.salary * percentagehike
#         self.salary = self.salary + hikeamount
#         return self.salary

# e1 = Employee('steve', 'jobs', 1000)
# e2 = Employee('sri', 'ram', 2000)
# print(e1.email())
# print(e2.email())
# print(e1.__dict__)
# print(e2.__dict__)
# e1.payhike(.10)
# print(e1.salary)
# e2.payhike(.10)
# print(e2.salary)
# print(e1.__dict__)
# print(e2.__dict__)

# class calculator:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# c1 = calculator(1, 2)
# c2 = calculator(10, 20)
#
# print(c1.add())
# print(c1.sub())
# print(c1.mul())
# print(c2.add())

# class point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def move(self, dx, dy):
#         self.a = dx
#         self.b = dy
#
# p1 = point(1, 2)
# p2 = point(10, 20)
# print(p1.__dict__)
# print(p2.__dict__)
# class player:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.health = 100
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#
#     def attack(self, point):
#         self.health -= point
#
# p1 = player(1, 2)
# p2 = player(3, 4)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(player.__dict__)

# class bankaccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#         self.transaction = []
#         self.transaction.append(f'**{name} initial amount deposite {balance}**')
#
#     def deposite(self, amount):
#         self.balance += amount
#         self.transaction.append(f'amount deposite {amount}')
#
#     def withdrawn(self, amount):
#         if amount > self.balance:
#             raise ValueError
#         self.balance -= amount
#         self.transaction.append(f'amount withdrawn {amount}')
#         return f'transaction completed'
#
#     def transfer(self, toaccount, amount):
#         if amount > self.balance:
#             raise ValueError
#         toaccount.deposite(amount)
#         self.balance -= amount
#
# c1 = bankaccount('praveen', 1000)
# c2 = bankaccount('ram')
# print(c1.transaction)
# c1.deposite(1000)
# print(c1.__dict__)
# c1.withdrawn(500)
# print(c1.__dict__)
# c1.transfer(c2, 700)
# print(c1.__dict__)
# print(c2.__dict__)


# class Employee:
#     def __init__(self, name, lname, pay):
#         self.f_name = name
#         self.last_name = lname
#         self.salary = pay
#
#     def pay_hike(self, percentage_hike):
#         self.hike_amount = self.salary * percentage_hike
#         self.salary += self.hike_amount
#         print(f'Total salay of {self.f_name} is {self.salary}')
        # return f'Total salay of {self.f_name} is {self.salary}'
#
#
# e = Employee('sriram', 'jai', 300000)
# print(e.__dict__)
# a = e.pay_hike(0.20)

# print(a)

# class calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(self.a + self.b)
#
#     def sub(self):
#         print (abs(self.a - self.b))
#
#     def mul(self):
#         print(self.a * self.b)
#
# c = calculator(2, 4)
# c2 = calculator(10, 4)
# c.add()
# c2.add()
# c.sub()
# c2.sub()
# c.mul()
# c2.mul()

# class Travel:
#     def __init__(self, name, ticket_no):
#         self.name = name
#         self.ticket_no = ticket_no
#
#     def book(self, seat_no):
#         self.seat_no = seat_no
#         print(f'traveller {self.name} as ticket number {self.ticket_no} and his seat no is {self.seat_no}')
#
#
# p = Travel('sriram', 5)
# o = Travel('ram', 'bus003')
# o.book('11')
# p.book('01')


# class Employee:
#     def __init__(self, f_name, l_name, pay):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.pay = pay
#
#     def personal_details(self, dob, _id, **kwargs):
#         self.dob = dob
#         self._id = _id
#         self.kwargs = kwargs
#         return f'the age of {self.f_name} {self.l_name} is {self.dob} and his Employee id is {self._id}'
        # return self.dob, self._id , self.kwargs
#
#
# p = Employee('sri', 'ram', 1000)
# print(p.personal_details(17, 1234, address='kdbf', phno=984929347))

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#         return self.a, self.b
#
# p = Point(2, 5)
# print(p.move(8, 4))

# class point:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# p = point()
# print(p.__dict__)

# class greeting:
#     def __call__(self, name):
#         return f'hello {name}'
#
# c = greeting()
# print(c('sriram'))

# class even:
#     def __call__(self, num):
#         if num % 2 == 0:
#             return f'the {num} is even'
#         return f'the {num} is odd'
#
#
# e = even()
# print(e(2))
# print(e(3))

# class reverse:
#     def __call__(self, *args):         # (['madam', 'java', 'pen'],)
#         for i in args:
#             if i == i[::-1]:
#                 print(f'{i} is palindrome')
#             else:
#                 print(f'{i} is not palindrome')
#
#
# r = reverse()
# r('madam', 'java', 'pen')

# class oven:
#     def __call__(self, *args):
#         l = []
#         for i in args:
#             if i[0] in 'aeiou':
#                 l.append(i)
#         return l
#
#
# p = oven()
# print(p('onion', 'eat', 'men', 'ice'))

# class emploee with emp details and create a num of emplo and

# class Employee:
#     count = 0
#
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         Employee.count += 1
#
#     def family(self, dob=17, place='hospet'):
#         self.dob = dob
#         self.place = place
#         return f'{self.dob} {self.place}'
#
#
# p = Employee('sriram', 1234)
# o = Employee('ram', 234)
# print(Employee.count)


