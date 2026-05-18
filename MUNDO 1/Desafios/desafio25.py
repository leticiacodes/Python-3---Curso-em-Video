#ler o nome de uma pessoa e dizer se tem 'SILVA' no nome

''' nome = str(input('Digite seu nome completo: '))
print('O nome possui SILVA? ')
print(nome.upper().find('SILVA') != -1) '''

''''''
nomeSilva = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nomeSilva.upper()))

