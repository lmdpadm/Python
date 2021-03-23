#preço = float(input('O preço do produto é R$'))
#input('Se você pagar a vista, tem desconto de 10%, se pagar a prazo tem acréscimento de 10%.')
#escolha = str(input('Você pagar a vista ou a prazo?'))
#vista = 0.90
#prazo = 1.10
#print('O valor final do seu produto é R${}'.format(preço * escolha))

preço = float(input('O preço do produto é R$'))
v = preço * 0.9
p = preço * 1.10
print('Se você pagar a vista o seu produto custará R${:.2f}, se pagar a prazo custará R${:.2f}!'.format(v, p))
