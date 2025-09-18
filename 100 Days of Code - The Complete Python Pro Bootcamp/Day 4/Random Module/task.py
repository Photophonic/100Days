import random
from demo_module import my_number

# will grab 13 from the module
num = random.randint(1, my_number)
print(num)

# to create a float 0 ~ 1
my_float = random.random() * 100

print(my_float)
print(round(my_float, 2))

# generates between including a ~ b numbers
random_float = random.uniform(0, my_number)
print(round(random_float,2))



coin_flip = random.randint(0,1)

if coin_flip%2:
    print("Heads")
else:
    print("Tails")