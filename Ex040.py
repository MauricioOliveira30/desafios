n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
média = (n1 + n2) / 2
if média >= 7:
    print('O aluno foi aprovado')
elif 7 > média > 5:
    print('O aluno está de recuperação')
elif média <= 5:
    print('O aluno está reprovado')
