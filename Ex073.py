Times=('Atlético-PR','Fortaleza','Bragantino',
       'Palmeiras','Atlético-MG','Fluminense',
       'Bahia','Atlético-GO','Santos','Flamengo',
       'Corinthias','Internacional','Juventude','Sport Recife','Chapecoense',
       'Cuiabá','São Paulo','América-MG','Grêmio')
print('-='*20)
print(f'Lista de times do Brasileirão:{Times}')
print('-='*20)
print(f'Os 5 primeiros são{Times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são{Times[15:21]}')
print('-='*20)
print(f'Times em ordem alfabética{sorted(Times)}')
print('-='*20)
print(f'O Chapecoense está na {Times.index("Chapecoense")+1}ª posição')
