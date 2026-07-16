#recebe um int
#o ususario escolher se quer converter par
#1 binario 2 octal 3: hexadecimal

import math
num = int(input('Digite um número: '))
print('\nESCOLHA UMA OPÇÃO DE CONVERSÃO\n')
print('1 - BINARIO\n')
print('2 - OCTAL\n')
print('3 - HEXADECIMAL\n')
op = int(input('Opção: '))

if op == 1:
    print('Binario: {}'.format(bin(num)[2:]))
elif op == 2:
    print('Octal: {}'.format(oct(num)[2:]))
elif op == 3:
    print('HEXADECIMAL: {}'.format(hex(num)[2:]))
else:
    print('ERRO! TENTE NOVAMENTE')