from coffeemachinedata import menu,resources
import os
real_program_done = False

def clearConsole():
    '''Clearing the console'''
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def money_count(orders,quantity):
    print("Please insert coins to pay!\n")
    while True:
        try:
            c_quarter=float(input("How many quarters? "))*0.25
            break
        except ValueError:
            print("Please input valid number!")
    while True:
        try:
            c_dime=float(input("How many dimes? "))*0.10
            break
        except ValueError:
            print("Please input valid number!")
    while True:
        try:
            c_nickel=float(input("How many nickels? "))*0.05
            break
        except ValueError:
            print("Please input valid number!")
    while True:
        try:
            c_penny=float(input("How many pennies? "))*0.01
            break
        except ValueError:
            print("Please input valid number!")
    total_money = round((c_quarter+c_dime+c_nickel+c_penny)-(orders['cost'])*quantity,2)
    if total_money<0:
        return total_money
    else:
        print(f'\nI received ${round(c_quarter+c_dime+c_nickel+c_penny,2)}')
        print(f'Your change is: ${total_money}')
        return total_money

def minus_inventory(orders,inventory,quantity):
    rem_water=int(inventory['water']-(orders['ingredients']['water'])*quantity)
    rem_coffee=int(inventory['coffee']-(orders['ingredients']['coffee'])*quantity)
    rem_milk=int(inventory['milk']-(orders['ingredients']['milk']*quantity))
    sales=float(round(inventory['cash']+orders['cost'],2))*quantity
    new_inventory = {
        "water": rem_water,
        "milk": rem_milk,
        "coffee": rem_coffee,
        "cash": sales
    }
    if new_inventory["water"]<0:
        print("Not enough water!")
        return inventory
    elif new_inventory["coffee"]<0:
        print("Not enough coffee!")
        return inventory
    elif new_inventory["milk"]<0:
        print("Not enough milk!")
        return inventory
    else:
        clearConsole()
        print(f'You ordered {quantity} cups of {coffee_order}')
        print(f'Your bill is ${orders["cost"]*quantity}')
        cash=money_count(order,order_quantity)
        if cash<0:
            print("You do not have enough money!!")
            return inventory
        else:
            if quantity>1:
                print(f'Here are your {coffee_order}s ☕! Enjoy!')
                return new_inventory
            else:
                print(f'Here is your {coffee_order} ☕! Enjoy!')
                return new_inventory
while not real_program_done:

    program_done = False
    clearConsole()
    print("WELCOME TO MY AWESOME COFFEE MACHINE")
    while not program_done:
        cash=0
        coffee_order = input("What would you like to order?\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00\nTo turn off the machine, please type 'off'\n\n").lower()
        if coffee_order == 'report':
            clearConsole()
            print(f'Water: {resources["water"]} ml')
            print(f'Coffee: {resources["coffee"]} g')
            print(f'Milk: {resources["milk"]} ml')
            print(f'Sales: ${resources["cash"]}')
            input("Press any key to continue ")
            program_done = True
        elif coffee_order == 'off':
            program_done = True
            real_program_done = True
        elif coffee_order == 'espresso' or coffee_order=='latte' or coffee_order=='cappuccino':
            while True:
                try:
                    order_quantity=int(input(f'How many orders do you want for {coffee_order}? '))
                    break
                except ValueError:
                    clearConsole()
                    print("Please input valid number! ")
            order = menu[f'{coffee_order}']
            resources=minus_inventory(order,resources,order_quantity)
            press_any_key=input("Press enter to order again! If you do not want to order again please type off\n")
            if press_any_key=='off':
                program_done = True
                real_program_done = True
            else:
                program_done=True
        else:
            print("\nSorry! I don't know that")
            input("Press enter to continue")
            program_done = True
clearConsole()
print('Thank you for using the machine! Good-bye')