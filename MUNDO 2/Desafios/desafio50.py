#ler 6 números inteiros
#mostrar a soma dos que forem par
#se o valor digitado for impar desconsidere

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Número: '))
    if n % 2 == 0:
        s += n
        cont += 1

print('Soma dos números pares: {}'.format(s))
print('A quantidade números pares foi: {}'.format(cont))