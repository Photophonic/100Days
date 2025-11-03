def format_name(first_name, last_name):
     first_name = first_name.title()
     last_name = last_name.title()
     return f'{first_name} {last_name}'


f_name = input('Enter first name: ')
l_name = input('Enter last name: ')

formatted_name = format_name(f_name, l_name)
print(formatted_name)