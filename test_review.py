# reverse a string
import keyword

s = "Shabaz"
# print(s[::-1])

# s1 = ""
# for i in range(len(s)):
#     s1=  s[i]+s1
#
# print(s1)
#
# s2=""
# for i in s:
#     s2 = i +s2
# print(s2)
#

# Using Lambda

# s3 = lambda s:s[::-1]
# print(s3(s))
#
# a = lambda x, y: x + y
#
# print(a(1, 2))
# print(a)
#
l = [5, 2, 7, 1, 0, 6]
#
#
# # l.sort()
# # print(l)
#
# n= len(l)
#
# for i in range(n):
#     for j in range(0,n-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]= l[j+1],l[j]
# print(l)

# from collections import OrderedDict
# dict1 ={
#     5:"Shabaz",
#     2:"John",
#     8:"Kevin"
# }
#
# print(OrderedDict(sorted(dict1.items())))
#
# print(dict1.keys())
#
# # dict1.pop(5)
# # print(dict1)
# #
# # dict2 = {
# #     9: "Ben",
# #     1: "carl"
# # }
# # dict1.update(dict2)
# # print(dict1)
#
#
# def frequncy(s):
#     freq = {}
#     for i in s:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return freq
#
#
s = "ShabazShabaz"
# print(frequncy(s))

def frequency(s):
    freq = {}

    for i in s:
        if i in freq:
            freq[i] +=1
        else:
            freq[i]=1
    return freq

print(frequency(s))
#
# # class Animal:
# #     def sound(self):
# #         print("Animal makes sound")
# #
# # class Dog(Animal):
# #     def sound(self):
# #         print("Dog Barks")
# #
# # a = Animal
# # print(a.sound(1))
# # d= Dog
# # print(d.sound(2))
#
# # list1 = [1,2,3,4,5]
# #
# # iter1 = iter(list1)
# #
# # print(next(iter1))
# # print(next(iter1))
# # print(next(iter1))
# # print(next(iter1))
# # print(next(iter1))
# #
# #
#
# # def func(a, b):
# #     return a + b
# #
# #
# # def func1(a, /, b, *, c):
# #     pass
#
# l1 = [3,2,0,9,5, 1,10 ,11]
# l1.sort()
# print(l1)
#


# l2 =["a","aa","b","bb"]
# l2.sort()
# print(l2)
#

dict1 ={
    5:"Shabaz",
    2:"John",
    8:"Kevin"
}

# from collections import OrderedDict
#
# print(OrderedDict(sorted(dict1.items())))
# print(type(dict1))
#
# dict1.update({9: "rahul", 1: "Aditya"})
# print(dict1.keys())
# print("Sorted Dictionary according to Keys are:" )
# od_dict =OrderedDict(sorted(dict1.items()))
#
# print(od_dict)




