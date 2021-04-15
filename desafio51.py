import time
print('Vamos estruturar uma progressão aritimética'.upper())
time.sleep(1)
termo = int(input('Qual é o primeiro termo desta PA? '))
time.sleep(0.5)
razao = int(input('Qual é a razão desta PA? '))
time.sleep(0.5)
print('Segue a progressão:')
for pa in range(termo, termo + (razao * 9) + 1, razao):
    print(pa, end=' ➟ ')
print('FIM')
