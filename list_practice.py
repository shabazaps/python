# Reverse a list

list1 = [1,2,3,4,5,6]
# list1=list1[::-1]
# # print(list1)
#
# # Other Method to rev a list
#
# # list1.reverse()
# # print(list1)
#
# list1.sort()
# # print(list1)
#
# list1.sort(reverse = True)
# print(list1)


# Insert an element at 3rd position with value 9

# list1.insert(3,9)
# print(list1)

# remove duplicates from a list
# list2=[1,2,3,4,1,3,7,8,5,4,3]
# set1=set(list2)
#
# list2=list(set1)
# print(list2)

# Search for 3 in list1

# n=9
# if n in list1:
#     print(f"{n} is Found!")
# else:
#     print(f"{n} is not Found")

# Searching using index:
# n=3
# flag = False
# for i  in range(len(list1)):
#     if n == list1[i]:
#         flag = True
#         break
# if(flag == True):
#     print("Element Found")
# else:
#     print("Element Not Found")

# Find the Max and min in a list:

list3 = [3,2,5,6,7,9,1]
list3.sort()
max = list3[len(list3)-1]
print(f"Maximum element in the list is {max}")
min= list3[0]
print(f"Minimum element in the list is {min}")

# Sum avg and product of list3
sum=0
avg=0
product = 1
for i in range(len(list3)):
    sum = sum + list3[i]
    product= product * list3[i]

avg = sum/len(list3)

print(f"Sum is {sum},   Average is {int(avg)},   Product is {product}")


# Binary Search

def binary_search(arr,x):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid=(low + high) //2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1





arr=[1,2,3,4,5,6,7,8,9]
x= 3
result = binary_search(arr,x)
if result == -1:
    print(f"{x} not found")
else:
    print(f"{x} was found in index: {result}")
