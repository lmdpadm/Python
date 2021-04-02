import datetime
ano = int(input('Qual é o seu ano de nascimento? '))
anoatual = datetime.date.today().year
idade = anoatual - ano
if idade > 0 and idade <= 9:
    print('Você está com {} anos, então se enquadra na categoria MIRIM.'.format(anoatual - ano))
elif idade <= 14:
    print('Você está com {} anos, então se enquadra na categoria INFANTIL.'.format(anoatual - ano))
elif idade <= 19:
    print('Você está com {} anos, então se enquadra na categoria JUNIOR.'.format(anoatual - ano))
elif idade <= 20:
    print('Você está com {} anos, então se enquadra na categoria SÊNIOR.'.format(anoatual - ano))
elif idade > 20:
    print('Você está com {} anos, então se enquadra na categoria MASTER.'.format(anoatual - ano))
else:
    print('Algo está errado, tente novamente!')
