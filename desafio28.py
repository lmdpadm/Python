import random
import time
print('-=-' * 25)
print('TENTE ADIVINHAR O NÚMERO QUE IREI PENSAR :)')
print('-=-' * 25)
número = int(input('Em qual número de 0 a 5 eu pensei? ')) #JOGADOR TENTA ADIVINHAR
sorteio = int(random.randint(0, 5)) #FAZ O COMPUTADOR PENSAR
print('PROCESSANDO...')
time.sleep(3)
if número == sorteio:
    print('Parabéns, você acertou! O número escolhido foi {}!!!'.format(sorteio))
else:
    print('Não foi desta vez, tente novamente! O número correto era {}.'.format(sorteio))