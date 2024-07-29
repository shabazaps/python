# Map Function
# Syntax: map(function, ilterator like list)
#
# def func(n):
#     return n * 10
#
# list1=[1,2,3,4,5]
# result= list(map(func, list1))
#
# print(result)

# Modify String using map

# s = ['sat', 'bat', 'cat', 'mat']
#
# test = list(map(list,s))
# print(test)

# l1 = [1,2,3,4,5,6,7,8,9]

# def multiply(n):
#     return n*10
#
# result = list(map(multiply,l1))
# print(result)


# Modify String using map

s = ['sat', 'bat', 'cat', 'mat']

# def Upper(a):
#     return a.upper()
#
# up_str=list(map(Upper,s))
#
# print(up_str)

# Length of each string in list of strings

s= ['hello', 'world', 'python']

def length(str):
    return len(str)

str_len= list(map(length,s))

print(str_len)
