nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':                                                             #condição simples
    print('Que nome bonito!')                                                   #condição simples
elif nome == 'Mariana' or nome == 'Pedro' or nome == 'Julio':                   #estrutura condicional aninhada
    print('O seu nome é bem popular no Brasil!')                                #estrutura condicional aninhada
elif nome == 'Ronaldo' or nome == 'Romário' or nome == 'Cristiano':             #estrutura condicional aninhada
    print('Você tem nome de craque de futebol!')                                #estrutura condicional aninhada
else:                                                                           #estrutura condicional composta
    print('O seu nome é bem normal...')                                         #estrutura condicional composta
print('Tenha um bom dia, {}!'.format(nome))