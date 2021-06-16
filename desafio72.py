tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', \
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        n = int(input('Digite um número entre 0 e 20: '))
        while n not in range(0, 21):
                n = int(input('Opção inválida, escolha um número entre 0 e 20: '))
        print(f'Você digitou o número {tupla[n]}.')
        c = str(input('Você quer continuar? [S/N] ')).upper().strip()
        while c not in 'SN':
                c = str(input('Opção inválida, escolha entre [S/N]')).upper().strip()
        if c == 'N':
                break
print('Obrigado por participar!')
