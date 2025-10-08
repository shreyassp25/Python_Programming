# Write a program to find whether a given number is prime or not.

a=7
for i in range(2,a):
    if(a%i==0):
        print("not Prime")
        break 
else:
    print("prime")