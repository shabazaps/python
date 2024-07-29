def file():
    f = open("fake_file.txt",'w')
    f.write("Now the file makes sense\n")

    f=open("fake_file.txt",'r')
    print(f.read())

file()