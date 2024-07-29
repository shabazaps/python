# t1=(1,2,3,4,5)
#
# l1=list(t1)
# l1[2] = 43
# t2= tuple(l1)
# print(t2)

# s="S h a b a z"
#
# # print(s[::-1])

# s="My name is Shabaz"
#
# l= s.split()
# print(len(l))

# s= "shahbaz ahmed mindfire"
#
# l1 = s.split()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for key, values in thisdict:
#     print(thisdict.keys())
#     break

from functools import reduce

numbers = [1, 2, 3, 4]

product = reduce(lambda x, y: x * y, numbers)

print(product)

l1 = [2, 3, 4, 5, 6, 7, 8, 9]

# n = 4
# print(type(n))
# n = float(n)
# print(type(n))

# def func(*,a,b,c):
#     pass
#
# print(a=3,b=4,c=5)

# for i in range(1,11):
#     if i ==5:
#         continue
#     print(i)

# 1,1,1
# 1,2,1
# 3,3,3


# a= 10
# def print_A():
#     a= a*10
#     print(a)
# print_A()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])
for key in thisdict.keys():
    if key == "brand":
        print(key)


s= "shahbaz ahmed mindfire"

l = s.split()

initials = [l[i][0].upper() for i in range(2)]

result = f"{'.'.join(initials)}.{l[-1].capitalize()}"
print(result)
