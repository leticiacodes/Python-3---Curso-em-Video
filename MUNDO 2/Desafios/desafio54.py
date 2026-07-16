#ler o ano de nascimento de 7 pessoas
#dizer qts já estão na maior idade e qts são menor
#considerar 21 
from datetime import date
ano = date.today().year
maior = 0
for c in range(1, 8):
    data = int(input('Digite a data de nascimeto: '))
    if ano - data >= 21:
        maior += 1

print('Quantidades de pessoas com maior idade: {}'.format(maior))
print('Quantidade de pessoas em menor idade: {}'.format(7 - maior))