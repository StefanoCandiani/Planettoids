"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - 12/06/2023
Project: Project 4, "Planettoids"
Group Game: "Blazing Glory"
File: asteroid_class
"""
import pygame
import math
from math_functions import *

class Asteroid():

    def __init__(self, center_x=0, center_y=0, trajectory_angle = 0, mesh=[[(0,0),(1,0),(0,1)]], asteroid_color=(128, 128, 128), size=2, scale=None, level_num = 0):
        '''Initializes the asteroid's position, calculates the velocity values using the size, level number, and trajectory angle, and sets up the mesh and corresponding variables.'''
        #Position and meshes
        self.center_x = center_x
        self.center_y = center_y
        self.mesh = mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]
        self.asteroid_color = asteroid_color
        #Set size values and appropriate mesh scalar
        if size == 3: #If the inputted size is three then this is a UFO and so gets special treatment
            self.asteroid_size = 0
        else:
            self.asteroid_size = size
        if scale != None:
            self.mesh_scale = scale #Allows for custom scales to override the base options
        else:
            scale_list = [12,25,50,30]
        self.mesh_scale = scale_list[size]
        #Calculate the velocity values
        velocity_ratios = [3,2,1,4] #These represent how each size scales with each other speed-wise
        difficulty_multipliers = [1,2,3,4,5,6,7,8,9,10] #These are difficulty multipliers for each level
        self.vel_x = math.cos(trajectory_angle)*(velocity_ratios[size]*difficulty_multipliers[level_num])
        self.vel_y = math.sin(trajectory_angle)*(velocity_ratios[size]*difficulty_multipliers[level_num])
        return

    def get_coords(self):
        '''Returns the location (center point) tuple of the asteroid'''
        return (self.center_x, self.center_y)

    def get_mesh_scaler(self):
        '''Returns the mesh scalar of the asteroid'''
        return self.mesh_scale
    
    def get_asteroid_color(self):
        '''Returns the asteroid's RGB color as a tuple'''
        return self.asteroid_color

    def get_asteroid_velo(self):
        '''Returns the asteroid's velocity values in a tuple'''
        return (self.vel_x, self.vel_y)

    def get_asteroid_mesh(self):
        '''Returns the asteroid's base mesh'''
        return self.mesh

    def get_asteroid_size(self):
        '''Returns the asteroid size value (0 = Small, 1 = Medium, 2 = Large)'''
        return self.asteroid_size

    def set_velocity(self, new_vel_x, new_vel_y):
        '''Changes the velocity variables to new_vel_x and new_vel_y'''
        self.vel_x = new_vel_x
        self.vel_y = new_vel_y

    def set_asteroid_mesh(self,new_mesh):
        '''Changes asteroid mesh to new_mesh'''
        self.mesh = new_mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]

    def frame(self, screen_width, screen_height):
        '''This function applies the physics calculations to the asteroid and transforms the mesh for one game tick (iteration of the game loop).'''
        # Changes position based on x and y velocities
        self.center_x += self.vel_x
        self.center_y += self.vel_y

        # Resets position if asteroid goes beyond screen
        if self.center_x < 0:
            self.center_x = screen_width
        if self.center_x > screen_width:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = screen_height
        if self.center_y > screen_height:
            self.center_y = 0

        # Scales base mesh and assigns to transform mesh variable
        for i in range(len(self.mesh)):
            for j in range(len(self.mesh[i])):
                self.transform_mesh[i][j] = tuple_scaler(self.mesh[i][j], self.mesh_scale)
        return

    def draw_asteroid(self, screen, color_tuple, light_source_tuple, location_tuple):
        '''This function draws the asteroid's rotated and translated mesh onto the screen. The rotation is dependent on the asteroid's orientation, and the translation is dependent on the location_tuple input.'''
        # Move(translate) transform mesh to the asteroid coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     location_tuple])

        # Display individual polygons based on location tuple, light source, etc.
        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple,light_source_tuple)),self.translate_mesh[single_polygon_index])
        return