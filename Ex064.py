c=0
s=0
n=0
while n!=999:
    n=int(input('Digite um número[999 para parar]: '))
    if n!=999:
     c += 1
     s+=n

print('Você digitou {} e a soma entre eles é {}'.format(c,s))