número = int(input('Escolha um número inteiro qualquer: '))
opção = int(input('Escolha uma das bases para conversão:\n[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL\nSua escolha: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(número, hex(número)[2:]))
else:
    print('Opção inexistente, escolha entre as opções 1, 2 ou 3.')