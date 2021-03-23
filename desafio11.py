l = float(input('A largura da parede é:'))
a = float(input('A altura da parede é:'))
ar = a * l
t = ar / 2
print('Sua parede tem a dimensão de {:.2f} x {:.2f}, e sua área é de {:.2f}.\nPara pintar essa parede, você precisará de {:.2f}L de tinta.'.format(a, l, ar, t))
