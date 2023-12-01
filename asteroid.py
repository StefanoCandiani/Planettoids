import pygame
from ship_light import tuple_scaler, tuple_adder, light_multiplier_calculator
import random

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

    def get_ast_coords(self):
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

        #Move(translate) transform mesh to the asteroid coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     (self.center_x, self.center_y)])

    def draw_asteroid(self, screen, color_tuple, light_source_tuple, location_tuple):
        for single_polygon_index in range(0,len(self.translate_mesh)):
            pygame.draw.polygon(screen,tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),self.translate_mesh[single_polygon_index])

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
                [(0.0, 1.0), (0.5, 1.0), (0.0, 0.0)],
                [(0.5, 1.0), (0.8, 0.4), (0.0, 0.0)],
                [(0.8, 0.4), (0.4, 0.0), (0.0, 0.0)],
                [(0.4, 0.0), (0.4, -0.4), (0.0, 0.0)],
                [(0.4, -0.4), (0.0, -1.0), (0.0, 0.0)],
                [(0.0, -1.0), (-0.4, -1.0), (0.0, 0.0)],
                [(-0.4, -1.0), (-0.5, -0.2), (0.0, 0.0)],
                [(-0.5, -0.2), (-0.3, 0.0), (0.0, 0.0)],
                [(-0.3, 0.0), (0.0, 1.0), (0.0, 0.0)]
            ],
            [
                [(-0.1, 0.8), (0.4, 1.0), (0.0, 0.0)],
                [(0.4, 1.0), (0.6, 0.35), (0.0, 0.0)],
                [(0.4, 1.0), (1.0, 0.6), (0.6, 0.35)],
                [(0.6, 0.35), (1.0, -0.25), (0.0, 0.0)],
                [(1.0, -0.25), (0.7, -0.65), (0.0, 0.0)],
                [(0.7, -0.65), (0.2, -0.8), (0.0, 0.0)],
                [(0.2, -0.8), (-0.1, -0.9), (0.0, 0.0)],
                [(-0.1, -0.9), (-0.5, -0.85), (0.0, 0.0)],
                [(-0.5, -0.85), (-0.85, -0.5), (0.0, 0.0)],
                [(-0.85, -0.5), (-0.7, 0.1), (0.0, 0.0)],
                [(-0.7, 0.1), (-1.0, 0.5), (0.0, 0.0)],
                [(-1.0, 0.5), (-0.5, 1.0), (0.0, 0.0)],
                [(-0.5, 1.0), (-0.1, 0.8), (0.0, 0.0)]
            ],
            [
                [(0.0, 1.0), (0.65, 0.65), (0.05, 0.5)],
                [(0.65, 0.65), (1.0, 0.0), (0.05, 0.5)],
                [(0.05, 0.5), (1.0, 0.0), (0.0, 0.0)],
                [(1.0, 0.0), (0.65, -0.65), (0.0, 0.0)],
                [(0.65, -0.65), (0.25, -0.85), (0.0, 0.0)],
                [(0.25, -0.85), (-0.5, -0.7), (0.0, 0.0)],
                [(-0.5, -0.7), (-0.65, -0.45), (0.0, 0.0)],
                [(-0.65, -0.45), (-0.4, -0.15), (0.0, 0.0)],
                [(-0.4, -0.15), (-1.0, 0.0), (-0.3, 0.6)],
                [(-0.4, -0.15), (-0.3, 0.6), (0.0, 0.0)],
                [(-0.3, 0.6), (0.05, 0.5), (0.0, 0.0)]
            ]
            # Asteroid Mesh to implement
            # [
            #     [(0.5, 0.5), (-0.5, 0.5), (0, 0)],
            #     [(-0.5, 0.5), (-1, 0), (0, 0)],
            #     [(-1, 0), (-0.5, -0.25), (0, 0)],
            #     [(-0.5, -0.25), (-0.4, -0.6), (0, 0)],
            #     [(-0.4, -0.6), (0.4, -0.6), (0, 0)],
            #     [(0.4, -0.6), (0.5, -0.25), (0, 0)],
            #     [(0.5, -0.25), (1, 0), (0, 0)],
            #     [(1, 0), (0.5, 0.5), (0, 0)],
            # ]
        ]

    #Selects one asteroid from possible asteroids and scales size using tuple_scaler()
    selected_asteroids = []
    for h in range(len(large_asteroid_meshes)):
        mesh = large_asteroid_meshes[h]
        selected_asteroids.append(large_asteroid_meshes[h])
        # random.randint(0,2)

    #Asteroid Instantiation
    asteroid_list = []
    for i in range(len(selected_asteroids)):
        asteroid_list.append(Asteroid(random.randint(0,screen_width),random.randint(0,screen_height), random.random(), random.random(), selected_asteroids[i]))

#Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        button = pygame.key.get_pressed()

        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
            running = False
            continue

        for asteroid in asteroid_list:
            asteroid.frame(screen_width, screen_height)

    #Draw Operations
        screen.blit(bg,(0,0))
        screen.blit(text_surface, text_surface_rect)
        # Draw Asteroid
        for asteroid in asteroid_list:
            asteroid.draw_asteroid(screen,(128,128,128),(light_source_x, light_source_y),asteroid.get_ast_coords())
            center = asteroid.get_ast_coords()
            ship_max_dist = asteroid.get_mesh_scaler()

    #Handles all of the soft screen wrapping
        for asteroid in asteroid_list:
            if center[0] + ship_max_dist > screen_width:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y), ((center[0] - screen_width), center[1]))
                # asteroid.set_velocity(random.random(), random.random())
            if center[0] - ship_max_dist < 0:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y), ((center[0] + screen_width), center[1]))
                # asteroid.set_velocity(random.random()*-1, random.random())
            if center[1] + ship_max_dist > screen_height:
                asteroid.draw_asteroid(screen, (128,128,128), (light_source_x, light_source_y), (center[0], (center[1] - screen_height)))
                # asteroid.set_velocity(random.random(), random.random())
            if center[1] - ship_max_dist < 0:
                asteroid.draw_asteroid(screen, (128,128,128), (light_source_x, light_source_y), (center[0], (center[1] + screen_height)))
                # asteroid.set_velocity(random.random(), random.random() * -1)

        pygame.time.Clock().tick(160)
        pygame.display.flip()


if __name__ == '__main__':
    main()
