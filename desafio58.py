import random
print('\033[1;33m-=-\033[m' * 15)
print('\033[1;31mTENTE ADIVINHAR O NÚMERO QUE IREI PENSAR :)\033[m')
print('\033[1;33m-=-\033[m' * 15)
n = ''
t = 0
sorteio = int(random.randint(0, 10))
while n != sorteio:
    n = int(input('Em qual número de 0 a 10 eu pensei? '))
    if n > sorteio:
        print('ERRROOOUU, continue tentando só que com um número menor')
    elif n < sorteio:
        print('ERRROOOUU, continue tentando só que com um número maior')
    t += 1
print('\033[1;36;41m✯✯✯✯✯ Parabéns, você acertou em {} tentativas! O número escolhido foi {} ✯✯✯✯✯\033[m'.format(t, sorteio))
