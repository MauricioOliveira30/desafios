from random import randint
from time import sleep
itens=('PEDRA','PAPEL','TESOURA')
computador=randint(0,2)
print('''Suas opções 
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador ==0:#Pedra
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('Jogador Vence')
    elif jogador==2:
        print('Computador Vence')
    else:
        print('Jogada Inválida')
elif computador==1:#Papel
    if jogador==0:
        print('Computador Vence')
    elif jogador==1:
        print('Empate')
    elif jogador==2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida')
elif computador==2:#Tesoura
    if jogador==0:
        print('Jogador Vence')
    elif jogador==1:
        print('EMPATE')
    elif jogador ==2:
        print('Computador Vence')
    else:
        print('Jogada Inválida')