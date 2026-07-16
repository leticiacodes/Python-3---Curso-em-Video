#dizer se o triangulo formado é
#equilatero todos os lados iguais
#isosceles 2 lados iguais
#escaleno todos os lados diferentes
#e dizer se pode formar um triangulo

r1 = float(input('Digite o tamanho da reta: '))
r2 = float(input('Digite o tamanho da reta: '))
r3 = float(input('Digite o tamanho da reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo ', end='')
    if r1 == r2 and r2 == r3: # if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não pode formar um triangulo')

