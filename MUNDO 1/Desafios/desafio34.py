#ler o salario de um funcionario
#para salarios maiores de 1250 calcule 10% de aumento
#para menores o aumento é de 15%

salario = float(input('Digite o salário: '))
if salario <= 1250:
    print('Novo salario: {} reais'.format(salario * 0.15 + salario))
else:
    print('Novo salario: {} reais'.format(salario * 0.10 + salario))