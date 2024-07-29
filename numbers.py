# printing Prime upto the Number

# def ifprime(n):
#     if n<=1:
#         return None
#
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# def prime_gen():
#     list1=[2]
#     n=int(input("Enter the range: "))
#     for i in range(3,n):
#        if ifprime(i):
#         list1.append(i)
#     print(list1)
#
# prime_gen()


# factorial

# def fact(n):
#
#     s = 1
#     for i in range(1,n):
#         s = s * i
#     print(f"The factorial of {n} is: {s}")
#
# fact(6)

# def fibo(n):
#     a = 1
#     b = 1
#     c = 0
#     print(f"The Fibonacci series upto {n} is: ")
#     print(a)
#     print(b)
#     for i in range(3,n+1):
#         c = a + b
#         print(c)
#         a = b
#         b = c
# fibo(7)