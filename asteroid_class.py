import pygame
from math_functions import *

class Asteroid():

    def __init__(self, center_x=0, center_y=0, v_x=0.75, v_y=1.0, mesh=[[(0,0),(1,0),(0,1)]], scale=50):
        self.center_x = center_x
        self.center_y = center_y
        self.vel_x = v_x
        self.vel_y = v_y
        self.mesh = mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]
        self.mesh_scale = scale

    def get_coords(self):
        return (self.center_x, self.center_y)

    def get_mesh_scaler(self):
        return self.mesh_scale

    def set_velocity(self, new_vel_x, new_vel_y):
        self.vel_x = new_vel_x
        self.vel_y = new_vel_y

    # Changes asteroid mesh if needed
    def set_asteroid_mesh(self,new_mesh):
        self.mesh = new_mesh
        self.transform_mesh = [[j for j in i] for i in self.mesh]
        self.translate_mesh = [[j for j in i] for i in self.mesh]

    def frame(self, screen_width, screen_height):
        self.center_x += self.vel_x
        self.center_y += self.vel_y
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

        #Move(translate) transform mesh to the asteroid coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     (location_tuple)])

        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple,light_source_tuple)),self.translate_mesh[single_polygon_index])