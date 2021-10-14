frase = str(input('Digite uma frase:')).upper().strip()
print('Quantas vezes aparece {} a letra A'.format(frase.count("A")))
print('A primeira letra apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra apreceu na posição {}'.format(frase.rfind('A')+1))
