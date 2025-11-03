# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))
from tenacity import retry_unless_exception_type


def format_name(first_name, last_name):
    if first_name =="" or last_name =="":
        return "enter both first and last name"

    first_name = first_name.title()
    last_name = last_name.title()
    return f'{first_name} {last_name}'


f_name = input('Enter first name: ')
l_name = input('Enter last name: ')

formatted_name = format_name(f_name, l_name)
print(formatted_name)


def age_checker(age):
    if age >= 18:
        return True
    else:
        return False

age_check = int(input('Enter age: '))
of_age = age_checker(age_check)

if of_age:
    print("enjoy the show")
else:
    print("you are not old enough for the show")


def is_leap(year):
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                # Divisible by 400, it is a leap year
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(add(2, multiply(5, divide(8, 4))))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))