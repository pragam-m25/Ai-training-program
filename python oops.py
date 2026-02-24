# Question1 
class Student:
    def __init__(self, n, m):
        self.name = n
        self.marks = m

s1 = Student("Rahul", 85)
s2 = Student("Aman", 92)

print(s1.name, s1.marks)
print(s2.name, s2.marks)

# Question 2
class Laptop:
    def __init__(self, b, p):
        self.brand = b
        self.price = p

l1 = Laptop("HP", 55000)
print(l1.brand, l1.price)


# Question 3
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 5)
print(r1.area())



# Question 4
class Employee:
    company_name = "TCS"
    
    def __init__(self, n):
        self.employee_name = n

e1 = Employee("Rohit")
print(Employee.company_name, e1.employee_name)



# Question 5
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 7))


# # Question 6
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c1 = Cat()
c1.sound()


# Question 7
class Person:
    def __init__(self, n):
        self.name = n

class Employee(Person):
    def __init__(self, n, s):
        super().__init__(n)
        self.salary = s

class Manager(Employee):
    def __init__(self, n, s, d):
        super().__init__(n, s)
        self.department = d

m1 = Manager("Karan", 50000, "IT")
print(m1.name, m1.salary, m1.department)



# Question 8
class Father:
    def showFather(self):
        print("I am father")

class Mother:
    def showMother(self):
        print("I am mother")

class Child(Father, Mother):
    pass

c = Child()
c.showFather()
c.showMother()


# Question 9
class BankAccount:
    def __init__(self, b):
        self.balance = b
    
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Left:", self.balance)

class SavingsAccount(BankAccount):
    def withdraw(self, amt):
        if self.balance - amt < 1000:
            print("Minimum balance required")
        else:
            self.balance -= amt
            print("Left:", self.balance)

s = SavingsAccount(5000)
s.withdraw(4500)


# Question 10
class Account:
    def __init__(self, b):
        self.__balance = b
    
    def deposit(self, amt):
        self.__balance += amt
    
    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            print("Left:", self.__balance)

a = Account(3000)
a.deposit(1000)
a.withdraw(2000)


# Question 11
class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r

class Square:
    def __init__(self, s):
        self.s = s
    
    def area(self):
        return self.s * self.s

shapes = [Circle(3), Square(4)]

for i in shapes:
    print(i.area())



# Question 12
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Car(Vehicle):
    def start(self):
        print("Car started")

b = Bike()
c = Car()
b.start()
c.start()


# Question 13
a = int(input())
b = int(input())

try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Question 14
try:
    n = int(input())
    print(n)
except ValueError:
    print("Invalid input")


# Question 15
try:
    x = int(input())
    y = int(input())
    print(x / y)
except ValueError:
    print("Wrong input")
except ZeroDivisionError:
    print("Zero not allowed")


# Question 16
try:
    f = open("test.txt", "w")
    f.write("hello")
finally:
    f.close()



# Question 17
class InsufficientBalanceError(Exception):
    pass

class Bank:
    def __init__(self, b):
        self.bal = b
    
    def withdraw(self, amt):
        if amt > self.bal:
            raise InsufficientBalanceError("Not enough balance")
        self.bal -= amt

b1 = Bank(2000)
try:
    b1.withdraw(3000)
except InsufficientBalanceError as e:
    print(e)


# Question 18
age = int(input())

if age < 18:
    raise Exception("Not eligible to vote")
else:
    print("You can vote")


# Question 19
lst = [10, 20, 30, 40]

try:
    i = int(input())
    print(lst[i])
except IndexError:
    print("Index out of range")


# Question 20
try:
    a = int(input())
    b = int(input())
    res = a / b
except ZeroDivisionError:
    print("Error")
else:
    print(res)


