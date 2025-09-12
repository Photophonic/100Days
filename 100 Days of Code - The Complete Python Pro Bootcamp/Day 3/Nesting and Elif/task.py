print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("Enter your age: "))


if height >= 120:
    print("You can ride the rollercoaster")
    if age > 18:
        print("Ticket price is $12")
    elif age >= 12 and age <= 18:
        print("Ticket price is $8")
    else:
        print("Ticket price is $5")
else:
    print("Sorry you have to grow taller before you can ride.")


