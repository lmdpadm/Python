#número = int(input('Digite um número de 0 a 9999: '))
#n = str(número)
#print('A unidade é {}.'.format(n[3]))
#print('A dezena é {}.'.format(n[2]))
#print('A centena é {}.'.format(n[1]))
#print('A milhar é {}.'.format(n[0]))

número = int(input('Digite um número entre 0 e 9999: '))
u = número // 1 % 10
print('A unidade é {}.'.format(u))
d = número // 10 % 10
print('A dezena é {}.'.format(d))
c = número // 100 % 10
print('A dezena é {}.'.format(c))
m = número // 1000 % 10
print('A milhar é {}.'.format(m))

