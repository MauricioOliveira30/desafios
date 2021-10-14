a = float(input('Digite o primeiro  lado para o triângulo:'))
b = float(input('Digite o segundo lado para o triâgulo:'))
c = float(input('Digite o terceiro lado para o triângulo:'))
if b - c < a < b + c and a > c - b:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
if a - c < b < a + c and b > c - a:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
if a - b < c < a + b and c > b - a:
    print('Forma um triângulo')
else:
    print('Não forma um triâgulo')
