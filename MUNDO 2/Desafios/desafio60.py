#ler um número e mostrar o fatorial
#5! = 120
#com while e depois com for

i = 1
num = int(input('Digite um número: '))
fat = 1
while i <= num:
    fat *= i
    i += 1
print('O fatorial (while): {}'.format(fat))

for c in range(i,num):
    fat *= i
print('O fatorial(for): {}'.format(fat))

##########
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')