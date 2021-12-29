from coffeemachinedata import menu,resources,menu_interface,clearConsole,print_interface,coffee,minus_inventory,refill_inventory
real_program_done = False
while not real_program_done:

    program_done = False
    clearConsole()
    print("WELCOME TO MY AWESOME COFFEE MACHINE")
    while not program_done:

        coffee_order = menu_interface()
        if coffee_order == 'report':
            print_interface(resources)
            input("")
            program_done = True
        elif coffee_order == 'off':
            program_done = True
            real_program_done = True
        elif coffee_order == '1' or coffee_order=='2' or coffee_order=='3' or coffee_order=='4':
            coffee_order=int(coffee_order)
            coffee_order=coffee(coffee_order)
            while True:
                try:
                    order_quantity=int(input(f'How many orders do you want for {coffee_order}? '))
                    break
                except ValueError:
                    clearConsole()
                    print("Please input valid number! ")
            order = menu[f'{coffee_order}']
            resources=minus_inventory(order,resources,order_quantity,coffee_order)
            press_any_key=input("Press enter to order again! If you do not want to order again please type off\n")
            if press_any_key=='off':
                program_done = True
                real_program_done = True
            else:
                program_done=True
        elif coffee_order=='refill':
            refill_inventory(resources)
        else:
            input("\nSorry! I don't know that")
            program_done = True
clearConsole()
input('Thank you for using the machine! Good-bye! ')
clearConsole()