'''nome = str(input('Qual é o seu nome? '))
if nome == 'Mariana':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primera nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi de {:.2f}!'.format(m))
if m >= 6.0:
    print('Parabéns, ótima média {}'.format(m))
else:
    print('Você precisa melhorar, estude mais...')
#print('PARABÉNS' if m >= 6 else 'Estude mais!')