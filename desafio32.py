import datetime
#import random
#a = random.randint(0, 2021)
#input('O ano é {}.'.format(a))
a = int(input('Qual ano você quer análisar? Coloque zero para análisar o ano atual: '))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} não é um ano bissexto!'.format(a))