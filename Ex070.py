print('-'*30)
print('SUPER BARATÃO')
print('-'*30)
tot=mais_mil=maisbarato=cont=0
produto_maisbarato=''
while True:
    nome=str(input('Nome do produto:'))
    preço=float(input('Preço:R$'))
    tot+=preço
    if preço>1000:
        mais_mil+=1
        if cont==1:
            maisbarato=preço
        else:
            if maisbarato<preço:
                maisbarato=preço
                produto_maisbarato=nome
    while r not in 'SN':
        r=str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if r=='N':
            break
print(f'O total da compra foi de{tot}\nO total de produtos acima de R$ 1000 é de {mais_mil}\nO produto mais barato é o {produto_maisbarato} custando {maisbarato}')