#nome = input('Qual é o seu nome?')
#print('Prazer, o meu nome é {:<20}!'.format(nome))
#print('Prazer, o meu nome é {:^20}!'.format(nome))
#print('Prazer, o meu nome é {:>20}!'.format(nome))
#print('Prazer, o meu nome é {:=^20}!'.format(nome))

#n1 = int(input('Um valor:'))
#n2 = int(input('Outro valor:'))
#print('A soma vale {}.'.format(n1+n2))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, multiplicação é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão é {} e a potência é {}'.format(di, e))