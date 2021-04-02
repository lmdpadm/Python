import time
print('Me diga suas notas, que lhe direi se foi aprovado:')
time.sleep(1)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('A sua média foi de {:.2f}, abaixo do mínimo de 5.00, então está R E P R O V A D O!'.format(média))
elif média >= 5 and média <= 6.9:
    print('A sua média foi de {:.2f}, não atingiu o mínimo de 7.00, então fará recuperação.'.format(média))
elif média >= 7:
    print('Parabéns, a sua média foi {:.2f}, maior do que 7.00, você está aprovado!'.format(média))
else:
    print('Algo está errado em suas notas, tente novamente!')