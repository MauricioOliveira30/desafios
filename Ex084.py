princ=list()
temp=list()
mai=men=0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    r=str(input('Quer continuar?[S/N]'))
    if len(princ)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
            if temp[1]<men:
                men=temp[1]

        princ.append(temp[:])
        temp.clear()
    if r  not in 'Ss':
            break
print('-='*30)
print(f'Ao todo foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso foi de  {mai}Kg.',end='')
for p in princ:
    if p[0]==mai:
        print(f'O maior peso cadastrado foi de [{p[0]}]')
