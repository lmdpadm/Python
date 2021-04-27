n = 0
p = float(input('Digite o primeiro número: '))
s = float(input('Digite o segundo número: '))
while n != 5:
    n = int(input('Como deseja calcular estes números?\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n '))
    if n == 1:
        print('A soma entre {:.2f} e {:.2f} totaliza {:.2f}. Participe novamente!'.format(p, s, p + s))
    elif n == 2:
        print('A multiplicação entre {:.2f} e {:.2f} totaliza {:.2f}. Participe novamente!'.format(p, s, p * s))
    elif n == 3:
        print('O maior número {}.'.format(max(p, s)))
    elif n == 4:
        print('Informe os valores novamente: ')
        p = float(input('Digite o primeiro valor: '))
        s = float(input('Digite o segundo valor: '))
    elif n == 5:
        print('Obrigado por participar!')
    else:
        print('Opção inválida, tente novamente!')
print('Fim!')
