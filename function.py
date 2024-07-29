# def argss(*,x):
#     print(x)
#
# argss(x="RV")
#
#
# def kwargs(x,/):
#     print(x)
#
# kwargs(3)
#
# def argkwrg(a,b,c,/,*,d,e,f):
#     print(a+b+c+d+e+f)
#
# argkwrg(5,5,5,d=5,e=5,f=5)
#
#
#  Recursive function:

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(3))

# using function as arguments to other function

def operation_apply(operation, a, b):
    return operation(a,b)

def multiply(a,b):
    return a * b

result = operation_apply(multiply,3,6)

print(result)



