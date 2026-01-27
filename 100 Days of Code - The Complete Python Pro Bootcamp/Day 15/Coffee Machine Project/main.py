from traceback import print_tb

import coffee as cf

menu = cf.MENU
resources = cf.resources

# control state of machine
is_on = True
profit = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # used to exit while loop
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f'Water: {resources['water']} ml\n'
              f'Milk: {resources['milk']} ml\n'
              f'Coffee: {resources['coffee']} ml\n'
              f'Money: ${profit}')
    else:
        # get resources required for selected drink
        drink = menu[choice]
        print(drink)
        print(choice)
        #  check if there is enough via function
        if cf.resource_amount(drink['ingredients']):
            payment = cf.process_coins()
            while payment < drink['cost']:
                print(f"{payment}. Please add more coins")
                add_coins = input("Would you like to add more coins? (yes/no): ")
                if add_coins == "no":
                    print(f"Your payment of {payment} has been refunded refunded.")
                    exit()
                else:
                    payment += cf.process_coins()
            print(f'You payed: {payment}')

            change_owed = round(payment - drink['cost'],2)
            print(f'Your change is {change_owed}.')
            profit += drink['cost']

            cf.make_drink(drink['ingredients'])
            print(f"{choice} is now available.")
