#crie um programa que faça o computador
#jogar jokenpo com vc

'''
from random import choice

lista = ['pedra','papel','tesoura']
computador = choice(lista)

usuario = str(input('Escolha: Pedra, Papel ou Tesoura: '))
usuario = usuario.strip().lower()

if computador == usuario:
    print('EMPATE')
elif usuario == 'pedra':
    if computador == 'tesoura':
        print('VOCE VENCEU! PARABÉNS')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
    else:
        print('VOCE PERDEU, MAIS SORTE NA PRÓXIMA')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
elif usuario == 'papel':
    if computador == 'pedra':
        print('VOCE VENCEU! PARABÉNS')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
    else:
        print('VOCE PERDEU, MAIS SORTE NA PRÓXIMA')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
elif usuario == 'tesoura':
    if computador == 'papel':
        print('VOCE VENCEU! PARABÉNS')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
    else:
        print('VOCE PERDEU, MAIS SORTE NA PRÓXIMA')
        print('COMPUTADOR ESCOLHEU: {}'.format(computador))
else:
    print('ERRO')
'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''SUAS OPÇÕES:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)

print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATOU!')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA!')