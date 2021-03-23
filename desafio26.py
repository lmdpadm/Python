frase = str(input('Digite uma frase: ')).strip().lower()
input('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
input('A primeira letra A, apareceu na {}ª posição.'.format(frase.find('a') + 1))
input('A última letra A, apareceu na {}ª posição.'.format(frase.rfind('a') + 1))