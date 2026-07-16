#ler 2 num int
#comparar o 1 valor maior
#o 2 valor maior
#ñ existe maior são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))


if n1 > n2:
    print('Primeiro valor é maior')
elif n2 > n1:
    print('Segundo valor é maior')
elif n1 == n2:
    print('Não existe maior são iguais!')
