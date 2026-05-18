'''Manipulando cadeias de texto'''

#atribuindo em uma variavel
frase = 'Curso em Vídeo Python'
print(frase)
#ele difere maiusculas de minusculas

''' fatiamento de string '''

#pegar pelo indice
frase[9]
print(frase[9])

#pegar pelo intervalo de indices mas o 14 não entra
frase[9:14]
print(frase[9:14])

#aqui não tem problema pq é N -1 
frase[9:21]
print(frase[9:21])

#pulando com base em um intervalo de 2
frase[9:21:2]
print(frase[9:21:2])

#começa do caractere na posição 0
frase[:5]
print(frase[:5])

#vai até o final
frase[15:]
print(frase[15:])

#começa do 9 até o final pulando de 3
frase[9::3]
print(frase[9::3])

'''Analise'''
len(frase) #tamanho / comprimento = 21
frase.count('o') #conta a quantidade de o minusculos = 3
frase.count('o',0,13) #contagem com fatiamento = 1
frase.find('deo') #mostra a posição que começa no caso 11
frase.find('Android') # retorna -1 pq não encontrou
'Curso' in frase #Existe a palavra Curso dentro frase: True

'''Transformção'''
frase.replace('Python','Android') #troca Python por Android
frase.upper() #frase vai ficar maiusculo
frase.lower() #frase vai ficar em minusculo
frase.capitalize() #deixa tudo em minusculo exceto o primeiro caracte
frase.title() #transforma a primeira letra de cada palavra em Maiusculo

frase = '  Aprenda Python '
frase.strip() #remove os espaços em excesso
frase.rstrip() #remove os espaços em excesso pela direita
frase.lstrip() #remove os espaços em excesso pela esquerda

'''Divisão'''
frase.split() # divide em listas diferentes


'''Junção'''
'-'.join(frase) #junta a string mas separa com -