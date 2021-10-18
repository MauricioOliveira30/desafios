lista=[]
pares=[]
ímpares=[]
while True:
    lista.append(int(input('Digite o valor:')))
    r=str(input('Quer continuar[S/N]:'))
    if r not in 'Ss':
        break
for i,v in enumerate(lista):
    if v%2==0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f'A lista completa é {lista}')
print(f'A lista dos pares é {pares}')
print(f'A lista dos ímpares é {ímpares}')