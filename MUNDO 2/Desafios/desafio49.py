#fazer tabuada do desafio 9 com laço for 
#o usuario escolhe o número

n = int(input('Numero: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, c*n))