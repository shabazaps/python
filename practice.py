# # # from functools import reduce
# # #
# # # l1=[1,2,3,4,5]
# # #
# # # sq=[x*x for x in l1]
# # # print(sq)
# # #
# # # def double(n):
# # #     return n*2
# # # print(list(map(double,l1)))
# # #
# # # def even(n):
# # #     return n%2==0
# # #
# # # print(list(filter(even,l1)))
# # #
# # # print(reduce(lambda x,y:x*y, l1))
# # #
# # # def postive(l1):
# # #     return list(filter(lambda x:x>0, l1))
# # #
# # # print(postive(l1))
# #
# # # change elements of a tuple:
# #
# # # tup1=(1,2,3,4,5)
# # # l1= list(tup1)
# # # l1[2]=43
# # # tup1=tuple(l1)
# # # print(tup1)
# #
# # # prime numbers upto 20
# # #
# # # print("Prime numbers till 20 are:")
# # # l1=[]
# #
# # # for i in range(2,20+1):
# # #     is_prime = True
# # #     for j in range(2,int(i/2)+1):
# # #         if i%j==0:
# # #             is_prime= False
# # #             break
# # #     if is_prime:
# # #         l1.append(i)
# # # print(l1)
# #
# # s= "ShabazAhmed"
# # freq={}
# #
# # for i in s:
# #     if i in freq:
# #         freq[i] +=1
# #     else:
# #         freq[i]=1
# #
# # print(freq)
#
# l1 = [1, 2, 3, 4, 5, 6]
# #
# # my_iter = iter(l1)
# #
# # for i in my_iter:
# #     print(i)
# #
# # def sq(nums):
# #     for i in nums:
# #         yield i*i
# #
# # sq_nums= sq(l1)
# #
# # for i in sq_nums:
# #     print(i)
#
# x = lambda x: x * x
#
# print(x(10))
#
# x = lambda x, y: x * y
#
# print(x(10, 2))
#
#
# # print(list(filter(lambda x: x%2==0,l1)))
#
# def multiply(n):
#     return n * 10
#
#
# # multi = list(map(multiply,l1))
#
# multi = list(map(lambda x: x * 10, l1))
# print(multi)
#
# # freq of each character
#
# s= "HelloWorldShabazAhmed"
#
# freq={}
#
# for i in s:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i]=1
#
# print(freq)
#
# # s= "ShabazAhmed"
# # freq={}
# #
# # for i in s:
# #     if i in freq:
# #         freq[i] +=1
# #     else:
# #         freq[i]=1
# #
# # print(freq)
from functools import reduce

# # # prime numbers upto 20
# # #
# n= int(input("Enter the range of prime numbers: "))
#
# l1=[]
#
# for i in range(2, n+1):
#     is_prime= True
#     for j in range(2, int(i/2)+1):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         l1.append(i)
#
# print(l1)



#
# for i in range(2,20+1):
#     is_prime = True
#     for j in range(2,int(i/2)+1):
#         if i%j==0:
#             is_prime= False
#             break
#     if is_prime:
#         l1.append(i)
# print(l1)


# l1= [1,2,3,4,5]
#
# sum = reduce(lambda a,b: a+b,l1)
# print(sum)
#
#
# double_l1= [x*2 for x in l1 if x%2==0]
#
# print(double_l1)

marks = [70,76,43,53,67,63]

m = ({ i:("good Marks" if i>50 else "Study hard")for i in marks})
print(m)