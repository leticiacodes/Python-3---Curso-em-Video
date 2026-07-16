#ler varios números inteiros do teclado
#parar quando digitar 999
#mostrar qts num foram digitados
#e qual foi a soma entre eles (desconsiderar 999)

num = 0
soma = 0
qtd = 0
#num = qtd = soma = 0
while num != 999:
    num = int(input('Número (digite 999 para parar): '))
    if num != 999:
        soma += num
        qtd += 1

print(f'A soma foi: {soma}')
print(f'A quantidade de números foi: {qtd}')

################
num = qtd = soma = 0
num = int(input('Número (digite 999 para parar): '))
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Número (digite 999 para parar): '))

print(f'A soma foi: {soma}')
print(f'A quantidade de números foi: {qtd}')