import pygame
from Settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
       super().__init__()
       self.image = pygame.Surface((32, 32))
       self.image.fill(Blue)
       self.rect = self.image.get_rect(center = (300, 490))
       self.plate = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_RIGHT]:
            self.rect.x += 5
        if keys[pg.K_UP]:
            self.rect.y -= 5
        if keys[pg.K_DOWN]:
            self.rect.y += 5
        if keys[pg.K_a]:
            self.nextBase()

    def nextBase(self):
        
        bases = [(304, 494),(109, 302), (301, 118), (492, 301)]
        
        for event in pygame.event.get(): 
            if event.type == pygame.KEYUP: 

                self.plate += 1
                self.rect.center = bases[(self.plate % 4 )]



# Home (304, 494)
# Third base  (492, 301)
#Second (301, 118)
# First (109, 302)