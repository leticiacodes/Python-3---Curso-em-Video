#ler um número int e dizer se ele é ou não primo

n = int(input('Digite um número: '))

cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1

if cont == 2: 
    print('É primo!')
else:
    print('NÃO é primo')