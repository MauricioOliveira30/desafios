s=0
cont=0
for c in range(1,7):
    núm=int(input('Digite o {}° valor:'.format(c)))
    if núm%2==0:
        s+=núm
        cont+=1
print('Os números pares são {} e a soma dos números pares é {}'.format(cont,s))
