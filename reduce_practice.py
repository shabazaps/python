from functools import reduce as r

# Sum of all squares
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = r(lambda x, y: x + y * y, l1)

print(sum)


# Factorial
# def factorial(n):
#     fact = r(lambda x, y: x * y, range(1, n + 1), 1)
#     return fact
#
#
# factorial_num = list(map(factorial, l1))
# print(factorial_num)


