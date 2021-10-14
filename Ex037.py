núm = int(input('Digite um número inteiro:'))

print('Escolha uma das bases para conversão:')
print('[1] converter para Binário')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(núm,bin(núm)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(núm,oct(núm)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(núm,hex(núm)[2:]))
else:
    print('Opção inválida')