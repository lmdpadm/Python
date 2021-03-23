import random
#n = random.randint(0, 1000)
n = int(input('Digite um número qualquer: '))
if n%2 == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))