# 1. string length
# strings are immutable, changes made to strings should be assigned to another variable to see the changes made.
#strings cannot be changed by running any functions on them.

name='shreyas'

print(len(name))

b=len(name)

print(b)

print(name.endswith('yas'))

print(name.capitalize())

s='Hello world'

index=s.find('world')

print("index = ", index)

s.replace("world","duniya")
print(s)

replaced=s.replace("world", "duniya")

print(replaced)



k=str(input("Enter your name: "))
print(f"good afternoon, {k}")




