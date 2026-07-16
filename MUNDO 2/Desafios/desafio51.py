#ler o primeiro termo e a razão de um pa
#mostrar os 10 primeiros termos

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print(c, end=' ')
print('ACABOUU')