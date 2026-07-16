#ler o peso de 5 pessoas
#dizer qual o menor e maior peso lido
'''
maior = 0
menor = 99999


for c in range(0,5):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('Maior peso: {}kg'.format(maior))
print('Menor peso: {}kg'.format(menor))

'''

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Digite o peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso: {}kg'.format(maior))
print('Menor peso: {}kg'.format(menor))
