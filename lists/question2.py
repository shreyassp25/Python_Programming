# Write a program to accept marks of 6 students and display them in a sorted manner

marks=[]

m1=int(input("enter marks : "))
m2=int(input("enter marks : "))
m3=int(input("enter marks : "))
m4=int(input("enter marks : "))
m5=int(input("enter marks : "))
m6=int(input("enter marks : "))
marks.append(m1)
marks.append(m2)
marks.append(m3)
marks.append(m4)
marks.append(m5)
marks.append(m6)

marks.sort()

print(marks)



