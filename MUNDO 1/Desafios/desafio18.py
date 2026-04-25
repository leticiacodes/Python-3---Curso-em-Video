#Ler um angulo e mostrar seno, cos, tg
#tem que converter para rad
import math
ang = float(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg =  math.tan(math.radians(ang))

print('Seno {:.2f} \nCosseno {:.2f} \nTangente {:.2f}'.format(seno, cos, tg))

'''
from math import radians, sin, cos, tan
ang = float(input('Digite o angulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tg =  tan(radians(ang))

print('Seno {:.2f} \nCosseno {:.2f} \nTangente {:.2f}'.format(seno, cos, tg))



'''