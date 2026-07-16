#refazer o desafio 51
#ler o primeiro termo de uma PA
#a razão mostrar os 10 primeiros termos usando while

'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print(c, end=' ')
print('ACABOUU')
'''

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
i = p
while i < decimo:
    print(i, end=' ')
    i += r
    if i == decimo:
        print(decimo)


#######Guanabara
print("Gerador de PA")
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}->',end=' ')
    termo +=razao
    cont += 1
print('FIM')