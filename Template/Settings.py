TITLE = "The Baseball Game"

"""
Tilesize = 32
WIDTH = 19
HEIGHT = 19
"""

WIDTH = 608
HEIGHT = 608
Tilesize = 32
FPS = 60

# Player properties
PLAYER_ACC = 32
PLAYER_FRICTION = -0.12

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


D = 0 #dirt
G = 1 #grass
W = 2 #white

Brown = (115,118,83)
Green = (96,128,56)
White = (255,255,255)
TileColor = {D : Brown, G : Green, W : White}

MAP = [[G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G],
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