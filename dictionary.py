# # # # # dict1 = {"a": "Hello", "b": "world", "c": "Python"}
# # # # # print(dict1["b"])
# # # # # # assigning keyt to a variable and printing it
# # # # # val = dict1["a"]
# # # # # print(dict1)
# # # # #
# # # # # # Creting keys with different datatypes
# # # # #
# # # # # dict2 = {"a": "Hello", False: "World"}
# # # # #
# # # # #
# # # # # # check if a key exits or not
# # # # # print("a" in dict1)
# # # # # print("a" not in dict1)
# # # # #
# # # # #
# # # # # # Keys() Method
# # # # #
# # # # # val=dict1.keys()
# # # # # print(type(val))
# # # # # # Output dict_keys
# # # # # print(val)
# # # # #
# # # # # print("Hello" in dict1.values())
# # # #
# # # #
# # # # def factorial(n):
# # # #     if n == 0:
# # # #         return 1
# # # #     else:
# # # #         return n * factorial(n - 1)
# # # #
# # # #
# # # # print(factorial(5))
# # # #
# # #
# # # # class Person:
# # # #   def __init__(self, name, age):
# # # #     self.name = name
# # # #     self.age = age
# # # #
# # # # p1 = Person("John", 36)
# # # #
# # # # print(p1.name)
# # # # print(p1.age)
# # #
# # #
# # # # class Person:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #
# # # #     def __str__(self):
# # # #         return f"{self.name}, {self.age}"
# # # #
# # # #
# # # # p1 = Person("John", 36)
# # # #
# # # # print(p1)
# # #
# # #
# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #
# # #     def my_func(self):
# # #         print("Hello my name is " + self.name)
# # #
# # #
# # # p1 = Person("Shabaz", 24)
# # #
# # # p1.my_func()
# # #
# # #
# # #
# # #
# #
# #
# # class Person:
# #     def __init__(self, fname, lname):
# #         self.firstname = fname
# #         self.lastname = lname
# #
# #     def printname(self):
# #         print(self.firstname, self.lastname)
# #
# #
# #
# # x = Person("John", "Doe")
# # x.printname()
# #
# #
# # class Student(Person):
# #     pass
# #
# #
# # x = Student("Mike", "Olsen")
# #
# # x.printname()
#
#
# x = 300
#
# def myfunc():
#   x = 200
#   print(x)
#
# myfunc()
#
# print(x)



def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
