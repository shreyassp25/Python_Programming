# Write a program to input eight numbers from the user and display all the unique numbers (once).

list=[]

n1=int(input("enter a num : "))
n2=int(input("enter a num : "))
n3=int(input("enter a num : "))
n4=int(input("enter a num : "))
n5=int(input("enter a num : "))
n6=int(input("enter a num : "))
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)
list.append(n6)

print(f"the unique numbers are : {set(list)}")

