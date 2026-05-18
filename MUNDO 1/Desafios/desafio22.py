#receber um nome completo
#transformar todas as letras em maiusculas
#todas em minusculas
#qts letra tem sem considerar espaços
#qts letras tem o primeiro nome

nome = input('Digite seu nome: ')
print(nome.upper())
print(nome.lower())
espaco = len(nome) - nome.count(' ')
print(espaco)
letras = nome.split()
print(len(letras[0]))

''''''

nomeCompleto = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em maiusculas é {}'.format(nomeCompleto.upper()))
print('Seu nome em minusculas é {}'.format(nomeCompleto.lower()))
print('Seu nome tem ao todo tem {} letras'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nomeCompleto.find(' ')))
separa = nomeCompleto.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
