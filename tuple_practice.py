# Tuple Unpacking
tup = ("Apple", "Banana", "Mango")
# [a,b,c]=tup
# print(a,c,b)

# Index accessing using tuple
for i in range(len(tup)):
    pass
   # print(tup[i])


# Concat 2 tuples

tup1=("Cherry","Kiwi","Avacado")

tup = tup+tup1
#print(tup)
# Count the number of occurences in tuple of a particular element
#print(tup.count("Banana"))

# copy tuple
tup3 = tuple(tup)
#print(tup3)

# search an element in tuple
#print("Apple" in tup3)


# length of tuple
#print(len(tup3))

#check if 2 tuples are equal

#print(tup == tup3)


# Merge & Remove duplicate from a tuple
tup2 = tup+ tup3
set1 = set(tup2)
#print(set1)
tup4 = tuple(set1)

# Concatenate elements of a tuple into a single string.
s=""
for i in range(len(tup4)):
    s = s + " "+ tup4[i]
print(s)