cubes=[]
cubes = [x**3 for x in range(10) if x%2==0]
print(cubes)

#Adding 2 to every element in a list
marks = [10,20,30,40,50]
new_marks=[x+2 for x in marks]
print(new_marks)