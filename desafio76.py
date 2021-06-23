produtos = ('Arroz', 11,
            'Feijão', 8,
            'Salada', 3,
            'Macarrão', 4,
            'Óleo', 8,
            'Carne', 40,
            'Frango', 12,
            'Porco', 15)
lista = 'LISTA DE PREÇOS'
print('$' * 38)
print(f'{lista:^38}')
print('$' * 38)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>5.2f}')
print('$' * 38)
