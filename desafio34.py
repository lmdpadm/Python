salário = float(input('Qual é o seu salário? R$ '))
novosalário = salário * 1.10 if salário > 1250.00 else salário * 1.15
#if salário > 1250.00:
#    print('O seu novo salário com aumento de {}, será de R$ {:.2f}!'.format('10%', salário * 1.10))
#else:
#    print('O seu novo salário com aumento de {}, será de R$ {:.2f}!'.format('15%', salário * 1.15))
print('O seu novo salário com aumento será de R${:.2f}!'.format(novosalário))