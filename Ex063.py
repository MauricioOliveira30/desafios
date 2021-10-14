print('-'*30)
print('Sequência de  fibbonacci')
print('-'*30)
n=int(input('Digite quantos termos você quer mostrar na sua sequência?'))
print('~'*30)
t1=0
t2=1
c=3
print('~'*30)
print('{}->{}'.format(t1, t2), end='')
while c<=n:
    t3 = t1 + t2
    print('->{}'.format(t3),end='')

