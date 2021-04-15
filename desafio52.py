lista = []
cont = 0
primo = int(input('Vamos descobrir se o número é primo: '))
for n in range(1, primo + 1):
    if primo % n == 0:
        cont += 1
        lista += [n]
if cont == 2:
    print('O número {} é primo, pois é divisível apenas por duas bases, que são {}.'.format(primo, lista))
else:
    print('O número {} não é primo, pois é divisível apenas uma ou mais de duas bases, que são {}.'.format(primo, lista))
