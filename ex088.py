from random import randint

lista=[]
jogos=[]
tot=1
print('-'*30)
print('   JOGA NA MEGA SENA   ')
print('-'*30)
quant=int(input('Quantos números quer que eu sorteie?'))
while tot<=quant:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
        cont+=1
        if cont>=6:
            break
        jogos.append(lista[:])
        lista.clear()
        lista.sort()
    tot+=1
print(f'Os números sorteados foram {jogos}')
