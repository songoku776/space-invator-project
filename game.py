import pygame
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_START_X = 370
PLAYER_START_Y = 480
PLAYER_SPEED_X = 5

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 3

COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 1")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def is_collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    return distance < COLLISION_DISTANCE

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED_X
            if event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED_X

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = ENEMY_SPEED_X
        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = -ENEMY_SPEED_X

        if is_collision(enemyX[i], enemyY[i], playerX, playerY):
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
