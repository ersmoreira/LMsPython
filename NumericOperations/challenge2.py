
first_number = input('First Number: ')
if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()
else:
    first_number = int(first_number)

second_number = input('Second Number: ')
if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()
else:
    second_number = int(second_number)

operator = input('Operation: ')
if operator == '+':
    label = 'Sum'
    res = first_number + second_number
elif operator == '-':
    label = 'Difference'
    res = first_number - second_number
elif operator == '*':
    label = 'Product'
    res = first_number * second_number
elif operator == '/':
    label = 'Quotient'
    res = first_number / second_number
elif operator == '%':
    label = 'Module'
    res = first_number % second_number
elif operator == '^':
    label = 'Exponent'
    res = first_number ^ second_number 
else:
    print('Operation not recognized.')
    exit()

resultado = f'{label} of {first_number} and {second_number} is {res}'
print(resultado)