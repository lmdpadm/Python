n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro: '))
n3 = int(input('O último: '))

#Encontrando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

#Encontrando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('O maior número é {} e o menor é {}!'.format(maior, menor))