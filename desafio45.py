import random
import time
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('\033[1;33m-=-\033[m' * 8)
print('\033[1;35mVAMOS BRINCAR DE \033[36mJOKENPÔ\033[m')
print('\033[1;33m-=-\033[m' * 8)
time.sleep(1.5)
print('TRÊS')
time.sleep(1)
print('.')
time.sleep(0.9)
print('.')
time.sleep(0.8)
print('.')
time.sleep(0.7)
print('DOIS')
time.sleep(0.6)
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.4)
print('UM')
time.sleep(0.3)
print('.')
time.sleep(1)
print('JÓÓÓÓÓKEEENPÔÔÔ!!!')
time.sleep(1)
eu = input('FAÇA SUA JOGADA!!! (PEDRA, PAPEL OU TESOURA) ').lower().strip()
time.sleep(1)
oponente = random.choice(lista).lower()
print('O seu oponente escolheu {}!!!'.format(oponente))
time.sleep(1)
if eu == 'pedra' and oponente == 'pedra':
    print('\033[1;35mHouve um empate, pedra com pedra, vira pedra rachada! Joguem novamente!\033[m')
elif eu == 'pedra' and oponente == 'papel':
    print('\033[1;35mVocê perdeu, o seu oponente embalou a sua pedra com o papel dele!\033[m')
elif eu == 'pedra' and oponente == 'tesoura':
    print('\033[1;35mVocê venceu, a sua pedra entortou a tesoura de seu oponente!\033[m')
elif eu == 'papel' and oponente == 'pedra':
    print('\033[1;35mVocê venceu, o seu papel embalou a pedra do seu oponente!\033[m')
elif eu == 'papel' and oponente == 'papel':
    print('\033[1;35mHouve um empate, papel com papel não vira nada... Joguem novamente!\033[m')
elif eu == 'papel' and oponente == 'tesoura':
    print('\033[1;35mVocê perdeu, a tesoura do seu oponente te detonou!\033[m')
elif eu == 'tesoura' and oponente == 'pedra':
    print('\033[1;35mVocê perdeu, a pedra do seu oponente detonou a sua tesoura!\033[m')
elif eu == 'tesoura' and oponente == 'papel':
    print('\033[1;35mVocê venceu, a sua tesoura picotou o papel do seu oponente!\033[m')
elif eu == 'tesoura' and oponente == 'tesoura':
    print('\033[1;35mHouve um empate, duas tesouras não viram nada... Joguem novamente!\033[m')
else:
    print('Algo deu errado, joguem novamente!')