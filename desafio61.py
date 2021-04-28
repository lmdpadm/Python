tempo = 1
print('Vamos estruturar uma progressão aritimética'.upper())
termo = int(input('Qual é o primeiro termo desta PA? '))
razao = int(input('Qual é a razão desta PA? '))
termo1 = termo
print('Segue a progressão:')
while tempo <= 10:
    print('{} ➟ '.format(termo1), end=' ')
    tempo += 1
    termo1 += razao
print('FIM')
