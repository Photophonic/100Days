# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

not_tall = True

while not_tall:
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    if height >= 120:
        print("Enjoy the ride")
        not_tall = False
    else:
        print("Try again")

