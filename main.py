# # # # # # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # # # # # thislist.reverse()
# # # # # # print(thislist)
# # # # # #
# # # # # # print(thislist)
# # # # # #
# # # # # #
# # # # # # list1 = ["apple", "banana", "cherry"]
# # # # # # # list2=list1
# # # # # # # list2=list1.copy()
# # # # # # list2 = list(list1)
# # # # # # print(list2)
# # # # # #
# # # # # #
# # # # # # tupl=( 23j)
# # # # # #
# # # # # #
# # # # # # print(tupl)
# # # # # # print(type(tupl))
# # # # # #
# # # # #
# # # # #
# # # # #
# # # # # fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# # # # #
# # # # # (green, yellow, *red) = fruits
# # # # #
# # # # # print(green)
# # # # # print(yellow)
# # # # # print(red)
# # # # #
# # # # #
# # # # # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# # # # #
# # # # # (green, *tropic, red) = fruits
# # # # #
# # # # # print(green)
# # # # # print(tropic)
# # # # # print(red)
# # # #
# # # #
# # # #
# # # # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# # # #
# # # # (green, *tropic, red) = fruits
# # # #
# # # # print(green)
# # # # print(tropic)
# # # # print(red)
# # #
# # #
# # # fruits = ("apple", "banana", "cherry")
# # # mytuple = fruits * 2
# # #
# # # print(mytuple)
# #
# #
# # thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False}
# #
# # print(thisset)
#
#
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.intersection_update(set2)
#
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.difference_update(set2)
#
# print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)