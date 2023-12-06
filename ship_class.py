"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - 12/06/2023
Project: Project 4, "Planettoids"
Group Game: "Blazing Glory"
File: ship_class
"""
import pygame
import math
from math_functions import *

class ship():
    def __init__(self,center_x=0,center_y=0,poly_mesh=[[(0,0),(1,0),(0,1)]],poly_scale=20,ship_angle=0,ship_color=(0xFF,0xFF,0xFF),thrust_color=(0xFF,0x9F,0x00),thruster_mesh=[[(-0.5,0),(-1,0),(((-math.sqrt(2)/2 + 0.5)/2)-0.5,math.sqrt(2)/4)],[(-0.5,0),(-1,0),(((-math.sqrt(2)/2 + 0.5)/2)-0.5,-math.sqrt(2)/4)]]):
        '''Initializes the ship's position, meshes, and other variables tied to further calculations.'''
        #Physics related
        self.ship_center_x = center_x
        self.ship_center_y = center_y
        self.ship_angle = ship_angle
        self.ship_velocity = (0,0)
        self.thrust_coefficient = 0.5
        self.friction_coefficient = 0.025
        #Mesh and drawing related
        self.mesh_scale = poly_scale
        self.ship_color = ship_color
        self.thrust_color = thrust_color
        self.draw_thruster = False
        self.base_mesh = poly_mesh
        self.transform_mesh = [[j for j in i] for i in self.base_mesh]
        self.translate_mesh = [[j for j in i] for i in self.base_mesh]
        self.thruster_mesh = thruster_mesh
        self.thruster_transform_mesh = [[j for j in i] for i in self.thruster_mesh]
        self.thruster_translate_mesh = [[j for j in i] for i in self.thruster_mesh]
        return

    def get_rotate_mesh(self): #Returns the rotated mesh
        '''Returns the ship's rotated mesh which is dependent on any previous calculations done by the frame() method.'''
        return self.transform_mesh

    def get_final_mesh(self): #Returns the translated rotated mesh
        '''Returns the ship's base mesh'''
        return self.translate_mesh
    
    def get_ship_coords(self): #Returns the ship's centerpoint coordinates respective to the game screen
        '''Returns the location (center point) tuple of the ship'''
        return (self.ship_center_x,self.ship_center_y)
    
    def get_mesh_scaler(self):
        '''Returns the mesh scalar of the ship'''
        return self.mesh_scale
    
    def get_ship_angle(self):
        '''Returns the ship's orientation angle'''
        return self.ship_angle

    def get_ship_color(self):
        '''Returns the ship's RGB color as a tuple'''
        return self.ship_color

    def frame(self,button,screen_width,screen_height):
        '''This function applies the physics calculations to the ship and transforms the mesh (including the thruster flame mesh) for one game tick (iteration of the game loop).'''
        #Check steering
        if button[pygame.K_LEFT]:
            self.ship_angle += -math.pi/25
        if button[pygame.K_RIGHT]:
            self.ship_angle += math.pi/25
        self.ship_angle = angle_rebounder(self.ship_angle)

        #Apply friction
        self.ship_velocity = tuple_adder([self.ship_velocity,tuple_scaler(linear_rotate_transform(self.ship_velocity,math.pi),self.friction_coefficient)])            
        
        #Apply Thrust
        if button[pygame.K_UP]:
            self.ship_velocity = tuple_adder([self.ship_velocity,(self.thrust_coefficient*math.cos(self.ship_angle),self.thrust_coefficient*math.sin(self.ship_angle))])
            self.draw_thruster = True #Enable the rendering of the thruster flame while up is being pressed
        else:
            self.draw_thruster = False #Disable the rendering of the thruster flame whenever up isn't pressed

        #Cap the velocity at a magnitude of 10
        if tuple_mag(self.ship_velocity) > 10:
            self.ship_velocity = tuple_scaler(self.ship_velocity,(10/tuple_mag(self.ship_velocity)))

        #Apply velocities to the position coordinates
        self.ship_center_x,self.ship_center_y = tuple_adder([self.get_ship_coords(),self.ship_velocity])

        # Wrap ship when it passes the screen border
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
        #Rotate thruster mesh and store to thruster transform mesh
        for individual_polygon_index in range(0, len(self.thruster_mesh)):  # individual_polygon in polygon_structure:
            for point_index in range(0, len(self.thruster_mesh[individual_polygon_index])):
                self.thruster_transform_mesh[individual_polygon_index][point_index] = tuple_scaler(
                    linear_rotate_transform(self.thruster_mesh[individual_polygon_index][point_index], self.ship_angle),
                    self.mesh_scale)
        return

    def draw_ship(self,screen,color_tuple,light_source_tuple,location_tuple): #Given the screen, the color of the ship, light source location, and desired screen location, this function draws the ship to the screen with all the necessary light, color, and location calculations.        
        '''This function draws the ship's rotated and translated mesh onto the screen. The rotation is dependent on the ship's orientation, and the translation is dependent on the location_tuple input. The function also draws the ships thruster flame using an internal boolean flag that is calculated during any call to the frame() method. (The thruster flame has a seperate mesh but still uses the ship angle and location_tuple input)'''
        #Move(translate) transform mesh to the input location coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)): #Loop through the transform mesh translating and drawing each of the polygons one at a time
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])): #Fill in the translate_mesh with the custom-location-translated version of that polygon in the transform_mesh
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                    location_tuple])
        #Move(translate) thruster transform mesh to the input location coordinates and store to thruster translate mesh
        for individual_polygon_index in range(0, len(self.thruster_transform_mesh)): #Loop through the transform mesh translating and drawing each of the polygons one at a time
            for point_index in range(0, len(self.thruster_transform_mesh[individual_polygon_index])): #Fill in the translate_mesh with the custom-location-translated version of that polygon in the transform_mesh
                self.thruster_translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.thruster_transform_mesh[individual_polygon_index][point_index],
                    location_tuple])
        
        #Loop through and draw each of the polygons in the translate_mesh with the appropriate light calculations
        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),self.translate_mesh[single_polygon_index])
        #Loop through and draw each of the polygons in the thruster_translate_mesh with the appropriate light calculations
        if self.draw_thruster == True:
            for single_polygon_index in range(0,len(self.thruster_translate_mesh)):
                pygame.draw.polygon(screen,(self.thrust_color[0],self.thrust_color[1]*light_multiplier_calculator(tuple_scaler(tuple_adder(self.thruster_transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple),self.thrust_color[2]),self.thruster_translate_mesh[single_polygon_index])
        return