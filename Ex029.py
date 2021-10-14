vel = float(input('Qual a sua  velocidade atual do carro?'))
if vel > 80:
    multa = (vel-80)*7
    print('Você pagará de multa R${}'.format(multa))
else:
    print('Tenha um bom dia!  Dirija com segurança!')

