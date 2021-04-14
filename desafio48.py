soma = 0
for impar in range(1, 501, 2):
    if impar%3 == 0:
        soma = soma + impar
print('A soma dos números ímpares e múltiplos de três entre 1 e 500 é {}:'.format(soma))


