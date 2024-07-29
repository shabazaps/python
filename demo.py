# x = 5.6j
#
# print(type(x))
#
# x= 6
# print(type(x))
#
# s = "Shabaz"
# s= "World"
#
# """
# print(s)
# """
#
# list1 = [1, 2, 3, 4, 5]
#
# print(list1[-1:-6:-1])
#
# # for i in range(len(list1)):
# #     print(list1[i])
#
# print(list1.pop(2))
#
# print(list1)
#

list1 = [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 0]

# list1 = list1 + list2

for i in range(len(list2)):
    list1.append(list2[i])

# print(list1)

my_dict={
    "name":"Shabaz",
    "roll":53,
    "state": "Bengal"
}
my_dict.update("city","Kolkata")

print(my_dict)