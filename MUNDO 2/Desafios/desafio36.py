#emprestimo bancario
#ler o valor da casa, o salario 
#qts anos ele vai levar pra pagar
#calcular a prestação mensal não pode ser
#maior que 30% do salario senão o emprestimo será negado

valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = float(input('Qual o tempo que vc vai pagar? '))

prestacao = valorCasa / (anos * 12)
percentual = salario * 0.3

if prestacao > percentual:
    print('Emprestimo negado!')
else:
    print('Emprestimo aceito')
    print('Valor da pestacao minima: {:.2f} reais'.format(prestacao))