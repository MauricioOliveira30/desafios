print('Gerador PA')
print('-='*10)
a1=int(input('Primeiro termo:'))
r=int(input('Razão:'))
termo=a1
c=1
while c<10:

    print('{}->'.format(termo),end='')
    termo += r
    c+=1
print('FIM')