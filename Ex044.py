print('=============Lojas Maurício==================')
preço=float(input('Preço das compras:R$'))
print('Formas de pagamento')
print('[1] à vista dinheiro\cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x no cartão')
opção=int(input('Qual é a opção?'))
if opção==1:
    total=preço*0.9
elif opção==2:
    total=preço*0.95
elif opção==3:
    total=preço
    parcela=total/2

    print('Sua compra parcelada em 2x de R${:.2f}'.format(parcela))
elif opção==4:
    total=preço*1.2
    totparc = int(input('Quantas parcelas?'))
    parcela=total/totparc
    print('Sua compra parcelada em {}x de R${:.2f}'.format(totparc,parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,total))
