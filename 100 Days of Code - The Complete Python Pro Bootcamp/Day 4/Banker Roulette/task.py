import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
number = random.randint(0, 4)

print (f'Who\'s paying the bil????\n'
       f'It\'s {friends[number]}!!!')

# alternate approach
print (f'Who\'s paying the bil????\n'
       f'It\'s {random.choice(friends)}!!!')
