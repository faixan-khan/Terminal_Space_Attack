import pygame
import time
import random
import sys
from enemy import *
from missile import *
from spaceship import *
pygame.init()
width = 900
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Kai Invaders')
Ship = pygame.image.load('ship.jpg')
Enemy = pygame.image.load("enemy_1.jpg")
EnemyHit = pygame.image.load("laser.jpg")
white = (255, 255, 255)
Red = (255, 0, 0)
Lime = (0, 255, 0)
Blue = (0, 0, 255)
clock = pygame.time.Clock()

DeathStar = SpaceShip()
MissilesList = []
enemyList = []

# drawing the outline of the board area


def drawborder(display):
    display.fill((0, 0, 0))
    pygame.draw.line(display, [140, 255, 7], [70, 700], [70, 60], 2)
    pygame.draw.line(display, [140, 255, 7], [800, 700], [800, 60], 2)
    pygame.draw.line(display, [140, 255, 7], [70, 700], [800, 700], 2)
    pygame.draw.line(display, [140, 255, 7], [70, 60], [800, 60], 2)
    font = pygame.font.SysFont(None, 33)
    tex = font.render("Welcome to space Invaders", True, white)
    display.blit(tex, (300, 0))
    ins = font.render(
        "INSTRUCTIONS.....A->left::D->right::S->SpecialMissile::Space->NormalMissile",
        True,
        Blue)
    display.blit(ins, (50, 30))

# function to display the points of player outside the box


def score():
    font = pygame.font.SysFont(None, 33)
    text = font.render("Points : " + str(enemy.score), True, Lime)
    display.blit(text, (0, 0))


enemycreation = 0
# main game code
while True:
    pygame.display.update()
    drawborder(display)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_q
                )):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and (
                event.key == pygame.K_s
        ):

            MissilesList.append(
                SpecialMissile(DeathStar.get_x(), DeathStar.get_y() - 35))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                DeathStar.move_left()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                DeathStar.move_right()

        if event.type == pygame.KEYDOWN and (
                event.key == pygame.K_SPACE
        ):
            MissilesList.append(
                SimpleMissile(DeathStar.get_x(), DeathStar.get_y() - 35))

# self destruct
#  Creates a new enemy
# Removes enemy
# Draws missiles
# Removes missiles
    for al in enemyList:
        al.On_Screen(display, Enemy, EnemyHit)
        al.self_kill()

    if(time.time() >= enemycreation + 10):
        enemycreation = time.time()
        enemyList.append(enemy())
    for al in enemyList:
        if al.get_status() == False:
            enemyList.remove(al)
    for mi in MissilesList:
        mi.hitAlien(enemyList)
        mi.On_Screen(display)
        mi.move_up()
    if MissilesList and MissilesList[0].get_status() == False:
        MissilesList.pop(0)
    DeathStar.On_Screen(display, Ship)
    score()
    clock.tick(9)
