# there are methods that u can use to make changes to lists
# unlike in strings, changes can be made to lists as they are mutable

l1=[6,3,1,4,7,9,0,8]


# to sort a list

l1.sort()


print (l1)

# to reverse a list

l1.reverse()

print(l1)

# to insert an element

l1.insert(2, 99)
print(l1)

# to pop an element from the list

l1.pop(2)
print(l1.pop(2))
print(l1)

# to add an element to the end of the list

l1.append(69)
print(l1)

# to remove an element

l1.remove(69)
print(l1)

# by pop without any index will pop last one by default

l1.pop()
print(l1)