lista = []
for var in range(1, 6):
    peso = [int(input('Qual é o peso da {}ª pessoa? Kg '.format(var)))]
    lista += peso
print('O maior peso é de {}Kg e o menor é de {}Kg.'.format(max(lista), min(lista)))
