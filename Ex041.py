import datetime
ano=datetime.date.today().year
nascimento=int(input('Digite seu ano de nascimento:'))
idade=ano-nascimento
if idade<=9:
    print('Mirim')
elif idade <=14:
        print('Infantil')
elif idade<=19:
    print('Junior')
elif idade<=20:
    print('Sênior')
else:
    print('Master')
