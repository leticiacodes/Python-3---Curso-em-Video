#ler um número de 0 a 9999 e mostre cada um dos digitos separados
#com string e matematicamente
#1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar:1


'''Matematicamente'''
''' n = int(input('Digite um número: '))

uni = n % 10
n = n // 10
dez = n % 10
n = n // 10
cent = n % 10
n = n // 10
mil = n % 10

print('Unidade: {}\n'.format(uni))
print('Dezena: {}\n'.format(dez))
print('Centena: {}\n'.format(cent))
print('Milhar: {}\n'.format(mil)) '''

''''''
'''Matematicamente'''
n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número: {}'.format(n))
print('Unidade: {}\n'.format(u))
print('Dezena: {}\n'.format(d))
print('Centena: {}\n'.format(c))
print('Milhar: {}\n'.format(m)) 