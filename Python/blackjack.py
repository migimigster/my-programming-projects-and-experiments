import random
import os

def deal_card():
    '''This is where cards are randomly chosen from the list'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(array):
    '''This is where scores are calculated'''
    if sum(array)==21 and len(array)==2:
        return 21

    if 11 in array and sum(array)>21:
        array.remove(11)
        array.append(1)

    sum_array=sum(array)
    return sum_array

def clearConsole():
    '''Clearing the console'''
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    
from blackjackart import logo

def game(cash):
    game_overall=False
    while not game_overall:

        print(logo)
        print("Welcome to the awesome python BlackJack! ")
        player_hand = []
        cpu_hand = []
        ddown=0
        program_done=False
        #This is where cards are append on player and cpu's hand. Also user will input bet amount
        for i in range(2):
            player_hand.append(deal_card())
            cpu_hand.append(deal_card())
        print(f"Your remaining cash is ${cash}")
        bet_amount = int(input("Place your bet! $"))
        if bet_amount<=remaining_cash:
            clearConsole()
            while not program_done:

                #This is where player and cpu hands' are shown
                player_score=calculate_score(player_hand)
                cpu_score=calculate_score(cpu_hand)
                print(f"You remaining cash is ${remaining_cash}")
                print(f"You bet ${bet_amount}")
                print(f"\nPlayer's hand is {player_hand} equal to {player_score}")
                print(f"CPU's hand is {cpu_hand} equal to {cpu_score}\n")

                #If initial hand is 21 then game is already over
                if player_score==cpu_score and player_score==21:
                    print("It's a draw")
                    print(f"Your remaining cash is ${cash}")
                    break
                elif player_score==21 or cpu_score>21:
                    print("You win!")
                    cash+=bet_amount
                    print(f"Your remaining cash is ${cash}")
                    break
                elif cpu_score==21 or player_score>21:
                    print("You lose!")
                    cash-=bet_amount
                    print(f"Your remaining cash is ${cash}")
                    break
                else:
                    #This is where players choose to hit, doubledown, split(coming soon) or stand
                    add_card=input("Are you going to: Hit: y\n                  Double Down: d (Note that if you hit once, you cannot double down!)\n                  Stand: n\n")
            #-----HIT! - This is where players can chose to hit another card----------------------------------#
                if add_card =='y':
                    player_hand.append(deal_card())
                    ddown+=1 # To make sure that you cannot double down once user hits
                    clearConsole()
            #-----STAND! - This is where players stand with computer----------------------------------#
                elif add_card == 'n':
                    clearConsole()
                    #This is where cpu will hit if hand is less than 17
                    while cpu_score!=0 and cpu_score<17:
                        cpu_hand.append(deal_card())
                        cpu_score=calculate_score(cpu_hand)
                    print(f"Your remaining cash is ${remaining_cash}")
                    print(f"Your bet is ${bet_amount}\n")
                    print(f"Player's hand is {player_hand} equal to {player_score}")
                    print(f"CPU's hand is {cpu_hand} equal to {cpu_score}")
                    program_done=True

                    #This is where comparison occurs after hitting
                    if  cpu_score>21 or (player_score>cpu_score and player_score<=21):
                        print("You win!")
                        cash+=bet_amount
                        print(f"Your remaining cash is ${cash}")                    
                    elif player_score==cpu_score:
                        print("It's a draw")
                        print(f"Your remaining cash is ${cash}")                    
                    elif player_score>21 or (player_score<cpu_score and cpu_score<=21):
                        print("You lose")
                        cash-=bet_amount
                        print(f"Your remaining cash is ${cash}")
            #-----DOUBLE DOWN! - This is where players will hit another card then their bet amount is increased 2x----------------------------------#
                elif add_card == 'd' and ddown==0:
                    clearConsole()
                    bet_amount*=2
                    player_hand.append(deal_card())
                    player_score=calculate_score(player_hand)
                #This is where cpu will hit if hand is less than 17
                    while cpu_score!=0 and cpu_score<17:
                        cpu_hand.append(deal_card())
                        cpu_score=calculate_score(cpu_hand)
                    print(f"Your remaining cash is ${remaining_cash}")
                    print(f"Your bet became ${bet_amount}\n")
                    print(f"Player's hand is {player_hand} equal to {player_score}")
                    print(f"CPU's hand is {cpu_hand} equal to {cpu_score}")
                    program_done=True

                    #This is where comparison occurs after hitting
                    if player_score>21 or (player_score<cpu_score and cpu_score<=21):
                        print("You lose")
                        cash-=bet_amount
                        print(f"Your remaining cash is ${cash}")
                    elif  cpu_score>21 or (player_score>cpu_score and player_score<=21):
                        print("You win!")
                        cash+=bet_amount
                        print(f"Your remaining cash is ${cash}")                   
                    elif player_score==cpu_score:
                        print("It's a draw")
                        print(f"Your remaining cash is ${cash}")                    

            #when game is over, program asks user if u want to bet again using remaining cash
            if cash==0 or cash<0:
                game_overall = True
                print("\nYou are out of money game over!")
            else:
                restart=input("\nDo you want to bet again? y or n? ")
                if restart=='n':
                    game_overall = True
                    clearConsole()
                    print(f"\nYou have ${cash}! Wow!")
                else:
                    clearConsole()
        else:
            clearConsole()
            print("Bet must not be zero,negative value, or higher than your remaining cash!")
            input("Press any letter to continue! ")
            game_overall = False
#if users want to quit or no cash remaining
overall = False
while not overall:
    remaining_cash = int(input("Input your cash-in to play BlackJack! (Max: $1000) $"))
    if remaining_cash<=0 or remaining_cash>1000:
        clearConsole()
        print("Cash-in must be $1 to $1000!")
    else:
        game(remaining_cash)
    play_again = input("Do you want to play again? y or n? ")
    if play_again=='n':
        clearConsole()
        print("Thank you for playing!")
        overall = True
    else:
        clearConsole()