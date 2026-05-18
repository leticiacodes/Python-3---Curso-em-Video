#um número entre 0 e 5
#usuario tenata descobrir o num 
#mensagem se o usuario vendeu ou perdeu

from random import randint
from time import sleep
computador = randint(0, 5) #FAZ O SORTEIO
print('-=-'*20)
num = int(input('Em qual número eu pensei de 1-5: '))
print('PROCESSANDO...')
sleep(2)
if computador == num:
    print('Parabéns voce acertou')
else:
    print('Mais sorte na proxima')
    print('O número era: {}'.format(computador))
