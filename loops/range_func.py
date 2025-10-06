# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:

# range(start, stop, step_size)
# step_size is usually not used with range()

for i in range(0,7):
    print(i)

# using for loop with else statement

for i in range (0,4):
    print(i)
else:
    print("done")

# break statement

#‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break    

# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)




# pass is a null statement in python. It instructs to “do nothing”.


l = [1,7,8]
for item in l:
    pass # without pass, the program will throw an error