
import random
import os
import pickle
import board
import pygame
from pygame.locals import *

#Initialize Colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 155, 155, 155)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
MAROON   = ( 175,   0,   0)
BLUE     = (   0,   0, 255)
BROWN    = ( 139,  69,  19)


#Pygame Initialization
pygame.init()
monitorSpecs = pygame.display.Info()

screen = pygame.display.set_mode((0,0), FULLSCREEN)
pygame.display.set_caption("Lord Checkington")

clock = pygame.time.Clock()

#Board Initialization
game = board.NewBoard(8, 8)

game.Draw()

#Board Drawing Variables
borderW = 5
borderGap = 20
spaceW = (monitorSpecs.current_h - (borderGap * 2)) / game.height
boardW = spaceW * game.height

#Load Board Sprites
spritePath = os.path.join('Assets', 'Sprites')

bNormalSprite = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Sprites', 'Black Piece.png')), (spaceW, spaceW)).convert_alpha()
rNormalSprite = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Sprites', 'Red Piece.png')), (spaceW, spaceW)).convert_alpha()
bKingSprite = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Sprites', 'Black King.png')), (spaceW, spaceW)).convert_alpha()
rKingSprite = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Sprites', 'Red King.png')), (spaceW, spaceW)).convert_alpha()

#Main game loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
    
    screen.fill(BROWN)

    pygame.draw.rect(screen, MAROON, [(monitorSpecs.current_w / 2) - (boardW / 2), (monitorSpecs.current_h / 2) - (boardW / 2), boardW, boardW])
    
    for row in range(len(game.pos[0]) - 1, -1, -1):
        rowMode = row % 2
        spaceY = monitorSpecs.current_h - (spaceW * (row + 1)) - borderGap
        for space in range(len(game.pos)):
            spaceX = (monitorSpecs.current_w / 2) - (boardW / 2) + (spaceW * space)

            if space % 2 == rowMode:
                pygame.draw.rect(screen, BLACK, [spaceX, spaceY, spaceW, spaceW])

                if game.pos[space][row] != None:
                    
                    if game.pos[space][row][board.P_COL] == 0:
                        if game.pos[space][row][board.P_KING]:
                            screen.blit(rKingSprite, [spaceX, spaceY])
                        else:
                            screen.blit(rNormalSprite, [spaceX, spaceY])
                            
                    elif game.pos[space][row][board.P_COL] == 1:
                        if game.pos[space][row][board.P_KING]:
                            screen.blit(bKingSprite, [spaceX, spaceY])
                        else:
                            screen.blit(bNormalSprite, [spaceX, spaceY])
                        
            

    pygame.draw.rect(screen, GREY, [(monitorSpecs.current_w / 2) - (boardW / 2) - (borderW / 2), (monitorSpecs.current_h / 2) - (boardW / 2) - (borderW / 2), boardW + borderW, boardW + borderW], borderW)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
