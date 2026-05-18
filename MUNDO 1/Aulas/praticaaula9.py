frase = 'Curso em Vídeo Python'
print(frase[::2])

print('Oi')

#imprime sem precisar de vários prints
print('''Python é simples e poderoso
perfeito para aprender e criar rápido muito''')

print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python','Android'))

#aqui seria para muda de fato
#frase = frase.replace('Python','Android')
print(frase.split()) #cria uma lista com separador de espaço
dividido = frase.split()
print(dividido[2][3])
