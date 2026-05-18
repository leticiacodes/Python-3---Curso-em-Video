#ler o nome de uma pessoa e mostrar o primeiro e ultimo
#Ana Maria de Souza
#primeiro: Ana
#último = Souza

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Primeiro nome: {}\n'.format(nome[0]))
print('Ultimo nome: {}\n'.format(nome[len(nome)-1]))