from higherorlowerart import logo,vs
from higherorlowergame_data import data
import random
import os

def clearConsole():
    '''Clearing the console'''
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def randgen():
    return random.choice(data)

def format(acc):
    name= acc["name"]
    desc= acc["description"]
    cou = acc["country"]
    fol = acc["follower_count"]
    return f"{name}, a {desc}, from {cou} with {fol} followers"

def check_ans(guess,A_count,B_count):
    if A_count>B_count:
        return guess=='A'
    else:
        return guess=='B'
def print_interface(A,B):
    print(logo)
    print(f"Compare A: {format(A)}")
    print(vs)
    print(f"Against B: {format(B)}")
    
def game():
    score=0 
    A=randgen()   
    B=randgen()
    game_not_done=True
    while game_not_done:
        A=B
        while A==B:
            B=randgen()
        print_interface(A,B)
        guess = input("Which person has the highest follower? ").upper()
        A_count=A["follower_count"]
        B_count=B["follower_count"]
        iscorrect=check_ans(guess,A_count,B_count)
        if iscorrect:
            clearConsole()
            score+=1
            print(f"You are right! Your score is {score}")
        else:
            print(f"\nYou are wrong! Your final score is {score}")
            game_not_done=False

clearConsole()
program_done = False
while not program_done:
    game()
    restart=input("Do you want to play again? y or n? ").lower()
    if restart == 'n':
        clearConsole()
        print("Thank you for playing!")
        program_done=True
    elif restart=='y':
        clearConsole()
