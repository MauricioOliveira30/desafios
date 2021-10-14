casa = float(input('Valor da casa:R$'))
salário = float(input('Salário do comprador:R$'))
financiamento = int(input('Quantos anos de financiamento:'))
prestação = casa / (financiamento*12)
print('Com salário de {} em {} anos a prestação será de {:.2f}'.format(salário,financiamento,prestação))
if prestação <= salário*0.3:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Negado')
