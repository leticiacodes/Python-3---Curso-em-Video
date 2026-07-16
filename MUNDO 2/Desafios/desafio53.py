#ler uma frase e dizer se ela é palindromo
#desconsidere os espaços

frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''

#vai do final, para o começo
for letra in range(len(junto)-1, -1, -1): 
    inverso += junto[letra]
if inverso == junto:
    print('PALINDROMO')
else:
    print('NÃO É PALINDROMO')