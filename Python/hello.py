#set the password and the attempt limit
password = ('Domino')
guess = ""
password_count = 0
password_limit = 3
out_of_limit = False

#this is where you input your password
while guess != password and not(out_of_limit):
    if password_count<password_limit:
        guess = input("What is the secret word? ")
        password_count +=1
        if guess == password:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        out_of_limit = True
#output when you guessed the password
if out_of_limit == True:
    print("No more attempt")
else:
    print("You may enter!")