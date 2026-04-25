#Ler o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcular e mostrar o comprimento da hipotenusa

import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('Hipotenusa {}'.format(math.hypot(co, ca)))

''' co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1/2)
print('Hipotenusa {:.2f}'.format(hip)) '''