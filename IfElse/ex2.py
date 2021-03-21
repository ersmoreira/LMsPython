#print(type("Hello World!"))
#print(type(7))
#print(type(True))
#print(type(False))
#print(type('True'))
#print(type('False'))

#print(bool('True'))
#print(bool('False'))
#print(bool(''))
#print(bool(' '))
#print(bool('Hello World'))

#print(bool(7))
#print(bool(1))
#print(bool(0))
#print(bool(-1))

#print(1 + 1 == 2)
#print(1 + 1 == 3)


first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('O valor está entre 1 e 10')

if first_number > 1 or second_number > 1:
    print('Pelo menos 1 valor é maior do que 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Ambos os valores passaram o teste')
else:
    print('Ambos os valores falharam o teste')