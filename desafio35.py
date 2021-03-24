#import random
#a = random.randint(1, 10)
#b = random.randint(1, 10)
#c = random.randint(1, 10)
#print('O lado A corresponde a {} cm.'.format(a))
#print('O lado B corresponde a {} cm.'.format(b))
#print('O lado C corresponde a {} cm.'.format(c))
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Com essas medidas, é possível formarmos um triângulo.')
else:
    print('Com os essas medidas, não é possível formarmos um triângulo.')
