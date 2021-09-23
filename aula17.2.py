'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

a = [2, 3, 4, 7]
#b = a
#b[2] = "pizza"  # O Python cria uma conexão entre uma lista e outra, as substituições se igualam
b = a[:]    # Crie uma cópia da lista utilizando fatiamento
b[2] = "pizza"
print(f'Lista A: {a}')
print(f'Lista B: {b}')

