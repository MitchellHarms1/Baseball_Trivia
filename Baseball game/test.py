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


class Player1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.image.fill(Blue)
        self.rect = self.image.get_rect()
        #self.rect.center = (Width / 2, Hieght / 2)
        self.vx = 288
        self.vy = 480
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player1()
        self.all_sprites.add(self.Player1)
        self.run()
    
    def run(self):
        # game loop
        self.playing = True


        while self.playing:

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