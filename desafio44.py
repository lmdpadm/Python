import time
print('{:=^50}'.format('\033[1;36m LUMA STORE\033[m '))
preço = float(input('Prezado cliente, o valor de sua compra é de \033[1;32mR$\033[m '))
time.sleep(1)
print('\033[1;4mSegue as formas de pagamento disponíveis:\033[m')
time.sleep(1.5)
print('\033[1;31m[ 1 ] - Dinheiro ou cheque te daremos 10% de desconto!')
time.sleep(1)
print('\033[1;32m[ 2 ] - À vista no cartão te daremos 5% de desconto!')
time.sleep(1)
print('\033[1;33m[ 3 ] - Em até duas vezes no cartão conseguimos manter o preço à vista!')
time.sleep(1)
print('\033[1;34m[ 4 ] - Em três ou mais vezes no cartão haverá 20% de juros!\033[m')
time.sleep(1)
pagamento = int(input('Qual será a forma de pagamento? '))
um = preço * 0.9
dois = preço * 0.95
três = preço
quatro = preço * 1.2
time.sleep(1.5)
if pagamento == 1:
    print('A compra de R${:.2f}, com pagamento em dinheiro ou cheque, ficará em R${:.2f}. Muito obrigado e volte sempre!'.format(preço, um))
elif pagamento == 2:
    print('A compra de R${:.2f}, com pagamento no cartão à vista, ficará em R${:.2f}. Muito obrigado e volte sempre!'.format(preço, dois))
elif pagamento == 3:
    print('A compra de R${:.2f}, com pagamento em duas vezes no cartão se manterá em {:.2f}, serão duas parcelas de R${:.2f}. Muito obrigado e volte sempre!'.format(preço, três, preço / 2))
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('A compra de R${:.2f}, com pagamento em {} parcelas no cartão, ficará em R${:.2f}, sendo cada parcela no valor de R${:.2f}. Muito obrigado e volte sempre!'.format(preço, parcelas, quatro, quatro / parcelas))
else:
    print('Você escolheu a opção errada, recomece o processo. Obrigado!')
time.sleep(2)
print('\033[1;36m--- Luma Store agradece a sua compra! ---\033[m')
