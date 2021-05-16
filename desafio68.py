import random
contador = 0
while True:
    print('\033[1;33m~\033[m' * 12)
    print('\033[1;34mPAR OU ÍMPAR\033[m')
    print('\033[1;33m~\033[m' * 12)
    pi = str(input('VOCÊ QUER PAR OU ÍMPAR? [P/I] ')).upper().strip()[0]
    suaescolha = int(input('DIGA O SEU VALOR! '))
    pcescolha = random.randint(0, 10)
    soma = suaescolha + pcescolha
    if soma % 2 == 0:
        if pi == 'P':
            print(f'Você jogou {suaescolha} e seu oponente {pcescolha}, totalizando {soma}, que é par. Você venceu! Jogue novamente...')
        elif pi == 'I':
            print(f'Você jogou {suaescolha} e seu oponente {pcescolha}, totalizando {soma}, que é par. Você perdeu!')
            break
    elif soma % 2 != 0:
        if pi == 'P':
            print(f'Você jogou {suaescolha} e seu oponente {pcescolha}, totalizando {soma}, que é ímpar. Você perdeu!')
            break
        elif pi == 'I':
            print(f'Você jogou {suaescolha} e seu oponente {pcescolha}, totalizando {soma}, que é ímpar. Você venceu! Jogue novamente...')
    contador += 1
print(f'\033[1;36mFIM DE JOGO, VOCÊ VENCEU {contador} VEZES!')
