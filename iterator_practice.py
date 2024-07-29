# s="Hello World"
#
# myit = iter(s)
# for i in range(len(s)):
#     print(next(myit))

# class Myiter:
#     def __init__(self):
#         self.num =0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
#
#
# v = Myiter()
# for i in v:
#     print(i)
#


# class Myiter:
#
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <=10:
#             val = self.num
#             self.num += 1
#             return val
#
#         else:
#             raise StopIteration
#
#
# v= Myiter()
#
# for i in v:
#     print(i)

# l1=[1,2,3,4,5,6,7,8,9,10]

# for i in l1:
#     print(i)

# my_iter = iter(l1)
#
# for i in my_iter:
#     print(i)

# def even(l1):
#     l2=[]
#     for i in l1:
#         if i%2==0:
#             l2.append(i)
#     return l2
#
#
# l1=[1,2,3,4,5,6,7,8,9,10]
#
# ev_iter = even(l1)
#
# for i in ev_iter:
#     print(i)




