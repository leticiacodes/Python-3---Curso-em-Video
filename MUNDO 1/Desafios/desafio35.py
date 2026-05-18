#ler um comprimento de 3 retas e diga
#ao usuario se elas podem ou não
#formar um triangulo

r1 = float(input('Digite o tamanho da reta: '))
r2 = float(input('Digite o tamanho da reta: '))
r3 = float(input('Digite o tamanho da reta: '))

'''
if r1 >= r2 and r1 >= r3:
    if (r2 + r3) > r1:
        print('Pode formar um triangulo')
    else:
        print('Não pode formar um triangulo')
elif r2 >= r1 and r2 >= r3:
    if (r1 + r3) > r2:
        print('Pode formar um triangulo')
    else:
        print('Não pode formar um triangulo')
elif r3 >= r1 and r3 >= r2:
    if (r1 + r2) > r3:
        print('Pode formar um triangulo')
    else:
        print('Não pode formar um triangulo')
else:
    print('Erro')
'''

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')