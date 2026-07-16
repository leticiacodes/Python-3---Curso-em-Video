#calcular o valor a ser pago por um produto
#considerando o preço normal e a cond de pagar
#a vista dinheiro / cheque: 10% desconto
#a vista no cartão 5% de desconto
#ate 2x no cartão preço normal
#3x ou + no cartão 20% de juros

normal = float(input('Digite o preço normal do produto: '))
print('Escolha uma opção para o pagamento:')
print('1 - A VISTA DINHEIRO / CHEQUE: DESCONTO DE 10%')
print('2 - A VISTA CARTÃO: 5% DE DESCONTO')
print('3 - ATÉ 2X NO CARTÃO: PREÇO NORMAL')
print('4 - 3X OU MAIS NO CARTÃO: 20% DE JUROS')
op = int(input('Opção: '))

if op == 1:
    print('Novo valor: {:.2f} reais'.format(normal - (normal * 0.10)))
elif op == 2:
    print('Novo valor: {:.2f} reais'.format(normal - (normal * 0.05)))
elif op == 3:
    print('Sua comprar será divida em 2x')
    print('Valor da parcela: {:.2f} reais'.format(normal / 2))
elif op == 4:
    parcelas = float(input('Quantas vezes voce quer parcelar? '))
    valorParcela = (normal + (normal * 0.20)) / parcelas
    print('Sua compra será divididas em {} parcelas de {:.2f} reais'.format(parcelas, valorParcela))
    print('Valor final: {:.2f} reais'.format((normal + (normal * 0.20))))
else:
    print('ERRO! POR FAVOR ESCOLHA UMA OPÇÃO VALIDA')
