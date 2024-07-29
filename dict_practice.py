dict1={
    "Name": "Shabaz",
    "roll": 43,
    "City": "Kolkata"
}
# Access value by key
# print(dict1.get("Name"))

# Changing Value from a Dictionary
# dict1["Name"] ="Roids"

# Removing key value pair
del dict1["Name"]
# print(dict1.get("Name"))

# Add new key value
dict1.setdefault("State","West Bengal")
# print(dict1.get("State"))

# Check if a key exists
# print("State" in dict1.keys())

dict2={
    "Country":"India",
    "Age": 24
}

# merge dictionaries using loops
# for key, value in dict2.items():
#     dict1[key] = value

# print(dict1)

# merge dictionaries using update()

dict1.update(dict2)
# print(dict1)

# Check Eqaulity

print(dict1==dict2)

# sort dictionary
