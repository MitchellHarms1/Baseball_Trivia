import pygame as pg


#Define tiles
D = 0 #dirt
G = 1 #grass
W = 2 #white

#Define tile color
Brown = (115,118,83)
Green = (96,128,56)
White = (255,255,255)
Blue = (0, 0, 255)
#Link tile with color
TileColor = {D : Brown, G : Green, W : White}

map1 =[[G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,G,G,D,G,G,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,G,D,W,D,G,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,D,D,D,D,D,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,D,D,D,G,D,D,D,G,G,G,G,G,G],
        [G,G,G,G,G,D,D,D,G,G,G,D,D,D,G,G,G,G,G],
        [G,G,G,G,D,D,D,G,G,G,G,G,D,D,D,G,G,G,G],
        [G,G,G,D,D,D,G,G,G,G,G,G,G,D,D,D,G,G,G],
        [G,G,D,W,D,G,G,G,D,W,D,G,G,G,D,W,D,G,G],
        [G,G,G,D,D,D,G,G,G,G,G,G,G,D,D,D,G,G,G],
        [G,G,G,G,D,D,D,G,G,G,G,G,D,D,D,G,G,G,G],
        [G,G,G,G,G,D,D,D,G,G,G,D,D,D,G,G,G,G,G],
        [G,G,G,G,G,G,D,D,D,G,D,D,D,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,D,D,D,D,D,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,G,D,W,D,G,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,D,D,D,D,D,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,G,D,D,D,G,G,G,G,G,G,G,G],
        [G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G],]

#Creating map size
Tilesize = 32
Width = 19
Hieght = 19

#Game Display
Display = pg.display.set_mode((Width*Tilesize,Hieght*Tilesize))

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12

