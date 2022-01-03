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

def comparison(player_score,cpu_score,cash,bet_amount):
    '''Comparison after hitting the cards'''
    if player_score>21 or (player_score<cpu_score and cpu_score<=21):
        print("You lose")
        cash-=bet_amount
        if cash<0:
            print(f"Your remaining cash is $0")
        else:
            print(f"Your remaining cash is ${cash}")
        return cash
    elif  cpu_score>21 or (player_score>cpu_score and player_score<=21):
        print("You win!")
        cash+=bet_amount
        print(f"Your remaining cash is ${cash}")
        return cash                   
    elif player_score==cpu_score:
        print("It's a draw")
        print(f"Your remaining cash is ${cash}")
        return cash  
def print_interface(cash,betamount,playerhand,playerscore,cpuhand,cpuscore):
    '''This is where it prints the status of the players'''
    print(f"Your remaining cash is ${cash}")
    print(f"Your bet is now ${betamount}")
    print(f"\nPlayer's hand is {playerhand} equal to {playerscore}")
    print(f"CPU's hand is {cpuhand} equal to {cpuscore}\n")

def cpu_smart(cash,betamount,playerhand,playerscore,cpuhand,cpuscore):
    '''if player is done and cpu doesn't have to hit if sure win'''
    clearConsole()
    print_interface(cash,betamount,playerhand,playerscore,cpuhand,cpuscore)
    print("You lose")
    cash-=betamount
    print(f"Your remaining cash is ${cash}")     
    return cash 

def cpu_compute(cpuscore,cpuhand,cash,betamount,playerhand,playerscore):
    '''This is where cpu hits if score is less than 17'''
    while cpuscore!=0 and cpuscore<17:
        cpuhand.append(deal_card())
        cpuscore=calculate_score(cpuhand)
    print_interface(cash,betamount,playerhand,playerscore,cpuhand,cpuscore)
    return cpuscore

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
        while True:
            try:
                bet_amount = int(input("Place your bet! $"))
                break
            except ValueError:
                print("Please input valid number! ")
        if bet_amount<=cash and bet_amount>0:
            clearConsole()
            while not program_done:
                #This is where player and cpu hands' are shown
                player_score=calculate_score(player_hand)
                cpu_score=calculate_score(cpu_hand)
                clearConsole()
                print_interface(cash,bet_amount,player_hand,player_score,cpu_hand,cpu_score)
                #If initial hand is 21 then game is already over
                if player_score==cpu_score and player_score==21:
                    print("It's a draw")
                    print(f"Your remaining cash is ${cash}")
                    break
                elif (player_score==21) and len(player_hand)==2:
                    print("You have won already!")
                    cash+=bet_amount
                    print(f"Your remaining cash is ${cash}")
                    break
                elif (cpu_score==21) or player_score>21:
                    print("You have lost already!")
                    cash-=bet_amount
                    if cash<0:
                        print(f"Your remaining cash is $0")
                    else:
                        print(f"Your remaining cash is ${cash}")
                    break
                else:
                    #This is where players choose to hit, doubledown, split(coming soon) or stand
                    add_card=input("Are you going to:\nHit: y\nDouble Down: d (Note that if you hit once, you cannot double down!)\nStand: n\n").lower()
            #-----HIT! - This is where players can chose to hit another card----------------------------------#
                if add_card =='y':
                    player_hand.append(deal_card())
                    ddown+=1
                    clearConsole()
            #-----STAND! - This is where players stand with computer----------------------------------#
                elif add_card == 'n':
                    #CPU doesn't need to hit if player is done and CPU's score>Player's score
                    if player_score<cpu_score:
                        cash=cpu_smart(cash,bet_amount,player_hand,player_score,cpu_hand,cpu_score)
                        break
                    else:                        
                    #This is where cpu will hit if hand is less than 17 and possible to beat player once player is done
                        clearConsole()
                        cpu_score=cpu_compute(cpu_score,cpu_hand,cash,bet_amount,player_hand,player_score)
                        program_done=True
                    #This is where comparison occurs after hitting
                    cash=comparison(player_score,cpu_score,cash,bet_amount)    
            #-----DOUBLE DOWN! - This is where players will hit another card then their bet amount is increased 2x----------------------------------#
                elif add_card == 'd' and ddown==0:
                    clearConsole()
                    bet_amount*=2
                    player_hand.append(deal_card())
                    player_score=calculate_score(player_hand)
                    #CPU doesn't need to hit if player is done and CPU's score>Player's score
                    if player_score<cpu_score or player_score>21:
                        print(f"Your initial bet was ${int(bet_amount/2)}")
                        cash=cpu_smart(cash,bet_amount,player_hand,player_score,cpu_hand,cpu_score)
                        break
                    else:
                    #This is where cpu will hit if hand is less than 17 and possible to beat player once player is done
                        clearConsole()
                        print(f"Your initial bet was ${int(bet_amount/2)}")
                        cpu_score=cpu_compute(cpu_score,cpu_hand,cash,bet_amount,player_hand,player_score)
                        program_done=True

                    #This is where comparison occurs after hitting
                    cash=comparison(player_score,cpu_score,cash,bet_amount)
                # To make sure that you cannot double down once user hits                    
                elif add_card=='d' and ddown>0:
                    clearConsole()
                    print("You cannot double down once you hit")
                    input("")
                else:
                    clearConsole()
            #when game is over, program asks user if u want to bet again using remaining cash
            if cash==0 or cash<0:
                game_overall = True
                print("\nYou are out of money game over!")
            else:
                restart=input("\nDo you want to bet again? y or n? ").lower()
                if restart=='n':
                    game_overall = True
                    clearConsole()
                    print(f"You have ${cash}! Wow!")
                else:
                    clearConsole()
        else:
            clearConsole()
            print("Bet must not be a zero, a negative value, nor higher than your remaining cash!")
            input("Press any key to continue! ")
            clearConsole()
            game_overall = False
#if users want to quit or no cash remaining
clearConsole()
overall = False
while not overall:
    while True:
        try:
            remaining_cash = int(input("Input your cash-in to play BlackJack! ($1-$1000) $"))
            break
        except ValueError:
            clearConsole()
            print("Input valid cash!")
            input("Press any key to continue")
    if remaining_cash<=0 or remaining_cash>1000:
        clearConsole()
        print("Cash-in must be $1 to $1000!")
        clearConsole()
    else:
        game(remaining_cash)
    play_again = input("Do you want to play again? y or n? ").lower()
    if play_again=='n':
        clearConsole()
        print("Thank you for playing!\n")
        input("Press any key to exit!")
        overall = True
    else:
        clearConsole()