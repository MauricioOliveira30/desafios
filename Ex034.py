salário = float(input('Digite seu salário:R$'))
if salário > 1250:
    print('Seu novo salário será de R${}'.format(salário*1.1))
else:
    print('Seu novo salário será de R${} '.format(salário*1.15))
