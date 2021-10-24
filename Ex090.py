aluno=dict()
aluno['nome']=str(input('Nome:'))
aluno['média']=float(input(f'A média de {aluno["nome"]}:'))
if aluno['média']>=7:
    aluno['situação']="Aprovado"
elif aluno['média']>=5:
    aluno['situação']="RECUPERAÇÃO"
else:
    aluno['situação']="REPROVADO"
print('-='*30)
print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["média"]}')
print(f'- situação é igual a {aluno["situação"]}')

