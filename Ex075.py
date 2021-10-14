números=(int(input('Digite um número:')),
int(input('Digite um número:')),
int(input('Digite um número:')),
int(input('Digite um número:')),
int(input('Digite um número:')))
print(f'Você digitou os valores {números}')
print(f'O valor 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O valor 3 apareceu na  {números.index(3)+1}ª posição')
else:
    print('O valor 3 não aparece em nenhuma posição da tupla')
print(f'Os valores pares digitados foram ',end=' ')
for núm in números:
    if núm%2==0:
        print(núm,end=' ')
