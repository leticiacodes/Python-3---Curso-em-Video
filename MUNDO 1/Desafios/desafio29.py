#ler a velocidade de um carro
#se < 80 multado
#multa de 7 reais a cada km depois de 80

velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print('Multa de {:.2f} reais'.format((velocidade - 80) * 7))
else:
    print('Parabéns voce respeitou o limite de velocidade!')