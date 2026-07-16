#ler varios numeros int
#mostrar a media
#maior e menor valor
#perguntar ao usuario se ele quer ou não continuar a digitar

maior = 0
menor = 0
media = 0
i = 0
qtd = 1
while True:
    num = int(input('Digite um número: '))
    res = input('Quer continuar [S/N]: ').upper()
    media += num

    if i == 0:
        maior = num
        menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    if res == 'N':
        break
    i+=1
    qtd += 1
print(media/qtd)
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))

#while res in 'Ss':