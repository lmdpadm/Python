print('Vamos estruturar uma progressão aritimética'.upper())
termo = int(input('Qual é o primeiro termo desta PA? '))
razao = int(input('Qual é a razão desta PA? '))
termo1 = termo
total = 0
mais = 10
tempo = 1
print('Segue a progressão:')
while mais != 0:
    total += mais
    while tempo <= total:
        print('{} ➟ '.format(termo1), end=' ')
        tempo += 1
        termo1 += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver mais? '))
print('FIM, o total de termos pesquisados foi {}.'.format(total))
