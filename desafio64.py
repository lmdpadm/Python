n = t = c = 0
print('\033[1;33mCÁLCULADORA\033[m\nDigite 999 para finalizar!')
n = int(input('Digite um número: '))
while n != 999:
    t += n
    c += 1
    n = int(input('Digite um número: '))
print('A soma dos {} números totaliza {}.'.format(c, t))
