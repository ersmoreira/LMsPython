import random

num_tries = 0
number = random.randint(1, 10)
acertou = False

print('Guess a number between 1 and 10')
print(number)
while  not acertou:
    num_tries += 1
    resposta = input(f'Emter a guess # {num_tries} : ')
    if not resposta.isnumeric():
        print('Numbers only , please')
        continue
    else:
        resposta = int(resposta)
    if resposta < number:
        print('Higher')
    if resposta > number:
        print('Lower')
    acertou = resposta == number
else:
    print(f'You guessed it in {num_tries} tries')