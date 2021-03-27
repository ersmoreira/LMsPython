def create_deck():
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = []

    for naipe in naipes:
        for carta in cartas:
            baralho.append(f'{carta} de {naipe}')

    return baralho
