#ler 2 notas e calcular a media
# media < 5 reprovado
# entre 5.0 e 6.9 recuperação
# >= 7 aprovado

n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a nota: '))
media = (n1 + n2) / 2

print('A média é: {}'.format(media))

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media < 6.9: #if 7 > media >= 5:
    print('RECUPERÇÃO')
elif media >= 7.0:
    print('APROVADO!')