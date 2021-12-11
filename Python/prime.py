
num = [1, 2, 3, 4, 5, 6]

# To take input from the user
#num = int(input("Enter a number: "))
# define a flag variable
x = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            x = True
            # break out of loop
            break
else:
    print(num, "is not a prime number")
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")