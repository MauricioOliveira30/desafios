listanum=[]
maior=menor=0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor na posição {c}:')))
    if c==0:
            maior=menor=listanum[c]
else:
    if listanum[c]>maior:
        maior=listanum[c]
        if listanum[c]<menor:
            menor=listanum[c]
print('-='*30)
print(f'Os valores digitados foram {listanum}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')