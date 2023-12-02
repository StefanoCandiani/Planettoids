"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: main
"""
import pygame
import math
import random
from math_functions import *
from ship_class import ship
from userinterface_class import Legend
from asteroid_class import Asteroid

def main():
    pygame.init() #Initialize game screen

    #Initilaize Game Variables
    #Screen variables
    screen_width = 800#1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("assets/Planettoids Beta v1.1")
    bg = pygame.image.load("assets/background1.png") #NOTE: For future implementation we should load these images into sprites to speed up the draw commands
    #Light Source Variables
    light_source_x = 345 #screen_width // 2
    light_source_y = 332 #screen_height // 2
    #Title text objects
    font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
    text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (screen_width // 2, screen_height // 5)
    #Initialize Player Ship
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]
    player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh)
    #Initialize Asteroid List
    asteroid_meshes = [
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
        # Alien Mesh to implement
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
    asteroid_list = []

    for i in range(len(asteroid_meshes)):
        asteroid_list.append(
            Asteroid(random.randint(0, screen_width), random.randint(0, screen_height), random.random(),
                     random.random(), asteroid_meshes[i]))

    # Create the UI
    legend = Legend(screen, screen_width, screen_height)

    #Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        button = pygame.key.get_pressed()
        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
            running = False
            continue

        player_ship.frame(button,screen_width,screen_height)
        for asteroid in asteroid_list:
            asteroid.frame(screen_width, screen_height)

        #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(bg,(0,0,screen_width,screen_height))
        screen.blit(text_surface, text_surface_rect)

        # Draw Ship
        player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), player_ship.get_ship_coords())
        center = player_ship.get_ship_coords()
        ship_max_dist = player_ship.get_mesh_scaler()

        # Handles all the soft screen wrapping - might add a 4 corner solution if the ship is perfectly in a corner
        if center[0] + ship_max_dist > screen_width:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] - screen_width), center[1]))
        if center[0] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] + screen_width), center[1]))
        if center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), (center[0], (center[1] - screen_height)))
        if center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), (center[0], (center[1] + screen_height)))

        # Corner wrapping
        if center[0] + ship_max_dist > screen_width and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] - screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] + screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] + screen_width), (center[1] + screen_height)))
        if center[0] + ship_max_dist > screen_width and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), (light_source_x, light_source_y), ((center[0] - screen_width), (center[1] + screen_height)))

        # Draw asteroid and handle screen wrapping for asteroid
        for asteroid in asteroid_list:
            asteroid.draw_asteroid(screen, (128,128,128), (light_source_x, light_source_y), asteroid.get_coords())
            ast_center = asteroid.get_coords()
            asteroid_max_dist = asteroid.get_mesh_scaler()

            if ast_center[0] + asteroid_max_dist > screen_width:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y),((ast_center[0] - screen_width), ast_center[1]))
            if ast_center[0] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y),((ast_center[0] + screen_width), ast_center[1]))
            if ast_center[1] + asteroid_max_dist > screen_height:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y),(ast_center[0], (ast_center[1] - screen_height)))
            if ast_center[1] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, (128, 128, 128), (light_source_x, light_source_y),(ast_center[0], (ast_center[1] + screen_height)))

        legend.showLegend(screen)
        legend.keyLightUp(button)

        pygame.display.flip()


if __name__ == '__main__':
    main()