#calcular valor do aluguel de um carro: km = 0.15, diaria = 60
dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos kms percorridos? '))
valor = (km * 0.15) + (dias * 60)
print('Valor a pagar é: {:.2f}'.format(valor))