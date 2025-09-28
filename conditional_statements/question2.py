# Write a program to find the greatest of four numbers entered by the user

a=int(input("Enter a num: "))
b=int(input("Enter a num: "))
c=int(input("Enter a num: "))
d=int(input("Enter a num: "))
if  (a>b)&(a>c)&(a>d):
    print(" a is the greatest")
elif(b>a)&(b>c)&(b>d):
    print(" b is the greatest")
elif(c>a)&(c>b)&(c>d):
    print("c is the gretest")
else:
    print('d is the greatest')    
