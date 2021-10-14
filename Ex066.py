s = cont = 0
while True:
    núm = int(input('Digite um valor(999 para parar):'))
    if núm == 999:
        break
    cont += 1
    s += núm
print(f'A soma dos {cont} valores foi {s}!')
