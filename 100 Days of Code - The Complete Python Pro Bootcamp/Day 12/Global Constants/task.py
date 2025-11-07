def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


"""
To check if a number n is prime, first see if it's less than 2 
if so, it's not prime. Otherwise, try dividing n by every number 
from 2 to n - 1. If any number divides it evenly, 
then n is not prime. If none do, then n is a prime number.
"""


n = 8

print(is_prime(n))


enemies = 1

def increase_enemies(enemy):
    # global enemies
    enemy += 1
    # print(enemies)
    return enemy

enemies = increase_enemies(enemies)
print(enemies)

# creating global constant, make them uppercase
PI = 3.14159
GOOGLE_URL = "https://www.google.com"



