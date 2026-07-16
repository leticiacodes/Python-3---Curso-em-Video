#melhorar o jogo do desafio 28
#mas agora o jogador tenta a adivinhar até acerta
#mostrar quantas chances a pessoa teve até vencer
# um numero de 0 a 10

from random import randint
from time import sleep
computador = randint(0, 10) #FAZ O SORTEIO

cont = 0

while True:
    jogador = int(input('Em qual número eu pensei de 1-10: '))
    print('PROCESSANDO...')
    sleep(0.5)
    cont += 1
    if computador == jogador:
        print('Parabéns voce acertou')
        print('Voce precisou de {} chances para vencer'.format(cont))
        break   
    else:
        print('Mais sorte na proxima')
        if computador > jogador:
            print('O número é maior')
        elif jogador > computador:
            print('O número é menor')
        

'''
acertou = False
cont = 0

while not acertou:
    jogador = int(input('Em qual número eu pensei de 1-10: '))
    cont += 1
    if computador == jogador:
        print('Parabéns voce acertou')
        print('Voce precisou de {} chances para vencer'.format(cont)) 
        acertou = True
    else:
        print('Mais sorte na proxima')
        if computador > jogador:
            print('O número é maior')
        elif jogador > computador:
            print('O número é menor')
'''