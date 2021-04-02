import datetime
anonascimento = int(input('Qual é o seu ano de nascimento? '))
anoatual = datetime.date.today().year
if anoatual - anonascimento < 18:
    print('Ainda não está na hora de você se alistar no serviço militar, faltam {} anos.'.format(18 - (anoatual - anonascimento)))
    print('Seu alistamento será em {}.'.format(anoatual + (18 - (anoatual - anonascimento))))
elif anoatual - anonascimento == 18:
    print('Você completou 18 anos, está na hora de se alistar ao serviço militar!')
elif anoatual - anonascimento > 18:
    print('Você já ultrapassou em {} anos o prazo de alistamento do serviço militar, não é mais necessário se preocupar.'.format((anoatual - anonascimento) - 18))
    print('Seu alistamento foi em {}.'.format(anoatual - ((anoatual - anonascimento - 18))))
else:
    print('Algo deu errado, tente novamente!')
