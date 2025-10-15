# 1. Take both people's names and check for the number of
# times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the
# word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number
# and print it out.

# looping through a string
# https://www.w3schools.com/python/gloss_python_for_string.asp

# count method on a string
# https://www.w3schools.com/python/ref_string_count.asp

def calculate_love_score(name1, name2):
    names = (name1+name2).replace(' ', '').lower()
    # print(names)

    true_count = 0
    love_count = 0

    for name in names:
        for letter in "true":
            # pass in the current letter of the loop
            # into the count method and add to count
            true_count += name.count(letter)

    for name in names:
        for letter in "love":
            love_count += name.count(letter)
    # print(true_count, love_count)

    final_score = str(true_count) + str(love_count)
    print(final_score)


calculate_love_score("Angela Yu", "Jack Bauer")

