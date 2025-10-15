from turtledemo.clock import current_day


def myfunction(v_name):
    print(f'Hello {v_name}')


names = ['Bob','John','Jack']
for name in names:
    myfunction(name)



def life_in_weeks(age):
    total_weeks = 90 * 52
    current_weeks = age * 52
    weeks = total_weeks - current_weeks
    print(f'You have {weeks} weeks left.')


life_in_weeks(45)


def greet_with(v_name, v_location):
    print(f'Hello {v_name}, you are in {v_location}.')

names = ['Bob','John','Jack']
locations = ['Washington', 'Dallas', 'New York']

# The zip() function returns a zip object, which is an iterator
# of tuples where the first item in each passed iterator is
# paired together, and then the second item in each passed
# iterator are paired together etc.
for name, location in zip(names, locations):
    greet_with(v_name = name, v_location=location)


