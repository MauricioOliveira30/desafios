import datetime
ano=datetime.date.today().year
maior=0
menor=0

for c in range(1, 8):
    nascimento = int(input(' Em que ano a {}ª nasceu?'.format(c)))
    idade=ano-nascimento
    if idade>=21:
          maior+=1
    else:
        menor+=1
print('Ao todo temos {} pessoas maiores de idade\nE também  tivemos {} pessoas menores de idade'.format(maior,menor))