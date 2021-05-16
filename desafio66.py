total = cont = 0
print('Vamos somar valores. Digite 999 para interromper!')
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    total += numero
    cont += 1
print(f'A soma total dos {cont} números é de {total}.')
