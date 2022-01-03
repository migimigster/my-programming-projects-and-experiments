from coffeemachinedata import menu,resources,menu_interface,clearConsole,print_report,coffee,minus_inventory,refill_inventory
from prettytable import PrettyTable
coffee_maker_done = False
while not coffee_maker_done:

    program_done = False
    clearConsole()
    print("WELCOME TO MY AWESOME COFFEE MACHINE")
    table = PrettyTable()
    ordernumber=['1','2','3','4']
    table.add_column("Order Number",ordernumber)
    table.add_column("Coffee",["Espresso","Latte","Cappuccino","Americano"])
    table.add_column("Price",["$1.5","$2.5","$3","$3.5"])
    print(table)
    while not program_done:
        #This is where customer or user has to input their choices
        coffee_order = menu_interface()
        if coffee_order == 'report':
            #Opens the inventory and total sales
            print_report(resources)
            input("")
            program_done = True
        elif coffee_order == 'off':
            #To end the program
            program_done = True
            coffee_maker_done = True
        elif coffee_order in ordernumber:
            #This is where the customer's order input
            coffee_order=int(coffee_order)
            coffee_order=coffee(coffee_order)
            while True:
                #Input of quantity of customer's order
                try:
                    order_quantity=int(input(f'How many orders do you want for {coffee_order}? '))
                    break
                except ValueError:
                    clearConsole()
                    print("Please input valid number! ")
            order = menu[f'{coffee_order}']
            resources=minus_inventory(order,resources,order_quantity,coffee_order)

            #If customer wants to order again
            press_any_key=input("Press enter to order again! If you do not want to order again please type off\n")
            if press_any_key=='off':
                program_done = True
                coffee_maker_done = True
            else:
                program_done=True
        elif coffee_order=='refill':
            #This is where inventory is refilled
            refill_inventory(resources)
        else:
            #if random or incorrect input has been inputted
            input("\nSorry! I don't know that")
            program_done = True
clearConsole()
input('Thank you for using the machine! Good-bye! ')
clearConsole()