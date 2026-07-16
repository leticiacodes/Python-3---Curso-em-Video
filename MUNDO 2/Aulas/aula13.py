#repetição for

for c in range(1, 6): #de um até 6 mas so considera 5x 
    print('Oi')
print('FIM!')

for c in range(1, 7): #de um até 6
    print(c)
print('FIM!')

for c in range(6 , 0, -1): #conta de 6 até 0
    print(c)
print('FIM!')

for c in range(0, 7, 2): #incrementa de 2 em 2
    print(c)
print('FIM!')

'''
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM!')

i = int(input('Digite um número para o inicio: '))
f = int(input('Digite um número para o fim: '))
p = int(input('Digite um número para o passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')
'''
s = 0
for c in range(0, 3):
    num = int(input('Numero: '))
    s += num

print('O somatorio de todos os valores é: {}'.format(s))
print('FIM!')