import pygame
import math
from ship_light import tuple_scaler, tuple_adder, light_multiplier_calculator
import random

class Asteroid():

    def __init__(self, center_x=0, center_y=0, v_x=0.75, v_y=1.0, mesh=[[(0,0),(1,0),(0,1)]], scale=50):
        self.a_center_x = center_x
        self.a_center_y = center_y
        self.vel_x = v_x
        self.vel_y = v_y
        self.a_mesh = mesh
        self.transform_mesh = [[j for j in i] for i in self.a_mesh]
        self.translate_mesh = [[j for j in i] for i in self.a_mesh]
        self.mesh_scale = scale

    def get_ast_coords(self):
        return (self.a_center_x, self.a_center_y)

    def get_mesh_scaler(self):
        return self.mesh_scale

    def set_velocity(self, new_vel_x, new_vel_y):
        self.vel_x = new_vel_x
        self.vel_y = new_vel_y

    def frame(self, screen_width, screen_height):
        self.a_center_x += self.vel_x
        self.a_center_y += self.vel_y
        if self.a_center_x < 0:
            self.a_center_x = screen_width
        if self.a_center_x > screen_width:
            self.a_center_x = 0
        if self.a_center_y < 0:
            self.a_center_y = screen_height
        if self.a_center_y > screen_height:
            self.a_center_y = 0

        #Move(translate) transform mesh to the ship coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     (self.a_center_x, self.a_center_y)])

    def draw_asteroid(self, screen, color_tuple, light_source_tuple, location_tuple):
        #Custom draw location
        if location_tuple != self.get_ast_coords():
            temp_translate_polygon = [(0,0),(0,0),(0,0)] #Create an empty polygon initialize the variable
            for single_polygon_index in range(0,len(self.transform_mesh)): #Loop through the transform mesh translating and drawing each of the polygons one at a time
                for point_index in range(0, len(self.transform_mesh[single_polygon_index])): #Fill in the temp_translate_polygon with the custom-location-translated version of that polygon in the transform_mesh
                    temp_translate_polygon[point_index] = tuple_adder([self.transform_mesh[single_polygon_index][point_index],location_tuple])
                pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),temp_translate_polygon)
        #Regular draw location same as ship location
        else:
            for single_polygon_index in range(0,len(self.translate_mesh)):
                pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),self.translate_mesh[single_polygon_index])
        return





def main():
    pygame.init() #Initialize game screen

#Initilaize Game Variables
    #Screen variables (Temporary)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Asteroids Test")
    bg = pygame.image.load("background1.png") #NOTE: For future implementation we should load these images into sprites to speed up the draw commands
    #Light Source Variables
    light_source_x = 345 #screen_width // 2
    light_source_y = 332 #screen_height // 2
    #Title text objects
    font_object_title = pygame.font.Font('AmazDooMLeft.ttf', 100)
    text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (screen_width // 2, screen_height // 5)
    #Initialize Asteroid Mesh List (Collection of Polygons organized in shape of asteroid)
    large_asteroid_meshes = [
        [
            [(0, 2), (1, 2), (0, 0)],
            [(1, 2), (1.6, 0.8), (0,0)],
            [(1.6, 0.8), (0.8, 0), (0, 0)],
            [(0.8, 0), (0.8, -0.8), (0, 0)],
            [(0.8, -0.8), (0, -2), (0, 0)],
            [(0, -2), (-0.8, -2), (0, 0)],
            [(-0.8, -2), (-1, -0.4), (0, 0)],
            [(-1, -0.4), (-0.6, 0), (0, 0)],
            [(-0.6, 0), (0, 2), (0, 0)]
        ],
        [
            [(-0.2,1.6),(0.8,2),(0,0)],
            [(0.8,2),(1.2,0.7),(0,0)],
            [(0.8,2),(2,1.2),(1.2,0.7)],
            [(1.2,0.7),(2,-0.5),(0,0)],
            [(2,-0.5),(1.4,-1.3),(0,0)],
            [(1.4,-1.3),(0.4,-1.6),(0,0)],
            [(0.4,-1.6), (-0.2,-1.8), (0,0)],
            [(-0.2,-1.8), (-1,-1.7), (0,0)],
            [(-1,-1.7), (-1.7,-1), (0,0)],
            [(-1.7,-1), (-1.4,0.2), (0,0)],
            [(-1.4,0.2), (-2,1), (0,0)],
            [(-2,1), (-1,2), (0,0)],
            [(-1,2), (-0.2,1.6), (0,0)]
        ],
        [
            [(0,2),(1.3,1.3),(0.1,1)],
            [(1.3,1.3),(2,0),(0.1,1)],
            [(0.1,1),(2,0),(0,0)],
            [(2,0),(1.3,-1.3),(0,0)],
            [(1.3,-1.3),(0.5,-1.7),(0,0)],
            [(0.5,-1.7), (-1,-1.4), (0,0)],
            [(-1,-1.4), (-1.3,-0.9), (0,0)],
            [(-1.3,-0.9), (-0.8,-0.3), (0,0)],
            [(-0.8,-0.3), (-2,0), (-0.6,1.2)],
            [(-0.8,-0.3), (-0.6,1.2), (0,0)],
            [(-0.6,1.2), (0.1,1), (0,0)],
        ]
    ]

    #Selects one asteroid from possible asteroids and scales size using tuple_scaler()
    selected_asteroid = large_asteroid_meshes[random.randint(0,len(large_asteroid_meshes)-1)]
    for i in range(len(selected_asteroid)):
        for j in range(len(selected_asteroid[i])):
            selected_asteroid[i][j] = tuple_scaler(selected_asteroid[i][j],25)

    v_x = random.random()
    v_y = random.random()

    #Asteroid Instantiation
    asteroid = Asteroid(400,300, v_x, v_y, selected_asteroid)

#Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        button = pygame.key.get_pressed()

        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
            running = False
            continue

        asteroid.frame(screen_width, screen_height)

    #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(bg,(0,0))
        screen.blit(text_surface, text_surface_rect)
        # Draw Ship
        asteroid.draw_asteroid(screen,(0,0,0xFF),(light_source_x, light_source_y),asteroid.get_ast_coords())

        center = asteroid.get_ast_coords()
        ship_max_dist = asteroid.get_mesh_scaler()

    # Handles all of the soft screen wrapping - might add a 4 corner solution if the ship is perfectly in a corner

        if center[0] + ship_max_dist > screen_width:
            asteroid.draw_asteroid(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] - screen_width), center[1]))
            v_x = random.randint(-2, 2) * 0.2140281490
        if center[0] - ship_max_dist < 0:
            asteroid.draw_asteroid(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] + screen_width), center[1]))
            v_x = random.randint(-2, 2) * 0.2140281490
        if center[1] + ship_max_dist > screen_height:
            asteroid.draw_asteroid(screen, (0, 0, 0xFF), (light_source_x, light_source_y), (center[0], (center[1] - screen_height)))
            v_y = random.randint(-2, 2) * 0.2140281490
        if center[1] - ship_max_dist < 0:
            asteroid.draw_asteroid(screen, (0, 0, 0xFF), (light_source_x, light_source_y), (center[0], (center[1] + screen_height)))
            v_y = random.randint(-2, 2) * 0.2140281490

        # FIXME: Make velocity change every time it screen-wraps
        # asteroid.set_velocity(v_x,v_y)

        pygame.display.flip()

if __name__ == '__main__':
    main()
