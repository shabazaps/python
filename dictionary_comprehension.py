# Dictionary Comprehension

# Creating a simple dictionary with i as key and i square as value

# print({i:i**2 for i in range(1,6)})
#
# marks = [35,50,70,90,15,43]
#
# m = ({i:("Good Marks" if i>50 else "Study harder" ) for i in marks})
#
# print(m)


# Character Frequency

# s="HelloWorld"
#
# freq=({i: s.count(i) for i in s})
# print(freq)


# check if even or odd

# eo =({i:("Even" if i% 2==0 else "Odd") for i in range(1,20)})
# print(eo)

# Length of word

word= ["hello","World", "Kolkata", "Delhi", "Lenovo"]

length=({i:len(i) for i in word})
print(length)

# temp_c * 9/5 + 32

# Convert temp from Celsius to Fahrenheit
#  * 9/5 + 32

# f=[78,90,43,53,76]
#
# c = ({i:(i* 9/5 + 32) for i in f})
#
# print(c)


