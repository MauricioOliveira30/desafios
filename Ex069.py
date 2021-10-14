menorM=0
maior=0
totH=0
while True:
    print('-'*30)
    print('Cadastre uma pessoa')
    print('-'*30)
    print('-'*30)
    idade=int(input('Idade:'))
    sexo=str(input('Sexo[M/F]:')).upper().strip()[0]
    print('-'*30)
    print('-'*30)
    r=str(input('Quer continuar[S/N]:')).strip().upper()[0]
    print('-'*30)
    if r not in 'S':
        break
    if maior<18:
        maior+=1
        if menorM<20 and sexo=='F':
         menorM+=1
        if sexo=='M':
            totH+=1

print(f'Total de pessoas com mais de 18 anos:{maior}\n Ao todo temos {totH} homens cadastrados\n E temos {menorM} com menos de 20 anos')
