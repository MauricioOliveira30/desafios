print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
a1=int(input('Primeiro termo:'))
r=int(input('Razão:'))
an=a1+(10-1)*r
for c in range(a1,an+1,r):
    print('{}'.format(c),end='-> ')
print('ACABOU')
