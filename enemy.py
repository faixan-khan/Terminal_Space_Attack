import pygame
import time
import random


class enemy:
    score = 0

    def __init__(self):
        self.x = random.randint(2, 9) * 80
        self.y = random.randint(1, 2) * 100
        self.creationtime = time.time()
        self.alive = True
        self.typehit = 0

    def self_kill(self):
        if time.time() - self.creationtime >= 8:
            self.alive = False

    def On_Screen(self, display, Enemy, EnemyHit):
        if self.alive:
            if self.typehit == 0:
                display.blit(Enemy, (self.x, self.y))
            else:
                display.blit(EnemyHit, (self.x, self.y))

    def dead(self):
        self.alive = False
        if self.typehit == 0:
            self.__class__.score = self.__class__.score + 1

    def specialhit(self):
        self.typehit = 1
        self.__class__.score = self.__class__.score + 1
        self.creationtime = time.time()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_status(self):
        return self.alive

    def get_typehit(self):
        return self.typehit
