import datetime

ano = datetime.date.today().year
nascimento = int(input('Digite seu ano de nascimento:'))
idade = ano - nascimento
falta=18-idade
passou=idade-18
alistamento_maior=ano-passou
alistamento_menor=falta+ano
if idade==18:
    print('Você que nasceu  em {} tem {} anos \nEstá na hora de você se alistar'.format(nascimento,idade))
elif idade<18:
    print('Você que nasceu em {} tem {} anos \nAinda faltam {} anos para você alistar\nSeu alistamento será em {} '.format(nascimento,idade,falta,alistamento_menor))
else:
    print('Você que nasceu em {} tem {} anos\nVocê já deveria ter se alistado há {} anos\nSeu alistamento foi em {}'.format(nascimento,idade,passou,alistamento_maior))