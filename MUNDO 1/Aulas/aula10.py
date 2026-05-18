'''
Condição
if carro.esquerda():
    bloco True
else:
    bloco False
'''

tempo = int(input('Quantos anos tem seu carro? '))

if tempo<=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

t = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')


nome = str(input('Qual o seu nome? '))
if nome == 'Letícia':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi: {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')