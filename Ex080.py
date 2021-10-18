lista=list()
for  c in range(0,5):
    v=int(input('Digite um valor:'))
    if c==0 or v>lista[-1]:
        lista.append(v)
        print(f'Adicionando o valor na posição final da lista...')
    else:
        pos=0
        while pos<len(lista):
            if v<=lista[pos]:
                lista.insert(pos,v)
                print(f'Adicionando o valor na posição {pos} da lista...')
                break
                pos+=1
print('-='*30)
print(f'Os valores digitados da lista foram {lista}')