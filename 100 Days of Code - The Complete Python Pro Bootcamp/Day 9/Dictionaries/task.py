from pandas.core.ops import logical_op

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# access the contents of the dictionary
print(programming_dictionary["Bug"])

# Adding elements to the dictionary
programming_dictionary["Loop"] = "Execute code until terminated."

print(programming_dictionary["Loop"])

# empty dictionary
demo_dictionary = {}

# easily wipe a dictionary
# programming_dictionary = {}
print(programming_dictionary)

# edit dictionary
programming_dictionary["Bug"] = 'Poor programming on the dev.'
print(programming_dictionary["Bug"])

# loop through a dictionary
for key,value in programming_dictionary.items():
    print(f'{key}: {value}')

# alternate to get just the value
for key in programming_dictionary:
    print(programming_dictionary[key])