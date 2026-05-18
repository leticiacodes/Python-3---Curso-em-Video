#ler 3 números e dizer qual o maior e qual o menor

'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 >= n2 and n1 >= n3:
    print('Número {} é o maior'.format(n1))
    if n2 >= n3:
        print('Número {} é  o menor'.format(n3))
    else:
        print('Número {} é  o menor'.format(n2))
elif n2 >= n1 and n2 >= n3:
    print('Número {} é o maior'.format(n2))
    if n1 >= n3:
        print('Número {} é  o menor'.format(n3))
    else:
        print('Número {} é  o menor'.format(n1))
elif n3 >= n1 and n3 >= n2:
    print('Número {} é o maior'.format(n3))
    if n1 >= n2:
        print('Número {} é  o menor'.format(n2))
    else:
        print('Número {} é  o menor'.format(n1))
'''

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

menor = a

if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c

maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c

print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))