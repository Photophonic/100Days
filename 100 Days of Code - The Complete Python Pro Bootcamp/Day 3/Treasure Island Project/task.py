print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
play_again = 'Y'
while play_again == 'Y':

    game_over = False
    while not game_over:
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")

        print ("You arrive at a fork in the road. Which direction would you like to go?")
        first_choice = input("Go left or right? ")

        if first_choice == "right":
            print("You fall into a hole. Game over")
            game_over = True
            break
        elif first_choice == "left":
            print("good choice, you keep walking.")

        print("You encounter a lake what do you do? ")
        second_choice = input("swim or wait? ")

        if second_choice == "swim":
            print("You are attacked by a trout. Game over")
            game_over = True
            break
        elif second_choice == "wait":
            print("You wait it out and the trout go to sleep")

        print("You encounter a set of doors which one do you open? ")
        third_choice = input("red, blue, or green?")

        if third_choice == "red":
            print("You get a nasty sunburn. Game over")
            game_over = True
            break
        elif third_choice == "blue":
            print("You fall asleep due to the rain. Game over")
            game_over = True
            break
        elif third_choice == "green":
            print("You found the treasure. Game over")
            game_over = True
            break
        else:
            print("Sorry, you lose. Game over")
            game_over = True
            break

    play_again = input("Do you want to play again? Y/N.")

print("Thank you for playing!")