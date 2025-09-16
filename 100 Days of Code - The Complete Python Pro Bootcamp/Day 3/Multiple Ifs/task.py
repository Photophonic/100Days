print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        total = 5
    elif age <= 18:
        print("Please pay $7.")
        total = 7
    else:
        print("Please pay $12.")
        total = 12

    wants_photo = input('Do you want a photo? (y/n): ')
    if wants_photo == 'y':
        print("That will be an additional $3")
        total += 3
    else:
        print("Thank you!")

    print(f"Your total is ${total}")

else:
    print("Sorry you have to grow taller before you can ride.")
