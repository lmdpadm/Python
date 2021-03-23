distância = float(input('Quantos kilometras terá sua viagem? Kms '))
if distância <= 200:
    print('A sua viagem de {} kms custará R$ {:.2f}.'.format(distância, distância * 0.50))
else:
    print('A sua viagem de {} kms custará R$ {:.2f}.'.format(distância, distância * 0.45))
#custo = distância * 0.50 if distância <= 200 else distância * 0.45
#print('A sua viagem de {} kms custará R$ {:.2f}.'.format(distância, custo))