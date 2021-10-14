import random

print('-=--=' * 12)
print("Vou pensar num número entre 0 e 5 Tente adivinhar... ")
print('-=--=' * 12)
jogador = int(input('Em que número pensei?'))
computador = random.randint(0, 5)
print('PROCESSANDO...')
if jogador == computador:
    print('PARABÉNS!Você conseguiu vencer!')
else:
    print('Ganhei pensei no número {} e não no {}!'.format(computador, jogador))
