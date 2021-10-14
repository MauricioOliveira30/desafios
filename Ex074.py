maior=0
menor=0
from random import randint
valores= (randint(1,5),randint(1,5),randint(1,5),randint(1,5)
          ,randint(1,5))
print('Os valores sorteados foram:',end='')
for val in valores:
    print(f'{(val)}',end=' ')

print(f'\nO valor maior foi {max(valores)} e o valor menor foi {min(valores)}')