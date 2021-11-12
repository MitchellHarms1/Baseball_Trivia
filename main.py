
import pygame as pg
import random
from Settings import *
from Sprite import *

class Game:
    def __init__(self):
       # initialize game window
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("The Baseball game")
        self.display = pg.display.set_mode((Width*Tilesize,Hieght*Tilesize)) #Tile size is 32
        self.running = True
        #self.clock = pg.time.Clock()
        #pygame.display.set_caption("The Baseball Game")
    def new(self):
        # resets game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()


    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            #self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw()
            
            
            
    def update(self):
        # game loop update
        self.all_sprites.update()
        
    def events(self):
        # game loop - events
            for event in pg.event.get():
            # check for closing window
             if event.type == pg.QUIT:
                if self.playing:
                     self.playing = False
                self.running = False

    def draw(self):
        # game loop - draw
        
            for row in range(Hieght):
        
                for col in range(Width):
                #print(map1[row -1][col])
                
                    pg.draw.rect(Display,TileColor[map1[row -1][col]], (col*Tilesize,row*Tilesize,Tilesize,Tilesize))   
        
            
            self.all_sprites.draw(self.display)
            #pg.display.flip()   
            pg.display.update() 

    def show_start_screen(self):
        # game start screen
        pass

    def show_go_screen(self):
        # game over screen
        pass 



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()

