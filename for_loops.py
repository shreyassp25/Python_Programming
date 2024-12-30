# for loops are used to iterate over every element of an object
#example practice code for for loops

my_iterable=[1,2,3,4]
for item_name in my_iterable:
    print(item_name)

############################### For loop to check if the numbers in a list are odd or even
my_list=[1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    if (num%2==0):
        print(f"the number {num} is even")
    else:
        print(f"the number {num} is odd")

############################## sum of elements in a list
sum=0
for i in my_list:
    sum = sum + i
    
print(sum)
#############################
list1=[(1,2),(3,4)]
for (a,b) in list1:
    print(a)
    print(b)
    



