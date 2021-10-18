lista=[]
mai=men=0
for c in range(0,5):
    lista.append(int(input(f'Digite a posição {c}:')))
    if c==0:
        mai=men=lista[c]
    if mai<lista[c]:
        mai=lista[c]
else:
    if men>lista[c]:
        men=lista[c]
print(f'O maior valor digitado foi {mai} na posição',end='')
for i,v in enumerate(lista):
    if v==mai:
        print(f'...{i}')
print('O menor valor foi encotrado na posição',end='')
for i,v in enumerate(lista):
    if v==men:
        print(f'...{i}')
print(lista)
