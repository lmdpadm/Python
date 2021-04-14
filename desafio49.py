numero = int(input('Escolha um número e falaremos sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
