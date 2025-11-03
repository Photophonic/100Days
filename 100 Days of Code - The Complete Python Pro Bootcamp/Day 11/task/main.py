import random

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

def compare(player_score, cpu_score):
    print(player_score, cpu_score)

from art import logo

# print(logo)
run_game = True

player_cards = []
player_score = 0

cpu_cards = []
cpu_score = 0

for i in range(2):
    player_cards.append(deal_card())
    cpu_cards.append(deal_card())



while run_game:
    player_score = calculate_score(player_cards)
    cpu_score = calculate_score(cpu_cards)

    print(f'Player cards: {player_cards}, Player score: {player_score}')
    print(f'CPU\'s card: {cpu_cards[0]}, CPU\'s score: {cpu_score}\n')

    if cpu_score == 0:
        print('Blackjack!, CPU Wins')
        print(f'CPU cards: {cpu_cards[0]}, CPU score: {cpu_score}\n')

    elif player_score == 0:
        print('Blackjack!, Player Wins')
        run_game = False
        break
    elif player_score > 21:
        print('Bust, CPU Wins')
        print(f'CPU cards: {cpu_cards[0]}, CPU score: {cpu_score}\n')
        run_game = False
        break

    player_draw = input('Draw another card? y/n ')
    if player_draw == 'y':
        player_cards.append(deal_card())

    if cpu_score <17:
        cpu_cards.append(deal_card())

print('Thanks for playing!')