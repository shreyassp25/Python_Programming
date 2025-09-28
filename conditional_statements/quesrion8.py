# Write a program to find out whether a given post is talking about “Harry” or not

p1="Harry"

post=input("Enter post text: ")

if(p1.lower() in post.lower()):
    print(" yes, talking about harry")
else:
    print("not talking aabout harry")

    