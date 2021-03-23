from random import choice
'''input('Um aluno será sorteado para apagar o quadro negro, segue os selecionados: \nLucas \nMariana \nJulio \nJuliana')
sorteio = random.choice(['o Lucas', 'a Mariana', 'o Julio', 'a Juliana'])
print('O aluno sorteado foi {}!'.format(sorteio))'''

n1 = str(input('O primeiro aluno:'))
n2 = str(input('O segundo aluno:'))
n3 = str(input('O terceiro aluno:'))
n4 = str(input('O quarto aluno:'))
lista = [n1, n2, n3, n4]
print('O aluno sorteado foi {}!'.format(choice(lista)))



