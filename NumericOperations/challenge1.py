fahrenheit = input('What is the temperature in fahrenheit? ')

if not fahrenheit.isnumeric():
    print('Input is not a number')
    exit()

fahrenheit = int(fahrenheit)
celsius = int((fahrenheit-32) * 5 / 9)

print(f'Temperature in celsius is {celsius}')