valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for v in valores:
    print(f'{v} ', end='')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista')