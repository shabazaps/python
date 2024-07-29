# # def gen():
# #     yield 1
# #     yield 2
# #
# # print(next(gen()))
#
# def square_gen(nums):
#     for i in nums:
#         yield i * i
#
#
# sq_nums = square_gen([1, 2, 3, 4, 5])
#
# print(sq_nums)
#
# for i in sq_nums:
#     print(i)
#

# Passing function as an argument:

# def shout(text):
#     return text.upper()


# def whisper(text):
#     return text.lower()
#
#
# def greet(func):
#     greetings = func("Hi, from inside the function")
#     print(greetings)
#
#
# greet(shout)
#
# greet(whisper)

# Returning functions from another function.

# def create_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
#
# add_15 = create_adder(15)
#
# print(add_15(10))


# Modifying a function

# def divide(a, b):
#     print( a/b)
#
# def smart_div(func):
#     def inner(x,y):
#         if x < y:
#             x,y = y,x
#         return func(x,y)
#     return inner
#
# div = smart_div(divide)
#
# div(2,10)


nums=[1,2,3,4,5,6,7,8,9]
def sq(nums):
    for i in nums:
        yield i*i

sq_nums=sq(nums)

for i in sq_nums:
    print(i)