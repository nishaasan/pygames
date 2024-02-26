import pygame
from pygame.locals import *
import random,time,sys
pygame.init()
collided=False
Score=0
run=True
last_tick=pygame.time.get_ticks()
FPS=60
FramesPerSec=pygame.time.Clock()
RED=(255,0,0)
WHITE=(255,255,255)
screen=pygame.display.set_mode((900,700))
pygame.display.set_caption("Catch and Win")
bg=pygame.image.load("bg1.png")
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.index=0
        self.images.append(pygame.image.load("dan-a.png"))
        self.images.append(pygame.image.load("dan-b.png"))
        self.image=self.images[0]
        self.surf=pygame.Surface((70,100))
        self.rect=self.surf.get_rect(center=(50,500))
        self.size=self.image.get_size()
    def update(self):
        pressed_keys=pygame.key.get_pressed()
        if self.index:
            self.index=0
        else:
            self.index=1
        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
                self.image=self.images[self.index]
        if self.rect.right<900:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
                self.image=self.images[self.index]

    def draw(self,surface):
        pygame.draw.rect(surface,RED,self.rect,2)
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0.5),int(self.size[1]*0.5)))
        surface.blit(self.image,self.rect)
        

p1=player()
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    p1.update()
    p1.draw(screen)
    pygame.display.update()
    FramesPerSec.tick(FPS)
