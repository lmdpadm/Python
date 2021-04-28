'''import math
numero = int(input('Vamos descobrir o fatorial no número: '))
fatorial = math.factorial(numero)
print('O fatorial de {}! é {}.'.format(numero, fatorial))'''

numero = int(input('Vamos descobrir o fatorial do número: '))
contador = numero
fatorial = 1
print('Calculando o fatorial de {}! = '.format(numero), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
