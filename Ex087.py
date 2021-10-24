matriz=[[0,0,0],[0,0,0],[0,0,0]]
spar=mai=scol=0
for l in range(0,3):
 for c in range(0,3):
     matriz[l][c]=int (input(f'Digite um valor para [{l}][{c}]:'))
print(matriz)
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}',end='')
    print()
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2==0:
            spar+=matriz[l][c]
for l in range(0,3):
    if matriz[l][c]==matriz[l][2]:
        scol+=matriz[l][2]
for c in range(0,3):
    if c==0 or matriz[1][c]:
        mai=matriz[1][c]
print('-='*30)
print(f'A soma dos pares é {spar}')
print(f'A soma dos elementos da terceira coluna  é {scol}')
print(f'O maior da segunda linha é {mai}')