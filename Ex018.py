import math

ângulo = float(input('Digite um ângulo qualquer:'))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {}° tem seno {:.2f} cosseno {:.2f} e tangente {:.2f}'.format(ângulo, seno, cosseno, tangente))
