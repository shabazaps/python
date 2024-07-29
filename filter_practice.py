# from functools import reduce
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# evens = list(filter(lambda n: n , nums))
#
# doubles = list(map(lambda n: n * 2, evens))
#
# sum = reduce(lambda a, b: a + b, doubles)
# # print(sum)
#
#
# # Print Max element
# max_element= reduce(lambda a, b: a if a>b else b, nums)
#
# print(max_element)

# Print all names that start with a

s= ['Alice', 'Bob', 'Anna', 'Alex', 'Eve']

# def start_a(str):
#     return str.startswith('A')
#
# a_str= list(filter(start_a,s))
#
# print(a_str)

def long(str):
    return len(str) > 3

long_word = list(filter(long,s))
print(long_word)