#ler o ano de nascimento
#mostrar a categoria
# até 9 mirim
# até 14 infantil
# até 19 junior
# até 25 senior
# acima master

from time import localtime
#from datetime import date

ano = localtime().tm_year
#ano = date.today().year

nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano - nascimento

print('Idade: {} anos'.format(idade))

if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <= 25:
    print('CATEGORIA: SENIOR')
else:
    print('CATEGORIA: MASTER')