import time
print('\033[1;33m=-=\033[m' * 9)
print('\033[1;32m Vamos cálcular o seu IMC\033[m')
print('\033[1;33m=-=\033[m' * 9)
time.sleep(1.5)
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Você está abaixo do peso com IMC de {:.2f}. Cuide-se!'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no peso ideal com um IMC de {:.2f}. Parabéns!'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso e um IMC de {:.2f}. Comece a se alimentar melhor!'.format(imc))
elif 30 <= imc < 40:
    print('Você está obeso com um IMC de {:.2f}. Se alimente melhor e faça exercícios regularmente!'.format(imc))
elif imc >= 40:
    print('Você está em obesidade mórbida com um IMC de {:.2f}. Procure ajuda médica urgentemente!'.format(imc))
else:
    print('Algo está errado, tente novamente!')