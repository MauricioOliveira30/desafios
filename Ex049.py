núm=int(input('Digite um número para ver sua tabuada:'))
print('-='*10)
for c in range(0,11):
    print('{} x {:2} = {}'.format(núm,c,núm*c))
print('-='*10)