game_level = 10

enemies = ["Alien", "Snakes", "Bombs"]

if game_level < 5:
    new_enemies = enemies[0]
    print(new_enemies)

print(enemies)
print(new_enemies)

def create_enemies():
    if game_level < 5:
        newer_enemies = enemies[1]
        print(newer_enemies)


create_enemies()
# will not work since it is a function var.
# print(newer_enemies)

