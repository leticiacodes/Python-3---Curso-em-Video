#ler 2 valores e mostrar um menu na tela
#1 somar / 2 multiplicar / 3 maior / 4 novos números
#5 sair do programa

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

op = 0
while op != 5:
    
    print('1 - SOMAR ')
    print('2 - MULTIPLICAR')
    print('3 - MAIOR')
    print('4 - NOVOS NÚMEROS')
    print('5 - SAIR DO PROGRAMA')
    op = int(input('Opção: '))

    if op == 1:
        print('{n1} + {} = {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1 > n2:
            print('MAIOR: {}'.format(n1))
        elif n2 > n1:
            print('MAIOR: {}'.format(n2))
        else:
            print('SÃO IGUAIS')
    elif op == 4:
        print('Novos valores ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    elif op == 5:
        print('Encerrando....')
    else:
        print('Opção invalida')

