import pygame
import time
import random


class SpaceShip:
    def __init__(self):
        self.x = 320
        self.y = 650

    def move_left(self):
        if(self.x >= 160):
            self.x = self.x - 80

    def move_right(self):
        if(self.x < 720):
            self.x = self.x + 80

    def On_Screen(self, display, Ship):
        display.blit(Ship, (self.x, self.y))

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x
