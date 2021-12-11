def main():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    import random

    #Welcome! this where you set how many rounds
    print("Welcome to awesome Rock, Paper, and Scissors Game!\nCoded by Migimigster\n")
    best_of=int(input("Choose how many rounds "))

    if best_of%2==0 or best_of<0:
        print("Best of score must be odd or positive number.")
    else:
        #Where the game really goes
        user_score=0
        cpu_score=0

        #Rock=0, Paper=1, Scissor=2
        for i in range (0,best_of):
            x=input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors. ")
            y=random.randint(0,2)
            x=int(x)

            images=[rock,paper,scissors]
            if x<0 or x>2:
                print("Invalid input")
            else:
                print(f"You chose: {images[x]}")
                print(f"Computer chose: {images[y]}")
            #Rock=0, Paper=1, Scissor=2
            if x==y:
                print(user_score,cpu_score)
            elif x==0 and y==2:
                user_score+=1
                print(user_score,cpu_score)
            elif x<y:
                cpu_score+=1
                print(user_score,cpu_score)
            elif x==2 and y==0:
                cpu_score+=1
                print(user_score,cpu_score)
            elif x<0 or x>2:
                print("Invalid draw. Penalty! Be careful!")
                cpu_score+=1
                print(user_score,cpu_score)
            else:
                user_score+=1
                print(user_score,cpu_score)

        #If round input ends, here is the result!    
        if best_of == user_score+cpu_score:
            print("Game Over!")
        if user_score>cpu_score:
            print("You win!")
        elif user_score==cpu_score:
            print("It's a draw!")
        else:
            print("You lose")

main()