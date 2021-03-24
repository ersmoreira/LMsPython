import random

naipes = ["Copas", "Ouros", "Espadas", "Paus"]
cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

baralho = []
for naipe in naipes:
    for carta in cartas:
        baralho.append(f'{carta} de {naipe}')
print(f'O baralho tem {len(baralho)} cartas.')

print('Dealing ...')
mao_jogador = []
while len(mao_jogador) < 5:
    carta = random.choice(baralho)
    baralho.remove(carta)
    mao_jogador.append(carta)
print(f'O baralho ainda tem {len(baralho)} cartas')
print(f'O jogador tem as seguintes cartas na mão: {mao_jogador}')