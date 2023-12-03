"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: bullet_class
"""
import pygame
import math
from math_functions import *

class Bullet():
    def __init__(self, screen,  x_coord, y_coord, angle, radius=3):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.angle = angle
        self.radius = radius
        self.screen = screen
        self.sped = 5
        self.bullet_velo = (0, 0)

    def frame(self, screen_width, screen_height):
        # 'Vector' the velocity
        self.bullet_velo = tuple_adder([self.bullet_velo, (self.sped * math.cos(self.angle), self.sped * math.sin(self.angle))])

        # Apply velo
        self.angle = angle_rebounder(self.angle)
        self.x_coord, self.y_coord = tuple_adder([self.get_coords(), self.bullet_velo])

        # Cap velo
        if tuple_mag(self.bullet_velo) > self.sped:
            self.bullet_velo = tuple_scaler(self.bullet_velo, (10 / tuple_mag(self.bullet_velo)))

        if self.x_coord < 0:
            self.x_coord = screen_width
        if self.x_coord > screen_width:
            self.x_coord = 0
        if self.y_coord < 0:
            self.y_coord = screen_height
        if self.y_coord > screen_height:
            self.y_coord = 0
        pass

    def draw_bullet(self):
        pygame.draw.circle(self.screen, 'white', (self.x_coord, self.y_coord), self.radius)

    def get_rad(self):
        return self.radius

    def get_coords(self):
        return (self.x_coord, self.y_coord)