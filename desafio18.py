import math
ângulo = float(input('O ângulo a ser cálculado é: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('Em um ângulo de {} graus, o seno é {:.2f}, cosseno {:.2f} e a tangente é de {:.2f}.'.format(ângulo, seno, cosseno, tangente))

