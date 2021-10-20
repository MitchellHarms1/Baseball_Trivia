import pygame as pg
from Settings import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(Blue)
        self.rect = self.image.get_rect()
        self.rect.center = (Width / 2, Hieght / 2)
        self.pos = vec(Width / 2, Hieght / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    
    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > Width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Width

        self.rect.center = self.pos

 