import pygame, sys
import random
import math
from pygame import mixer

# Initialize  pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("background.png")

mixer.music.load("caves.mp3")
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Cybersquare - Space invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Player spaceship
playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64, 128))
playerX = 370
playerY = 480
playerX_change = 0

# Player enemy
enemyImg = []
enemyX = []
enemyY =[]
enemyX_change = []
enemyY_change = [] 
for i in range (6):
    enemyImg.append(pygame.image.load("enemy11.png",))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(100,200))
    enemyX_change.append(5)
    enemyY_change.append(30)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10 #Speed of the bullet
bullet_state = "ready" # Ready - Can't see bullet, Fire - Bullet is moving

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    display_score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(display_score, (x,y))

def player(x, y):
    screen.blit(playerImg,(x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x, y))

def fire_bullet(x, y): # Movement of bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))

def fire_bullet(x, y): # Movement of bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

def game_over():
    over_text=over_font.render("GAME OVER", True,(255,255,255))
    screen.blit(over_text,(200,250))

running = True
while running:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                print ("Left key is pressed")
                playerX_change = -5

            if event.key == pygame.K_d:
                print ("Right key is pressed")
                playerX_change = 5

            if event.key == pygame.K_w:
                print ("Shoot key is pressed")
                if bullet_state == "ready":
                  bulletX = playerX
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                print ("Keystroke has been released")
                playerX_change = 0
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    for i in range(6):
        if enemyY[i]>440:
            for j in range(6):
                enemyY[j] = 2000
            game_over
            break
        if enemyX[i] < 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
             bulletY = 480
             bullet_state = "ready"
             score += 1
             print (score)
             enemyX[i] = random.randint(0, 735)
             enemyY[i] = random.randint(100, 200)
        enemy(enemyX[i], enemyY[i], i)
    show_score(textX, textY)      
    player(playerX,playerY)
   
    pygame.display.update()


            
