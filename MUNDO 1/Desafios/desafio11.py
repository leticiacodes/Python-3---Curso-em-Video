#calcular area, litro tinta p area de 2m²
largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
tinta = area / 2
print('A quantidade de litros para pintar uma aréa de {} é de {}'.format(area,tinta))
