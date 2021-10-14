maispesado=0
maisleve=0
for p in range(1,6):
    peso=float(input('Peso da {}ª pessoa:'.format(p)))
    if p==1:
        maispesado=peso
        maisleve=peso
else:
    if peso<maisleve:
        maisleve=peso

if maispesado>peso:
    maispesado=peso
print('O mais pesado é {} e o mais leve é {}'.format(maispesado,maisleve))