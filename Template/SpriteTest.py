import pygame as pg
from Settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x = -self.rect.WIDTH
        if keys[pg.K_RIGHT]:
            self.rect.x = self.rect.WIDTH
        if keys[pg.K_UP]:
            self.rect.y = -self.rect.WIDTH
        if keys[pg.K_DOWN]:
            self.rect.y = self.rect.WIDTH

        # apply friction
        #self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        #self.vel += self.acc
        #self.pos += self.vel + 0.5 * self.acc
    
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.center = self.pos