tupla = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))
print(f'OS NÚMEROS ESCOLHIDOS FORAM: {tupla}')
if tupla.count(9) > 0:
    print(f'O NÚMERO NOVE APARECE {tupla.count(9)} VEZES.')
else:
    print(f'O NÚMERO NOVE NÃO APARECE.')
if tupla.count(3) > 0:
    print(f'O NÚMERO TRÊS APARECEU PELA PRIMEIRA VEZ NA {tupla.index(3) + 1}ª POSIÇÃO .')
else:
    print(f'O NÚMERO TRÊS NÃO APARECE.')
print(f'OS NÚMEROS PARES SÃO', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
