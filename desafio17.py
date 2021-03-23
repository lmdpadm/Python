from math import hypot
catetooposto = float(input('O comprimento do cateto oposto é: '))
catetoadjacente = float(input('O comprimento do cateto adjacente é: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
#hipotenusa = (catetooposto ** 2 + catetoadjacente ** 2) ** (1/2)
print('Um triângulo retângulo com cateto oposto de {:.2f} e cateto adjacente de {:.2f}, tem a hipotenusa de {:.2f}.'.format(catetooposto, catetoadjacente, hipotenusa))