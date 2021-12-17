# import random

# def difficulty(x):
#   if x == 'easy':
#     return 10
#   elif x == 'hard':
#     return 5

# def comparison(guess,number,d):
#   if guess>number:
#     print(f"Your guess is too high!")
#     return d-1
#   elif guess<number:
#     print(f"Your guess is too low!")
#     return d-1
#   else:
#     print("Congrats you guessed the number!")

# print("Number Guessing Game!!")
# number = random.randint(1,20)
# print(f"Psst! the solution is {number}")

# difficult = input("Choose a difficulty\ntype 'easy' or 'hard': ").lower()
# d=difficulty(difficult)

# guess=0

# while guess!=number:
#   print(f"You have {d} attempts remaining to guess the number.")
#   guess = int(input("Input your guess! "))

#   d=comparison(guess,number,d)  

#   if d==0:
#     print("You have zero guesses. game over!")
#     break
#   elif guess!=number:
#     print("Guess again")
#--------------MY VERSION-----------------#

import random

def difficulty(x):
  if x == 'easy':
    return 10
  elif x == 'hard':
    return 5

print("Number Guessing Game!!")
number = random.randint(1,20)
print(f"Psst! the solution is {number}")

difficult = input("Choose a difficulty\ntype 'easy' or 'hard': ").lower()
d=difficulty(difficult)

print(f"You have {d} attempts remaining to guess the number.")
guess = int(input("Input your guess! "))
d-=1
while True:
  if guess>number and d!=0:
    print(f"Your guess is too high! You have {d} attempts left")
    d-=1
    guess = int(input("Input your guess again! "))
  elif guess<number and d!=0:
    print(f"Your guess is too low! You have {d} attempts left")
    d-=1
    guess = int(input("Input your guess again! "))
  elif guess!=number and d==0:
    print("You have zero guesses! Game over")
    break
  else:
    print("Congrats! You have guessed the number")
    break