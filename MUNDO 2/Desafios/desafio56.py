#ler nome, idade e sexo de 4 pessoas
#a media de idade do grupo
#qual o nome do homem mais velho
#quantas mulheres tem menos de 21 anos

media = 0
mulherqtd = 0
maisvelho = 0
 
for c in range(0,4):
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    media += idade
    sexo = str(input('SEXO: ')).strip().lower()

    if sexo == 'feminino':
        if idade < 21:
            mulherqtd += 1
    if sexo == 'masculino':
        if idade > maisvelho:
            maisvelho = idade
            nomehomem = nome

print('A media da idade do grupo é: {}'.format(media / 4))
print('Quantidade de mulher com menos de 21 anos: {}'.format(mulherqtd))

if maisvelho > 0:
    print('O homem mais velho é {}'.format(nomehomem))
else:
    print('Não possui homem no grupo')