soma = 0
cont = 0
print('Vamos somar apenas os números pares da listagem abaixo:')
for num in range(0, 6):
    par = int(input('Digite um número inteiro: '))
    if par % 2 == 0:
        soma += par
        cont += 1
print('Você informou {} números pares e a soma deles é de {}.'.format(cont, soma))
