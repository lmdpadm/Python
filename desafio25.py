nome = str(input('Qual o seu nome completo? ')).strip().title()
print('O seu nome tem Pereira? {}'. format('Pereira' in nome))
print('O seu nome tem Pereira? {}'.format('pereira' in nome.lower()))