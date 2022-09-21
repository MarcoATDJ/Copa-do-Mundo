from msilib.schema import Icon
from tkinter import font
from unicodedata import name
import pygame
from pygame.locals import *
from sys import exit
import button


pygame.init()

#Banco de imagens
game_icon = pygame.image.load("assets\\logo.png")
init_pag = pygame.image.load("assets\\jogo_fundo.png")
group_pag = pygame.image.load("assets\\jogo_fundo_grupos.png")
ranking_pag = pygame.image.load("assets\\jogo_fundo_ranking.png")
button_play = pygame.image.load("assets\\botao_jogar.png")
button_exit = pygame.image.load("assets\\botao_sair.png")
input_text = pygame.image.load("assets\\input_name.png")

#Definir Fontes
font = pygame.font.SysFont("arialblack", 40)

#Definir Cor
cor_texto = (0,0,0)

#Configurações da tela
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption('Copa do Mundo')
pygame.display.set_icon(game_icon)

#Funções
def texto_w(texto, fonte, texto_cor, x, y):
    img = font.render(texto, True, texto_cor)
    screen.blit(img, (x, y))

#Variaveis do jogo
jogo_status = 0 #0:inicio / 1:perguntas / 2:ranking
run = True

#Botoes instancias
botao_play = button.Button(850, 580, button_play, 1)
botao_sair_i = button.Button(850, 670, button_exit, 1)
botao_sair_g = button.Button(1000, 670, button_exit, 1)
botao_sair_r = button.Button(1000, 470, button_exit, 1)

#Loop Jogo
while run:
    #Cabeçalho
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Tela inicial  
    if jogo_status == 0:     
        screen.blit(init_pag, (0, 0))
        
        
        
        if botao_play.draw(screen):
            jogo_status = 1    
            print("vai para grupos")      
        if botao_sair_i.draw(screen):
            print("saiu do jogo")   
            run = False    
    elif jogo_status == 1:
        screen.blit(group_pag, (0, 0))
        if botao_sair_g.draw(screen):
            print("saiu do jogo")   
            jogo_status = 2
    elif jogo_status == 2:
        screen.blit(ranking_pag, (0, 0))
        if botao_sair_r.draw(screen):
            print("saiu do jogo")   
            run = False
    
    
    
    
    pygame.display.update()
    
pygame.quit()