s=0
maisvelhoh=0
nomevelhoh=''
menor=0
menores=0
for p in range (1,5):
    print('--------{}ªPessoa-----------'.format(p))
    nome=str(input('Nome:')).strip()
    idade=int(input('Idade:'))
    Sexo=str(input('Sexo[M/F]:')).strip()
    if p==1 and Sexo in 'Mm':
        maisvelhoh=idade
        nomevelhoh=nome
    else:
        if maisvelhoh>idade  and Sexo=='M':
            maisvelhoh=idade
            nomevelhoh=nome
    if idade<20 and Sexo in 'Ff':
        menor+=1

    s+=idade
m=s/p
print('A média foi de {} anos\nO homem mais velho tem {} anos e se chama {}\nA quantidade de mulheres menores de 20 anos é {} '.format(m,maisvelhoh,nomevelhoh,menor))
