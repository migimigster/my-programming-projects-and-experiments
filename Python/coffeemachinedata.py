import os
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "americano": {
        "ingredients": {
            "water": 300,
            "milk": 75,
            "coffee": 32,
        },
        "cost": 3.5,
    }
}

resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 10000,
    "cash": 0
}
def coffee(customer_order):
    if customer_order==1:
        return 'espresso'
    elif customer_order==2:
        return 'latte'
    elif customer_order==3:
        return 'cappuccino'
    elif customer_order==4:
        return 'americano'
def clearConsole():
    '''Clearing the console'''
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def print_interface(resources):
    clearConsole()
    print(f'Water: {resources["water"]} ml')
    print(f'Coffee: {resources["coffee"]} g')
    print(f'Milk: {resources["milk"]} ml')
    print(f'Sales: ${resources["cash"]}')
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
def minus_inventory(orders,inventory,quantity,coffee_order):
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
        cash=money_count(orders,quantity)
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
def refill_inventory(inventory):
    clearConsole()
    refill_ing=input("Which ingredient would you like to refill? Water? Coffee? Milk?\n").lower()
    if refill_ing=='water':
        quan=int(input("How many milliliters of water? "))
        inventory['water']=int(inventory['water']+quan)
    elif refill_ing=='coffee':
        quan=int(input("How many grams of coffee? "))
        inventory['coffee']=int(inventory['coffee']+quan)
    elif refill_ing=='milk':
        quan=int(input("How many milliliters of milk? ")) 
        inventory['milk']=int(inventory['milk']+quan)
    else:
        clearConsole()
        return inventory
    print(f'Water: {inventory["water"]} ml')
    print(f'Coffee: {inventory["coffee"]} g')
    print(f'Milk: {inventory["milk"]} ml')
    input("Press enter to continue")
    clearConsole()
    return inventory

def menu_interface():
    x=input("What would you like to order? (Input their respective number.\n1. Espresso: $1.50\n2. Latte: $2.50\n3. Cappuccino: $3.00\n4. Americano: $3.50\nTo turn off the machine, please type 'off'\n\n").lower()
    return x