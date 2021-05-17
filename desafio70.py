import time
print('\033[1;33m♣' * 22)
print('\033[1;31m★★★ VAMOS AS COMPRAS ★★★')
print('\033[1;33m♣\033[m' * 22)
time.sleep(1)
total = mil = 0
barato = []
pbarato = ''
while True:
    produto = str(input('PRODUTO: ')).upper().strip()
    preco = float(input('PREÇO R$ '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('CONTINUAR COMPRANDO? [S/N] ')).upper().strip()[0]
    print('~' * 27)
    total += preco
    if preco > 1000:
        mil += 1
    barato += [preco]
    if preco == min(barato):
        pbarato = produto
    if continuar == 'N':
        break
time.sleep(1)
print('COMPRAS FINALIZADAS')
print(f'O total da compra foi de R${total:.2f}')
print(f'Ao todo {mil} produtos custam mais que R$1000.00')
print(f'O produto mais barato é {pbarato} que custou R${min(barato):.2f}')
