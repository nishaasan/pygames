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
bg=pygame.image.load('/Users/musthak/Desktop/pygamefolder/back.png')
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.index=0
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/dan-a.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/dan-b.png"))
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
class Friend (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/balloon1.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/balloon2.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/balloon3.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/apple.png"))
        self.image=self.images[1]
        self.surf=pygame.Surface((30,65))
        self.rect=self.surf.get_rect(center=(random.randint(40,900),0))
        self.size=self.image.get_size()
    def move(self):
        self.rect.move_ip(0,5)

    def draw(self,surface):
        pygame.draw.rect(surface,RED,self.rect,2)
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0.2),int(self.size[1]*0.2)))
        surface.blit(self.image,self.rect)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.index=0
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/space_ship1.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/space_ship2.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/space_ship3.png"))
        self.images.append(pygame.image.load("/Users/musthak/Desktop/pygamefolder/space_ship4.png"))
        self.image=self.images[0]
        self.surf=pygame.Surface((50,65))
        self.rect=self.surf.get_rect(center=(random.randint(40,900),0))
        self.size=self.image.get_size()
    def move(self):
        global collided
        self.rect.move_ip(0,5)
        self.image=self.images[self.index]
        if self.index<3:
            self.index+=1
        else:
          self.index=0
        if self.rect.bottom>600 or collided:
            self.rect.top=0
            self.rect.center=(random.randint(40,850),0)
    def draw(self,surface):
        pygame.draw.rect(surface,RED,self.rect,2)
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0,2),int(self.size[1]*0.2)))
        surface.blit(self.image,self.rect)

p1=player()
f1=Friend()
e1=Enemy()
enemies=pygame.sprite.Group()
enemies.add(e1)
friends=pygame.sprite.Group()
friends.add(f1)
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    if not collided:
        e1.move()
        p1.update()
    p1.draw(screen)
    now=pygame.time.get_ticks()
   # print(now)
    if now-last_tick>1000:
        last_tick=pygame.time.get_ticks()
       # print(last_tick)
        new_friend=Friend()
        new_friend.image=new_friend.images[random.randint(0,3)]
        friends.add(new_friend)
    for friend in friends:
        friend.draw(screen)
        friend.move()
        if friend.rect.top>700:
            friends.remove(friend)
            del friend
            hit_friend=pygame.sprite.spritecollideany(p1,friends)
            if hit_friend:
                friends.remove(hit_friend)
                del hit_friend
                Score+=1
    if pygame.sprite.spritecollideany(p1,enemies):
       bg=pygame.image.load('/Users/musthak/Desktop/pygamefolder/bg2.png')
       collided=True

       e1.draw(screen)

    pygame.display.update()
    FramesPerSec.tick(FPS)
