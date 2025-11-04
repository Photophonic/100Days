import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_round():
    # print(logo)
    run_game = True
    player_cards = []
    player_score = -1
    cpu_cards = []
    cpu_score = -1

    for i in range(2):
        player_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while run_game:
        player_score = calculate_score(player_cards)
        cpu_score = calculate_score(cpu_cards)

        print(f'Player cards: {player_cards}, Player score: {player_score}')
        print(f'CPU\'s card: {cpu_cards[0]}')

        if player_score == 0 or cpu_score == 0 or player_score > 21:
            run_game = False
        else:
            player_draw = input('Draw another card? y/n ').lower()
            if player_draw == 'y':
                player_cards.append(deal_card())
            else:
                run_game = False

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(player_score, cpu_score))

while input ("Do you want to play a game of Blackjack? y/n ").lower() == 'y':
    play_round()

print('Thanks for playing!')