s = ''
while s != 'M' and s != 'F': #PODE SER UTILIZADO - WHILE S NOT IN 'MmFf'
    s = str(input('Diga o seu sexo: [M/F] ')).upper().strip()[0] #FATIAMENTO DA PRIMEIRA LETRA
    if s != 'M' and s != 'F':
        print('Você digitou o sexo errado, digite novamente!')
print('Sexo {} registrado!'.format(s))
