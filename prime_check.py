def check_prime(n):
    flag = False
    if n <= 1:
        print("This number is neither prime nor composite.")
    else:
        for x in range(2, n):
            if n % x == 0:
                flag = True
                break  
        if flag==True:
            print("The number is not prime.")
        else:
            print("The number is prime.")

n = int(input("Enter a number: "))
check_prime(n)
