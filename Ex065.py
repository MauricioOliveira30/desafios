r='S'
soma=maior=menor=cont=0
while r in'S':
    núm=int(input('Digite um número:'))

    soma+=núm
    cont+=1
    if cont == 1:
        maior=menor=núm
    else:
        if maior>núm:
            maior=núm
            if menor<núm:
                menor=núm
    r = str(input("Quer continuar?[S/N]:")).upper().strip()[0]
media=soma/cont


print('A média dos números foi de {:.2f} o menor número é {} e o maior número é {} '.format(media,menor,maior))