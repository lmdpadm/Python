a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Com essas medidas, é possível formarmos um triângulo ', end='')
    if a == b == c:
        print('Equilátero!')
    elif a == b or b == c or a == c:
        print('Isóceles!')
    elif a != b != c != a:
        print('Escaleno!')
#if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b and a == b == c:
#    print('Com essas medidas, é possível formarmos um triângulo equilátero!')
#elif (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b and a == b or a == c or b == c:
#    print('Com essas medidas, é possível formarmos um triângulo isóceles!')
#elif (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b and a != b != c:
#    print('Com essas medidas, é possível formarmos um triângulo escaleno!')
else:
    print('Com essas medidas não é possível formarmos um triângulo!')
