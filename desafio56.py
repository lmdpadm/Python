ihomem = 0
nhomem = ''
qtdmulher = 0
lista = []
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = [int(input('Idade: '))]
    sexo = str(input('Sexo [M/F]: ')).upper()
    lista += idade
    if sexo == 'M':
        ihomem = max(idade)
    if sexo == 'M' and idade < [999]:
        nhomem = nome
    if sexo == 'F' and idade < [20]:
        qtdmulher += 1
print('A média de idade do grupo é de {:.2f} anos de vida.'.format(sum(lista) / len(lista)))
print('O homem mais velho tem {} anos e se chama {}.'.format(ihomem, nhomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qtdmulher))
