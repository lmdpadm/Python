n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

'''nome = 'Lucas'
idade = 29
salário = 1070.7
print(f'{nome} tem {idade} anos e ganha um salário mensal de R${salário:.2f}')'''
