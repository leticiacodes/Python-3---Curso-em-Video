#4 aluno
#mostrar a ordem dos sorteados
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Ordem do sorteio: ')
print(lista)

'''
se eu fizer com sample ele cria uma copia
sorteio = random.sample(lista, k=4)
print(sorteio)
'''