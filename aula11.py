'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30;m
'''

print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[1;4;7;30mOlá, Mundo!\033[m')

a = 2
b = 10
print('Os valores são \033[31m{}\033[m e \033[35m{}\033[m.'.format(a, b))

nome = 'Lucas'
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format('\033[1;33;41m', nome, '\033[m'))