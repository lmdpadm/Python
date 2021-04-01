casa = float(input('Qual o valor da casa desejada? R$ '))
salário = float(input('Qual é o seu salário mensal? R$ '))
prazo = int(input('Em quantos anos você quer financiar a casa? '))
finaciamentoaprovado = float(salário * 0.30)
prestação = casa / (prazo * 12)
if prestação <= finaciamentoaprovado:
    print('O seu financiamento com parcelas de R${:.2f}, foi aprovado! Pois corresponde a {:.2f}% do seu salário, menos do que os 30% permitidos.'.format(prestação, (prestação / salário) * 100))
else:
    print('O seu financiamento não foi aprovado, pois as parcelas de R${:.2f}, correspondem a mais de 30% do seu salário de R${:.2f}.'.format(prestação, salário))
