#ler o peso e altura e calcule o IMC
#abaixo de 18.5: Abaixo do peso
#entre 18.5 e 25: peso ideal
#25 até 30: Sobrepeso
#30 até 40: obsidade
# > 40 obsidade morbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (pow(altura, 2))

print('IMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25: #elif imc < 25
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBSEIDADE')
else:
    print('OBSIDADE MORBIDA')