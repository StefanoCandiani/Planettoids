"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - 12/06/2023
Project: Project 4, "Planettoids"
Group Game: "Blazing Glory"
File: bullet_class
"""
import pygame
import math
from math_functions import *

class Bullet():
    def __init__(self, screen,  x_coord, y_coord, angle, radius=3):
        '''Initializes the bullet's physics variables and other object variables'''
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.angle = angle
        self.radius = radius
        self.screen = screen
        self.sped = 5
        self.bullet_velo = (0, 0)
        return

    def frame(self, screen_width, screen_height):
        '''This function applies the physics calculations to the bullet for one game tick (iteration of the game loop).'''
        # Calculate the horizontal and vertical components of the velocity and insert them into a vector
        self.bullet_velo = tuple_adder([self.bullet_velo, (self.sped * math.cos(self.angle), self.sped * math.sin(self.angle))])

        # Cap the velocity at 10
        if tuple_mag(self.bullet_velo) > self.sped:
            self.bullet_velo = tuple_scaler(self.bullet_velo, (10 / tuple_mag(self.bullet_velo)))

        # Apply the velocity vector to the position values
        self.angle = angle_rebounder(self.angle)
        self.x_coord, self.y_coord = tuple_adder([self.get_coords(), self.bullet_velo])

        # Wrap the bullet when it passes the screen border
        if self.x_coord < 0:
            self.x_coord = screen_width
        if self.x_coord > screen_width:
            self.x_coord = 0
        if self.y_coord < 0:
            self.y_coord = screen_height
        if self.y_coord > screen_height:
            self.y_coord = 0
        return

    def draw_bullet(self):
        '''This function draws the bullet as a white circle of self.radius and at it's current center coordinate.'''
        pygame.draw.circle(self.screen, 'white', (self.x_coord, self.y_coord), self.radius)

    def get_angle(self):
        '''Returns the bullet's trajectory angle'''
        return self.angle

    def get_rad(self):
        '''Returns the bullet's radius'''
        return self.radius

    def get_coords(self):
        '''Returns the bullet's center coordinates as a tuple'''
        return (self.x_coord, self.y_coord)