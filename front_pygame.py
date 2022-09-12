from msilib.schema import Icon
import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1366, 768))
game_icon = pygame.image.load('assets\\logo.png')
init_pag = pygame.image.load('assets\\jogo_fundo.png')
group_pag = pygame.image.load('assets\\jogo_fundo_grupos.png')
ranking_pag = pygame.image.load('assets\\jogo_fundo_ranking.png')

pygame.display.set_caption('Copa do Mundo')
pygame.display.set_icon(game_icon)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.blit(init_pag, (0, 0))
    
        
    
    pygame.display.update()