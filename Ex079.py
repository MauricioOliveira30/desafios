números=[]
while True:
    n=int(input('Digite um valor:'))
    if n not in  números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar...')
    r = str(input('Quer continuar?[S/N]:')).upper()
    if r!='S':
        break
números.sort()
print('-='*30)
print(f'Você digitou os valores {números}')