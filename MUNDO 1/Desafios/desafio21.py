#abra e reproduza um audio de arq mp3

import pygame
pygame.init() #inicializa o pygame
pygame.mixer.music.load('MUNDO 1/Desafios/audiodesafio21python.mp3') #carrega o arquivo
pygame.mixer.music.play()#toca
pygame.event.wait()
