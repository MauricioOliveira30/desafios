núm=int(input('Digite um número para \ncalcular seu fatorial:'))
c=núm
f=1
print('Calculando {}!='.format(núm), end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x ' if c>1 else ' = ',end='')
    f*=c
    c -= 1
print('{}'.format(f),end='')
