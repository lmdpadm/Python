import datetime
soma = 0
ano = datetime.date.today().year
for idade in range(1, 8):
    nascimento = int(input('Digite o ano do nascimento da {}ª pessoa: '.format(idade)))
    if ano - nascimento < 21:
        soma += 1
print('Ao todos temos {} pessoas que não atingiram a maioridade e {} que já atingiram.'.format(soma, 7 - soma))
