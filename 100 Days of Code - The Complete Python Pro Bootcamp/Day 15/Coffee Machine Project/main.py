import coffee as cf

menu = cf.MENU
resources = cf.resources

# control state of machine
is_on = True
money = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # used to exit while loop
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f'Water: {resources['water']} ml\n'
              f'Milk: {resources['milk']} ml\n'
              f'Coffee: {resources['coffee']} ml\n'
              f'Money: ${money}')
    else:
        # get resources required for selected drink
        drink = menu[choice]
        #  check if there is enough via function
        if cf.resource_amount(drink['ingredients']):
            print('Thanks')