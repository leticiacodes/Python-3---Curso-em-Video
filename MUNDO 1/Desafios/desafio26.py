#ler uma frase
#contar qts a tem
#em qual posição aparece pela 1 vez
#e pela ultima vez

frase = str(input('Digite uma frase: ')).strip()
print('Quantidade de a: {}'.format(frase.lower().count('a')))
print(frase.upper().find('A')+1) #posição da 1
print(frase.upper().rfind('A')+1) #ultima vez de a