#ler um numero inteiro n
#mostar na tela os n primeiros elementos
#de um sequencia de Fibonacci
#0 1 1 2 3 5 8

primeiro = 0
segundo = 1

qtd = int(input('Qunatos termos vc quer mostrar? '))
cont = 3

if qtd >= 1:
        print(f'{primeiro} -> ',end='')
if qtd >= 2:
        print(f'{segundo} -> ',end='')

while cont <= qtd:

    f = primeiro + segundo
    print(f'{f} -> ',end=' ')
    primeiro = segundo
    segundo = f
    cont += 1
    
print('FIM')