valores=list()
while True:
    v=int(input('Digite um valor:'))
    r=str(input('Quer continuar?[S/N]:'))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!Não vou adicionar')
        if r in'Nn':
            break
print('-='*30)
print(valores.sort())
print(valores)


