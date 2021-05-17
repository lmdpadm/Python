cad = 'CADASTRE-SE'
maiordezoito = 0
homens = 0
mulheresmenor = 0
while True:
    print('\033[1;31m%\033[m' * 24)
    print(f'{cad:^24}')
    print('\033[1;31m%\033[m' * 24)
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]
    print('-' * 24)
    escolha = ' '
    while escolha not in "SN":
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        maiordezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenor += 1
    if escolha == 'N':
        break
print('-' * 24)
print(f'''Ao todo temos {maiordezoito} pessoas com mais de 18 anos.
Foram {homens} homens cadastrados.
Temos {mulheresmenor} mulheres com menos de 20 anos.''')
