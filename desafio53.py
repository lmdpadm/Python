frase = input('Vamos verificar se sua frase é um palíndromo. Digite a frase: ')
frasefinal = frase.upper().replace(' ', '').strip()
palindromo = frase[::-1].upper().replace(' ', '').strip()
if frasefinal == palindromo:
    print('A frase {} é um palíndromo!'.format(frase.strip()))
else:
    print('A frase {} não é um palíndromo!'.format(frase.strip()))
