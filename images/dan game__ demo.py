import pygame
from pygame.locals import*
import random,time,sys
pygame.init()
collided=False
score=0
last_tick=pygame.time.get_ticks()
FPS=60
FramePerSec=pygame.time.Clock()
RED=(255,0,0)
WHITE=(255,255,255)
screen=pygame.display.set_mode((900,700))
pygame.display.set_caption("catch and win")
bg=pygame.image.load("bg1.png")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    pygame.display.update()
