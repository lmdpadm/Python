n = cont = 0
nu = lista = []
c = ''
while n < 10 and c != "N":
    n += 1
    nu = [int(input('Digite um número: '))]
    c = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    lista += nu
    cont += 1
print('~'*45)
print('Você digitou {} números!'.format(cont))
print('A média de todos esses números é {:.2f}'.format(sum(lista) / len(lista)))
print('O maior é {} e o menor é {}.'.format(max(lista), min(lista)))
print('~'*45)