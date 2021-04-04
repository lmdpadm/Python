for c in range (0, 10):
    print('Oi')
print('FIM')

for c in range (0,6):
    print(c)
print('FIM')

for c in range (6, 0, -1):
    print(c)
print('FIM')

for c in range (0, 9, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range (1, n + 1):
    print(c)

início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(início, fim + 1, passo):
    print(c)

s = 0
for c in range (0, 10):
    n = int(input('Digite um número: '))
    s = s + n
print('A soma de todos os valores é {}.'.format(s))
