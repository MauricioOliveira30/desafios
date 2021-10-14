peso=float(input('Qual o seu peso (Kg)?'))
altura=float(input('Qual a sua altura (m)?'))
imc=peso/(altura**2)
print('De acordo com seu imc você está {:.1f}'.format(imc))

if imc<18.5:
    print('Abaixo do Peso')
elif imc<25:
    print('Peso ideal')
elif imc<=30:
    print('Sobrepeso')
elif imc<=40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
