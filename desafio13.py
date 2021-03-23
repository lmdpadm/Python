salário = float(input('O salário de Lucas é R$'))
aumento = float(input('Qual o percentual de aumento? %'))
ns = salário * (1 + (aumento/100))
input('O novo salário de Lucas com aumento de {:.2f}%, será de R${:.2f}'.format(aumento, ns))


