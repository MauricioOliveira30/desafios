import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar  qual foi?')
tentativas = 0
acertou = False
computador = random.randint(0, 10)
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    tentativas+=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
            if jogador > computador:
                print('Menos...Tente mais uma vez')
print('Acertou com {} tentativas!Parabéns'.format(tentativas))
