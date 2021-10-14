a = float(input('Digite o primeiro  lado para o triângulo:'))
b = float(input('Digite o segundo lado para o triâgulo:'))
c = float(input('Digite o terceiro lado para o triângulo:'))
if b - c < a < b + c and a > c - b:
    print('Forma um triângulo')
    if a==b==c:
        print('Triângulo Equilátero')
    elif a!=b!=c!=a:
            print('Triângulo escaleno')
    else:
        print("Triângulo isósceles")
else:
    print('Não forma um triângulo')
