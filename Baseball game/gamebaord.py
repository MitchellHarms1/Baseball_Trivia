import pygame, sys
import random
from Settings import *
from Sprite import *

pygame.init()
pygame.display.set_caption("The Baseball game")
display = pygame.display.set_mode((Width*Tilesize,Hieght*Tilesize)) #Tile size is 32
#pygame.display.set_caption("The Baseball Game")


#Sprites
all_sprites = pygame.sprite.Group()
    

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(Hieght):
        
        for col in range(Width):
            #print(map1[row -1][col])
            pygame.draw.rect(Display,TileColor[map1[row -1][col]], (col*Tilesize,row*Tilesize,Tilesize,Tilesize))

    pygame.display.update()
    all_sprites.update() 