import pygame
from math_functions import *

class Asteroid():

    def __init__(self, center_x=0, center_y=0, v_x=0.75, v_y=1.0, mesh=[[(0,0),(1,0),(0,1)]], scale=50, asteroid_color=(128, 128, 128)):
        # Variable Initializer
        self.center_x = center_x
        self.center_y = center_y
        self.vel_x = v_x
        self.vel_y = v_y
        self.mesh = mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]
        self.mesh_scale = scale
        self.asteroid_color = asteroid_color

    def get_coords(self):
        # Returns location tuple of asteroid
        return (self.center_x, self.center_y)

    def get_mesh_scaler(self):
        # Returns mesh scaler of asteroid
        return self.mesh_scale
    
    def get_asteroid_color(self):
        return self.asteroid_color

    def set_velocity(self, new_vel_x, new_vel_y):
        # Changes velocity
        self.vel_x = new_vel_x
        self.vel_y = new_vel_y

    def set_asteroid_mesh(self,new_mesh):
        # Changes asteroid mesh
        self.mesh = new_mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]

    def frame(self, screen_width, screen_height):
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

    def draw_asteroid(self, screen, color_tuple, light_source_tuple, location_tuple):

        # Move(translate) transform mesh to the asteroid coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     location_tuple])

        # Display individual polygons based on location tuple, light source, etc.
        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple,light_source_tuple)),self.translate_mesh[single_polygon_index])