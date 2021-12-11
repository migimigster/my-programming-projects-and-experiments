def main():
  #Awesome Password Generator Project
  import random
  import os
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  #This is where you input how many characters in your password
  print("Welcome to the Awesome Password Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  totalnr=nr_letters+nr_symbols+nr_numbers
  if totalnr<=16 and totalnr>=8:
    password=[]
    s=""
    for i in range(1,nr_letters+1):
      random_char=random.choice(letters)
      password.append(random_char)
    for j in range(1,nr_symbols+1):
      random_sym=random.choice(symbols)
      password.append(random_sym)
    for k in range(1,nr_numbers+1):
      random_num=random.choice(numbers)
      password.append(random_num)
    random.shuffle(password)
    for l in password:
      s+=l

    #Output
    print(f"Your password is: {s}")
    quit()
    
  else:
    print("Password must be 8-16 characters")
    return main()

main()
