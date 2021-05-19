              #-4          -3      -2      -1
              #0           1       2       3
lanche = ('HAMBÚRGUER', 'SUCO', 'PIZZA', 'PUDIM')
print(lanche[-3])
print(lanche[1:3])
print(lanche[0:4])
print(lanche[:3])
print(lanche[-3:])
print(lanche[:-2])
print(lanche)

#TUPLAS SÃO IMUTÁVEIS
#lanche[1] = 'REFRIGERANTE'
#print(lanche[1])

for comida in lanche:
    print(f'Vamos comer {comida}?')

print(len(lanche))


for comida in lanche:
    print(f'Eu vou comer {comida}')
print('=' * 20)

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print('=' * 20)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')

print('Casseta, comemos pra caramba!')

print(sorted(lanche))   #ordem alfabética

print('=' * 20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b       #tuplas não se soman, se juntam
print(c)
print(len(c))
print(c.count(5))
print(c.index(8)) #considera a primeira ocorrência
print(c.inder(5, 2))