"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: ship_class
"""
import pygame
import random
import math
from math_functions import *

class ship():
    def __init__(self,center_x=0,center_y=0,poly_mesh=[[(0,0),(1,0),(0,1)]],poly_scale=20,ship_angle=0):
        #Initialize Variables
        self.ship_center_x = center_x
        self.ship_center_y = center_y
        self.ship_angle = ship_angle
        self.base_mesh = poly_mesh
        self.transform_mesh = [[j for j in i] for i in self.base_mesh]
        self.translate_mesh = [[j for j in i] for i in self.base_mesh]
        self.mesh_scale = poly_scale
        self.ship_velocity = (0,0)
        self.thrust_coefficient = 0.75
        self.friction_coefficient = 0.025
        return

    def frame(self,button,screen_width,screen_height):
        #Check steering
        if button[pygame.K_LEFT]:
            self.ship_angle += -math.pi/25
        if button[pygame.K_RIGHT]:
            self.ship_angle += math.pi/25
        #Apply friction
        self.ship_velocity = tuple_adder([self.ship_velocity,tuple_scaler(linear_rotate_transform(self.ship_velocity,math.pi),self.friction_coefficient)])            
        #Apply Thrust
        if button[pygame.K_UP]:
            self.ship_velocity = tuple_adder([self.ship_velocity,(self.thrust_coefficient*math.cos(self.ship_angle),self.thrust_coefficient*math.sin(self.ship_angle))])
        #Bound velocity
        if tuple_mag(self.ship_velocity) > 10:
            self.ship_velocity = tuple_scaler(self.ship_velocity,(10/tuple_mag(self.ship_velocity)))
        #Apply velocities
        self.ship_angle = angle_rebounder(self.ship_angle)
        self.ship_center_x,self.ship_center_y = tuple_adder([self.get_ship_coords(),self.ship_velocity])

        # Wrap ship
        if self.ship_center_x < 0:
            self.ship_center_x = screen_width
        if self.ship_center_x > screen_width:
            self.ship_center_x = 0
        if self.ship_center_y < 0:
            self.ship_center_y = screen_height
        if self.ship_center_y > screen_height:
            self.ship_center_y = 0

        #Rotate base mesh and store to transform mesh
        for individual_polygon_index in range(0, len(self.base_mesh)):  # individual_polygon in polygon_structure:
            for point_index in range(0, len(self.base_mesh[individual_polygon_index])):
                self.transform_mesh[individual_polygon_index][point_index] = tuple_scaler(
                    linear_rotate_transform(self.base_mesh[individual_polygon_index][point_index], self.ship_angle),
                    self.mesh_scale)
        return

    def get_rotate_mesh(self): #Returns the rotated mesh
        return self.transform_mesh

    def get_final_mesh(self): #Returns the translated rotated mesh
        return self.translate_mesh
    
    def get_ship_coords(self): #Returns the ship's centerpoint coordinates respective to the game screen
        return (self.ship_center_x,self.ship_center_y)
    
    def get_mesh_scaler(self):
        return self.mesh_scale

    def draw_ship(self,screen,color_tuple,light_source_tuple,location_tuple): #Given the screen, the color of the ship, light source location, and desired screen location, this function draws the ship to the screen with all the necessary light, color, and location calculations.        
        #Move(translate) transform mesh to the ship coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)): #Loop through the transform mesh translating and drawing each of the polygons one at a time
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])): #Fill in the translate_mesh with the custom-location-translated version of that polygon in the transform_mesh
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                    location_tuple])
        #Loop through and draw each of the polygons in the translate_mesh with the appropriate light calculations
        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),self.translate_mesh[single_polygon_index])
        return