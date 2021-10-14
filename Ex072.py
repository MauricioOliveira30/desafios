números=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove'
         ,'dez','onze','doze','treze','catorze','quinze','dezeseis','dezeste','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if 0<=n<=20:
        break
    print('Tente novamente.',end='')
print(f'O número que você digitou foi {números[n]}')
