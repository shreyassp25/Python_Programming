newfile=open("myfile.txt")
print(newfile.read())
print(newfile.read())
newfile.seek(0)
print(newfile.read())
print(newfile.readlines())

