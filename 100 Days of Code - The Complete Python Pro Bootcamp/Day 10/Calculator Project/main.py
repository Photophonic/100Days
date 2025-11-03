from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(first_number, operand, second_number):
    if operand == "+":
        result = add(first_number, second_number)
    elif operand == "-":
        result = subtract(first_number, second_number)
    elif operand == "*":
        result = multiply(first_number, second_number)
    elif operand == "/":
        result = divide(first_number, second_number)
    return result

print(logo)
continue_calc = 'n'
my_result = 0

while True:

    if continue_calc == 'y':
        first_number = my_result
    else:
        first_number = int(input("What is your first number?  "))
    print('+\n-\n*\n/\n')
    operand = input("What operation do you want to perform?  ")
    second_number = int(input("What is your second number?  "))

    my_result = calculator(first_number, operand, second_number)

    print(f"{first_number} {operand} {second_number} = {my_result}")

    continue_calc = input(f"Type 'y' to continue calulating with {my_result} "
                          f"or 'n' to start a new calculation,"
                          f"or 'q' to quit. ")

    if continue_calc == 'q':
        break

print('Thanks for mathing.')



