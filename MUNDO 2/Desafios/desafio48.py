#soma entre todos os números impares
#que são multiplos de 3 e que estão entre 1 e 500

s = 0
print('IMPARES MULTIPLO DE 3: ')
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c

print('A soma é: {}'.format(s))
print('FIM\n\n')


soma = 0
cont = 0
print('IMPARES MULTIPLO DE 3: ')
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont+= 1
        
print('A soma é: {}'.format(soma))
print('A quantidade de números é: {}'.format(cont))
print('FIM\n\n')