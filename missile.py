import pygame
import time
import random
import sys
import math
laser = pygame.image.load("laser.png")
laser2 = pygame.image.load("laser2.jpg")


class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Status = True

    def get_status(self):
        return self.Status


class SimpleMissile (Missile):
    def __init__(self, x, y):
        super(SimpleMissile, self).__init__(x, y)

    def hitAlien(self, listofallaliens):
        for alien in listofallaliens:
            if alien.get_x() == self.x and alien.get_status() and alien.get_y() >= self.y:
                alien.dead()
                self.Status = False

    def move_up(self):
        if self.Status:
            self.y = self.y - (7)
        if self.y < 60:
            self.Status = False

    def On_Screen(self, display):
        if self.Status:
            display.blit(laser2, (self.x + 20, self.y))


class SpecialMissile (Missile):

    def __init__(self, x, y):
        super(SpecialMissile, self).__init__(x, y)

    def hitAlien(self, listofallaliens):
        for alien in listofallaliens:

            if alien.get_x() == self.x and alien.get_y() >= self.y and alien.get_status():
                self.Status = False
                if alien.get_typehit() == 0:
                    alien.specialhit()

    def move_up(self):
        if self.Status:
            self.y = self.y - (14)
        if self.y < 60:
            self.Status = False

    def On_Screen(self, display):
        if self.Status:
            display.blit(laser, (self.x + 20, self.y))
            print(self.x)
            print(self.y)
