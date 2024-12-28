##print formatiing is a method by which chnages can be made during print without actually tyoing out the change

### 2 methods- .format() and f-strings

name=input("enter your name: ")
print("hello there {}".format(name))


print("the {2} {1} {0}".format("fox","brown","quick"))
    
print("my name is {a} {b}".format(a="anthony",b="golsalves"))

### float formatting follows the synatx-   {value:width.precisionf}


result=100/77
print(result)
print("result is {r:1.3f}.".format(r=result))

#####  string literal method

print(f"hello there {name}")





