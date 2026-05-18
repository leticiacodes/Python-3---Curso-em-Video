#perguntar uma distancia em km
#precço da passagem cobrando 0,50 por km para km até 200k
#se maior 0,45

distancia = float(input('Digite a distancia total: '))
''' if distancia <= 200:
    print('Valor cobrado: {} reais'.format(distancia*0.50))
else:
    print('Valor cobrado: {} reais'.format(distancia*0.45)) '''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Valor cobrado: {} reais'.format(preco))