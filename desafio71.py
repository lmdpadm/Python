print('\033[1;32m$' * 24)
print('\033[m{:^24}'.format('BANCO LUMA'))
print('\033[1;32m$\033[m' * 24)
valor = int(input('VALOR DO SAQUE R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'TOTAL DE {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('\033[1;32m$\033[m' * 24)
print('OBRIGADO E VOLTE SEMPRE!')
