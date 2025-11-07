import random

def play_round(player_difficulty):
    run_game = True
    num_of_guesses = 0
    mystery_number = random.randint(1, 10)
    player_guess = 0

    if player_difficulty == 'easy':
        num_of_guesses = 10
    elif player_difficulty == 'hard':
        num_of_guesses = 5
    else:
        print('Invalid difficulty')

    while run_game:
        while num_of_guesses > 0 and run_game:
            print(f"Guesses left: {num_of_guesses}")
            player_guess = int(input("Guess your number: "))

            if player_guess == mystery_number:
                print(f"Congratulations, you guessed my number {mystery_number}!")
                run_game = False
            elif player_guess < mystery_number:
                print("Your guess is too low.")
                num_of_guesses -= 1
            elif player_guess > mystery_number:
                print("Your guess is too high.")
                num_of_guesses -= 1

            if num_of_guesses == 0:
                run_game = False
                print(f"Sorry, my number was {mystery_number}!")


print("Welcome to Number Guessing Project\n"
      "I'm thinking of a number between 1 and 100\n")
difficulty = input("Choose a difficulty, easy or hard: ")
play_round(difficulty)

print("test end???")