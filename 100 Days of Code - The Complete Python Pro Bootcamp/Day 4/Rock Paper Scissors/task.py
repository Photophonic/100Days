import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = [rock, paper, scissors]

my_choice = int(input('What do you choose? Type 0 for "Rock", '
                   '1 for "Paper" or 2 for "Scissors"\n'))
pc_choice = random.randint(0, len(choices)-1)


print(f'You selected:\n'
      f'{choices[my_choice]}\n')

print(f'Computer selected:\n'
      f'{choices[pc_choice]}\n')

if my_choice == 0 and pc_choice == 2:
    print('You Win!')
elif pc_choice == 0 and my_choice == 2:
    print('You Lose!')
elif pc_choice > my_choice:
    print('You Lose!')
elif my_choice > pc_choice:
    print('You Win!')
elif pc_choice == my_choice:
    print('Draw.')
else:
    print('Try again.')

