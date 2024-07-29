# set1= {1,2,3,4,5}
#
# # Adding elements to Set
# set1.update({4,5,6,7})
#
#
# # Remove elements from a set
# set1.remove(6)
#
#
# # check if element exist
# print(5 in set1)
#
# # check length
# print(len(set1))
#
# # Check subset
# # print(set1.issubset(set1))
#
# # check if Disjoint(NO Common element)
#
# # set2 = {11,23}
# # print(set1.isdisjoint(set2))
#
# # Finding max and min
#
# # By Conevrting to list
# list1 = list(set1)
# list1.sort()
# max=list1[len(list1)-1]
# min = list1[0]
# print(f"The max is {max} and min is {min}")
# set2=set(list1)
#
# # By max min method
#
#
set1 = {3, 1, 4, 1, 5, 9}

max_v = max(set1)
min_v = min(set1)

print(f"The max is {max_v} and min is {min_v}")

#
#
#
#
