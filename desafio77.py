tupla = ('LUCAS', 'MATHEUS', 'DIAS', 'PEREIRA')
vogais = ('A', 'E', 'I', 'O', 'U')
for palavras in tupla:
        print(f'\nNa palavra {palavras.upper()}, existem as vogais', end=' ')
        for letra in palavras:
            if letra.upper() in 'AEIOU':
                print(letra, end=' ')
