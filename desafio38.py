import time
print('Escolha dois números:')
time.sleep(1)
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor {} é o maior!'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é o maior!'.format(n2))
elif n2 == n1:
    print('Não existe valor maior, ambos são iguais!')
else:
    print('Algo deu errado, tente novamente!')
