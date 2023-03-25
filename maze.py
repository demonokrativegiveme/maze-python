import pygame as pg
from random import randint
pg.init()
tiles=25
window=pg.display.set_mode((tiles*40,tiles*29))
pg.display.set_caption('Maze')
class Game_sprite():
    def __init__(self,image,x,y,w,h,speed):
        self.image=pg.transform.scale(pg.image.load(image),(w,h))
        self.w=w
        self.h=h
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Game_sprite):
    def control(self,walls):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x-=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x+=self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x+=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x-=self.speed
        if keys[pg.K_UP]:
            self.rect.y-=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y+=self.speed
        if keys[pg.K_DOWN]:
            self.rect.y+=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y-=self.speed
class Wall(Game_sprite):
    pass    
class Enemy(Game_sprite):
    def __init__(self, image, x, y, w, h, speed, direction):
        super().__init__(image, x, y, w, h, speed)
        self.direction=direction
    def move(self,walls):
        if self.direction == 1:
            self.rect.x+=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.direction=2
        if self.direction == 2:
            self.rect.x-=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.direction=1
list_wall =['1111111111111111111111111111111111111111',
'0000000000000000000000000000000000000111',
'0000000000000000000000000000000000000111',
'1111111001110011111111111111111111100111',
'1111111001110011100000000000000000000111',
'1110011001110011100000000000000000000111',
'1110011001110011100111111111111111100111',
'1110000001110011100110000000110000000111',
'1110000001110011100110000000110000000111',
'1111111111110011100110011100110011100111',
'1110000000000011100110011100000011100111',
'1110000000000011100110011100000011100111',
'1110011111111111100110011111111111100111',
'1110011111111111100110011111111111100111',
'1110000000000000000110000000000000000111',
'1110000000000000000110000000000000000111',
'1111111111001111111110011111111111111111',
'1111111111001111111110011111111111111111',
'1100000000000000000000000000000000000111',
'1100000000000000000000000000000000000111',
'1100111111111111111111111111111111100111',
'1100111111111111111111111111111111100111',
'1100000000000000000000000000000000000111',
'1100000000000000000000000000000000000111',
'1111111100111111111111111111111111111111',
'1111111100111111111111111111111111111111',
'1111111100000000000000000000000000000001',
'1111111100000000000000000000000000000001',
'1111111111111111111111111111111111111111']
walls=[]
floors=[]
for i in range(len(list_wall)):
    for g in range(len(list_wall[i])):
        if list_wall[i][g] == '1':
            walls.append(Game_sprite('image/pixel.png',g*tiles,i*tiles,tiles,tiles,0))
        if list_wall[i][g] == '0':
            floors.append(Game_sprite('image/floor.png',g*tiles,i*tiles,tiles,tiles,0))
player=Player('image/hero.png',1*tiles,2*tiles,tiles,tiles,tiles/5)
final=Game_sprite('image/lastreward.png',37*tiles,27*tiles,tiles,tiles,tiles/5)
enemy1=Enemy('image/invisibletrap.png',3*tiles,21*tiles,tiles,tiles,tiles/50,1)
enemy3=Enemy('image/invisibletrap.png',36*tiles,6*tiles,tiles,tiles,tiles/50,1)
enemy4=Enemy('image/invisibletrap.png',12*tiles,11*tiles,tiles,tiles,tiles/50,1)
invisibletrap=Enemy('image/invisibletrap.png',4*tiles,6*tiles,tiles,tiles,tiles/50,1)
enemy5=Enemy('image/invisibletrap.png',23*tiles,27*tiles,tiles,tiles,tiles/50,1)
enemies=[enemy1,enemy3,invisibletrap,enemy4,enemy5]
game=True
lose=Game_sprite('image/lose.png',0,0,40*tiles,29*tiles,0)
win=Game_sprite('image/victory.png',0,0,40*tiles,29*tiles,0)
end=0
while game:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type==pg.QUIT:
            game=False
    for i in walls:
        i.reset()
    for i in floors:
        i.reset()
    player.reset()
    player.control(walls)
    final.reset()
    for i in enemies:
        i.reset()
        i.move(walls)
        if pg.sprite.collide_rect(player,i):
            end = 1
            game=False
    if pg.sprite.collide_rect(player,final):
        end=2
        game=False
    pg.display.flip()
if end == 1:
    gameover=lose
else:
    gameover=win
game=True
while game:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type==pg.QUIT:
            game=False
    gameover.reset()
    pg.display.flip()
