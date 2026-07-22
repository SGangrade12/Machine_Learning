# # String Handling
#
#
# s="Hello World"
#
# print(s)
#
# print(type(s))
#
# print(len(s))
#
# print(s.lower())
# print(s.upper())
# print(s.replace("o","x"))
# print(s.index("o"))
# print(s.count("o"))
# print(s.find("o"))
# print(s.find("x"))
# print(s.index("o"))
# # print(s.index("x"))
# x=s.split()
# print(s.split())
# print(s.split("o"))
# sep=" "
# sep.join(x)
# print(sep.join(x))
# print(s[3:8:4])
# print(s[-1:-12:-1])
# print(s[::-1])
# print(reversed(s[::-1]))




# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# Lambda function
# Anonymous function
# Single line function
# Faster than def function
# No use of print or return statement

# l1=[1,2,3,4,5]
# l2=[10,20,30,40,50]

# a=lambda x,y: x if x>y else y

# print(a(l1,l2))


# Lambda with Map:



# OOPs

# class Phone:
#     def makecall(self):
#         print("Making call")

#     def sendmsg(self):
#         print("Sending message")

#     def set_color(self,color):
#         self.color=color
    
#     def set_cost(self,cost):
#         self.cost=cost
    
#     def show_details(self):
#         return f"Color: {self.color}, Cost: {self.cost}"


# mobile=Phone()

# mobile.makecall()
# mobile.sendmsg()
# mobile.set_color("blue")
# mobile.set_cost(10000)
# print(mobile.show_details())


# Adding Multiple Parameters in OOPs using constructor(__init__)

# class Vehicle:
#     def __init__(self,brand,mileage,price):
#         self.brand=brand
#         self.mileage=mileage
#         self.price=price
    
#     def show_details(self):
#         return f"Brand: {self.brand}, Mileage: {self.mileage}, Price: {self.price}"

# vehicle1=Vehicle("Toyota",15,20000)

# print(vehicle1.show_details())



# Inheritance In OOPs

# 1. Single Inheritance

# class Vehicle:
#     def __init__(self,brand,mileage,price):
#         self.brand=brand
#         self.mileage=mileage
#         self.price=price
    
#     def show_details(self):
#         return f"Brand: {self.brand}, Mileage: {self.mileage}, Price: {self.price}"
    

# class car(Vehicle):
#     def show_details(self):
#         return f"Brand: {self.brand}, Mileage: {self.mileage}, Price: {self.price}"
    
#     print("I am a car ")


# c1=car("Toyota",15,20000)

# print(c1.show_details())


# Polymorphism

# class shape:
#     def area(self):
#         pass

# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth


# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius 
#     def area(self):
#         return 3.14*self.radius*self.radius
    

# class triangle(shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return (self.base*self.height)/2
    

# s=[rectangle(2,3),circle(5),triangle(1,2)]

# for i in s:
#     print(i.area())



# Abstraction
# from abc import ABC,abstractclassmethod,classmethod
# class vehicle(ABC):
#     @classmethod
#     @abstractclassmethod
#     def set_mileage(self,mileage):
#         self.mileage=mileage

#     def show_mileage(self):
#         return self.mileage
    

# class car(vehicle):
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def show_mileage(self):
#         return self.mileage
    

# Encapsulation

# Access Modifier
# 1.Public Access Modifier
# 2.Protected Area Modifier


# 1.Public Access Modifier

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# p1=person("Sadanksh",21)

# print(p1.name)

# 2.Protected Area Modifier

# class person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def display(self):
#         print(f"The name of the person is {self.__name} and the age of the person is {self.__age}")


# class student(person):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
    
#     def display(self):
#         print(f"The name of the person is {self.name} and the age of the person is {self.age}")

# s1=student("Sadanksh Gangrade",21)

# s1.display()

# 3.Private Area Modifier

# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age

#     def display(self):
#         print(f"The name of the person is {self._name} and the age of the person is {self._age}")


# class student(person):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
    
#     def display(self):
#         print(f"The name of the person is {self.name} and the age of the person is {self.age}")

# s1=student("Sadanksh Gangrade",21)

# s1.display()



# Modules and Packages

# import math

# from math import factorial

# from math import *

# print(factorial(5))

# import random 

# print(random.randint(1,10))

# Packages
# import numpy as np
# print(np.random.randint(1,10))
