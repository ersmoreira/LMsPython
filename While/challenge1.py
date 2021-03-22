import random

num = random.randint(1, 5)
certo = False
ntries = 0
print(num)


while certo != True:
    resposta = input('Guess a number between 1 and 5: ')
    ntries += 1
    certo = str(resposta) == str(num)

print(f'You guessed it in {ntries} tries!')