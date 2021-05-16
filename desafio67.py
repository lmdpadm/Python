print('\033[1;33m~\033[m' * 39)
print('\033[1;35mCÁLCULADORA DE TABUADA\033[m')
print('digite um número negativo para desligar')
print('\033[1;33m~\033[m' * 39)
while True:
    tabuada = int(input('\033[1;34mDESEJA SABER A TABUADA DE QUAL VALOR?\033[m '))
    if tabuada < 0:
        break
    for c in range (1, 11):
        print(f'{tabuada} X {c} = {tabuada * c} ')
print('\033[1;36mCÁLCULADORA DE TABUADA DESLIGADA')
