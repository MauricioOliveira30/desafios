distância = float(input('Digite a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
if distância<=200:
    print('E o preço da viagem será de R${:.2f}'.format(distância*0.5))
else:
    print('Eo preço da viagem será de R${:.2f}'.format(distância*0.45))
