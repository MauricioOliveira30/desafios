ano = int(input('Em ano você está?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é BISSEXTO')
else:
    print('Esse ano não é BISSEXTO')
