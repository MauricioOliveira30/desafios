while True:
    print('-'*20)
    núm=int(input('Quer ver a tabuada de qual valor?'))
    if núm < 0:
        break
    for c in range(0,11):
        print(f'{núm}x{c}={núm*c}')
    print('-'*20)

print('PROGRAMA TABUADA ENCERRADO.Volte sempre!')