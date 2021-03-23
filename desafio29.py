import random
v1 = random.randint(60, 120)
v2 = print('O carro está andandno a {}Km/h.'.format(v1))
if v1 > 80:
    print('Você está andando {}kms acima do permitido, será multado em R${:.2f}.'.format(v1 - 80, (v1 - 80) * 7))
else:
    print('Você está andando a {}kms, dentro dos limites de velocidade, boa viagem!'.format(v1))
