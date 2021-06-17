from random import randint
tupla = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print(f'OS VALORES SORTEADOS FORAM ', end='')
for n in tupla:
    print(f'{n}', end=' ')
print(f'\nO MAIOR NÚMERO DA TUPLA É {max(tupla)}')
print(f'O MENOR NÚMERO DA TUPLA É {min(tupla)}')
