import random
from art import logo, vs
from game_data import data
import data_comp as comp

# Keep game going while true
play = True
score = 0
# random.choice will select from the list at proper length
first_choice = random.choice(data)
# print(first_choice)

while play:
    print(logo)
    # select second choice.
    second_choice = random.choice(data)
    # In the event both are the same, select again
    while second_choice == first_choice:
        second_choice = random.choice(data)

    # print values from the selected lists
    print(f"Compare A:{comp.format_data(first_choice)}")
    # print(f"{vs}\n")
    print(f"Compare B:{comp.format_data(second_choice)}")
    selection = input("\nWho has more followers? Type 'A' or 'B':").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)


    higher_followers = comp.compare(first_choice['follower_count'],
                                    second_choice['follower_count'])

    if selection == higher_followers:
        # increment score
        score += 1
        print(f"Correct, current score is {score}.")
        # swap
        first_choice = second_choice
    else:
        print(f"Game over, final score was {score}.")
        play = False


