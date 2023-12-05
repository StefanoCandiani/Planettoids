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

    # NOTE: For future implementation we should load these images into sprites to speed up the draw commands
    background_list = [
        "assets/800x600/Lev1 800x600.png",
        "assets/800x600/Lev2 800x600.png",
        "assets/800x600/Lev3 800x600.png",
        "assets/800x600/Lev4 800x600.png",
        "assets/800x600/Lev5 800x600.png",
        "assets/800x600/Lev6 800x600.png",
        "assets/800x600/Lev7 800x600.png",
        "assets/800x600/Lev8 800x600.png",
        "assets/800x600/Lev9 800x600.png",
        "assets/800x600/Lev10 800x600.png"
    ]

    #Light Source Variables
    lightsource_list = [
        (800, 0),       # Level 1
        (800, 300),     # Level 2
        (0, 0),         # Level 3
        (276, 117),     # Level 4
        (410, 266),     # Level 5
        (612, 0),       # Level 6
        (28, 500),      # Level 7
        (470, 187),     # Level 8
        (345, 208),     # Level 9
        (345, 332)      # Level 10
    ]
    level_num = 0

    #Title text objects
    font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
    text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (screen_width // 2, screen_height // 5)
    #Initialize Player Ship
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]
    player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh)
    #Initialize asteroid mesh designs
    asteroid_meshes = [
        # Peanut
        [
            [(0, 1), (0.5, 1), (0.2, 0.3)],                 # 1
            [(0.8, 0.4), (0.5, 1), (0.2, 0.3)],             # 2
            [(0.8, 0.4), (0.4, 0.2), (0.2, 0.3)],           # 3
            [(0.1, -0.4), (0.4, 0.2), (0.2, 0.3)],          # 4
            [(0.1, -0.4), (0.4, 0.2), (0.4, -0.4)],         # 5
            [(0.1, -0.4), (0, -1), (0.4, -0.4)],            # 6
            [(0.1, -0.4), (0, -1), (-0.4, -1)],             # 7
            [(0.1, -0.4), (-0.1, -0.2), (-0.4, -1)],        # 8
            [(-0.5, -0.2), (-0.1, -0.2), (-0.4, -1)],       # 9
            [(-0.5, -0.2), (-0.1, -0.2), (-0.3, 0)],        # 10
            [(0.2, 0.3), (-0.1, -0.2), (-0.3, 0)],          # 11
            [(0.2, 0.3), (0, 1), (-0.3, 0)],                # 12
            [(0.2, 0.3), (-0.1, -0.2), (0.1, -0.4)],        # 13


            # Old mesh design
            # [(0.0, 1.0), (0.5, 1.0), (0.0, 0.0)],
            # [(0.5, 1.0), (0.8, 0.4), (0.0, 0.0)],
            # [(0.8, 0.4), (0.4, 0.0), (0.0, 0.0)],
            # [(0.4, 0.0), (0.4, -0.4), (0.0, 0.0)],
            # [(0.4, -0.4), (0.0, -1.0), (0.0, 0.0)],
            # [(0.0, -1.0), (-0.4, -1.0), (0.0, 0.0)],
            # [(-0.4, -1.0), (-0.5, -0.2), (0.0, 0.0)],
            # [(-0.5, -0.2), (-0.3, 0.0), (0.0, 0.0)],
            # [(-0.3, 0.0), (0.0, 1.0), (0.0, 0.0)]
        ],
        # Cookie
        [
            [(-0.5, 1), (-0.1, 0.8), (-0.25, 0.5)],         # 1
            [(-0.1, 0.8), (-0.25, 0.5), (0.6, 0.4)],        # 2
            [(-0.1, 0.8), (0.6, 0.4), (0.4, 1)],            # 3
            [(0.6, 0.4), (0.4, 1), (1, 0.6)],               # 4
            [(0.6, 0.4), (0.4, 0.1), (-0.25, 0.5)],         # 5
            [(-0.2, -0.3), (0.4, 0.1), (-0.25, 0.5)],       # 6
            [(0.6, 0.4), (0.4,0.1), (1, -0.25)],            # 7
            [(0.7, -0.6), (0.4,0.1), (1, -0.25)],           # 8
            [(0.7, -0.6), (0.4, 0.1), (0.2, -0.8)],         # 9
            [(-0.2, -0.3), (0.4, 0.1), (0.2, -0.8)],        # 10
            [(-0.2, -0.3), (-0.1, -0.8), (0.2, -0.8)],      # 11
            [(-0.2, -0.3), (-0.1, -0.8), (-0.5, -0.75)],    # 12
            [(-0.2, -0.3), (-0.5,-0.75), (-0.75, -0.5)],    # 13
            [(-0.2, -0.3), (-0.7, 0.1), (-0.75, -0.5)],     # 14
            [(-0.2, -0.3), (-0.7, 0.1), (-0.25, 0.5)],      # 15
            [(-1, 0.5), (-0.7, 0.1), (-0.25, 0.5)],         # 16
            [(-1, 0.5), (-0.5, 1), (-0.25, 0.5)]            # 17

            # Old mesh design
            # [(-0.1, 0.8), (0.4, 1.0), (0.0, 0.0)],
            # [(0.4, 1.0), (0.6, 0.35), (0.0, 0.0)],
            # [(0.4, 1.0), (1.0, 0.6), (0.6, 0.35)],
            # [(0.6, 0.35), (1.0, -0.25), (0.0, 0.0)],
            # [(1.0, -0.25), (0.7, -0.65), (0.0, 0.0)],
            # [(0.7, -0.65), (0.2, -0.8), (0.0, 0.0)],
            # [(0.2, -0.8), (-0.1, -0.9), (0.0, 0.0)],
            # [(-0.1, -0.9), (-0.5, -0.85), (0.0, 0.0)],
            # [(-0.5, -0.85), (-0.85, -0.5), (0.0, 0.0)],
            # [(-0.85, -0.5), (-0.7, 0.1), (0.0, 0.0)],
            # [(-0.7, 0.1), (-1.0, 0.5), (0.0, 0.0)],
            # [(-1.0, 0.5), (-0.5, 1.0), (0.0, 0.0)],
            # [(-0.5, 1.0), (-0.1, 0.8), (0.0, 0.0)]
        ],
        # Jester Hat
        [
            [(-1, 0), (-0.4, -0.2), (-0.3, 0.6)],       # 1
            [(-0.4, -0.2), (-0.3, 0.6), (0,0)],         # 2
            [(0,0), (-0.3,0.6), (0.05,0.5)],            # 3
            [(0.05,0.5), (0.7,0.7), (0,1)],             # 4
            [(0.05,0.5), (0.7,0.7), (0.5,0.2)],         # 5
            [(0.05,0.5), (0.5,0.2), (0,0)],             # 6
            [(0.5,0.2), (0.7,0.7), (1,0)],              # 7
            [(0.5,0.2), (1,0), (0.4,-0.4)],             # 8
            [(0.7,-0.7), (0.4,-0.4), (1,0)],            # 9
            [(0.7,-0.7), (0.4,-0.4), (0.25,-0.8)],      # 10
            [(0.25,-0.8), (0.4,-0.4), (-0.5,-0.6)],     # 11
            [(0.4,-0.4), (0,0), (0.5,0.2)],             # 12
            [(-0.5,-0.7), (0.4,-0.4), (0,0)],           # 13
            [(-0.5,-0.7), (-0.4,-0.2), (0,0)],          # 14
            [(-0.5,-0.7), (-0.4,-0.2), (-0.7,-0.45)]    # 15

            # Old mesh design
            # [(0.0, 1.0), (0.65, 0.65), (0.05, 0.5)],
            # [(0.65, 0.65), (1.0, 0.0), (0.05, 0.5)],
            # [(0.05, 0.5), (1.0, 0.0), (0.0, 0.0)],
            # [(1.0, 0.0), (0.65, -0.65), (0.0, 0.0)],
            # [(0.65, -0.65), (0.25, -0.85), (0.0, 0.0)],
            # [(0.25, -0.85), (-0.5, -0.7), (0.0, 0.0)],
            # [(-0.5, -0.7), (-0.65, -0.45), (0.0, 0.0)],
            # [(-0.65, -0.45), (-0.4, -0.15), (0.0, 0.0)],
            # [(-0.4, -0.15), (-1.0, 0.0), (-0.3, 0.6)],
            # [(-0.4, -0.15), (-0.3, 0.6), (0.0, 0.0)],
            # [(-0.3, 0.6), (0.05, 0.5), (0.0, 0.0)]
        ],
        # Mushroom
        [
            [(0.35, 0.3), (0.5, 1), (1, 0.7)],          # 1
            [(0.35, 0.3), (0.7, 0), (1, 0.7)],          # 2
            [(0.35, 0.3), (0.7, 0), (0.2, -0.3)],       # 3
            [(1, -0.5), (0.7, 0), (0.2, -0.3)],         # 4
            [(1, -0.5), (0.25, -1), (0.2, -0.3)],       # 5
            [(-0.5, -1), (0.25, -1), (0.2, -0.3)],      # 6
            [(-0.5, -1), (-0.5, -0.25), (0.2, -0.3)],   # 7
            [(-0.5, -1), (-0.5, -0.25), (-1, -0.5)],    # 8
            [(-1,0.1), (-0.5, -0.25), (-1, -0.5)],      # 9
            [(-1, 0.1), (-0.5, -0.25), (-1, 0.7)],      # 10
            [(-0.2, 0.2), (-0.5, -0.25), (-1, 0.7)],    # 11
            [(-0.2, 0.2), (-0.5, 1), (-1, 0.7)],        # 12
            [(-0.2, 0.2), (-0.5, 1), (0, 0.5)],         # 13
            [(-0.2, 0.2), (0.35, 0.3), (0, 0.5)],       # 14
            [(-0.2, 0.2), (0.35, 0.3), (0.2, -0.3)],    # 15
            [(-0.2, 0.2), (-0.5, -0.25), (0.2, -0.3)],  # 16
            [(0, 0.5), (0.35, 0.3), (0.5, 1)]           # 17

        ],
        # Weird Looking Pacman
        [
            [(0, 0.1), (0.2, 1), (-0.4, 0.3)],          # 1
            [(-0.3, 1), (0.2, 1), (-0.4, 0.3)],         # 2
            [(-0.3, 1), (-0.4, 0.3), (-1, 0.1)],        # 3
            [(-0.4, 0.3), (-0.5, -0.2), (-1, 0.1)],     # 4
            [(-1, -0.3), (-0.5, -0.2), (-1, 0.1)],      # 5
            [(-1, -0.3), (-0.5, -0.2), (-0.5, -1)],     # 6
            [(0.1, -0.5), (-0.5, -0.2), (-0.5, -1)],    # 7
            [(0.1, -0.5), (-0.5, -0.2), (-0.4, 0.3)],   # 8
            [(0.1, -0.5), (0, 0.1), (-0.4, 0.3)],       # 9
            [(0.1, -0.5), (0, 0.1), (0.5, 0)],          # 10
            [(0.5, 1), (0, 0.1), (0.5, 0)],             # 11
            [(0.5, 1), (1, 0.2), (0.5, 0)],             # 12
            [(0.1, -0.5), (1, -0.2), (0.5, 0)],         # 13
            [(0.1, -0.5), (1, -0.2), (0.2, -1)],        # 14
            [(0.1, -0.5), (-0.5, -1), (0.2, -1)]        # 15
        ],
        # Kaiju
        [
            [(-1, 0.5), (-0.5, 1), (-0.3, 0.5)],        # 1
            [(0, 0.7), (-0.5, 1), (-0.3, 0.5)],         # 2
            [(-1, 0.5), (0, 0), (-0.3, 0.5)],           # 3
            [(0, 0.7), (0, 0), (-0.3, 0.5)],            # 4
            [(0, 0.7), (0, 0), (0.4, 0.5)],             # 5
            [(0, 0.7), (0.7, 1), (0.4, 0.5)],           # 6
            [(1, 0.2), (0.7, 1), (0.4, 0.5)],           # 7
            [(1, 0.2), (0.7, 0), (0.4, 0.5)],           # 8
            [(0, 0), (0.7, 0), (0.4, 0.5)],             # 9
            [(1, 0.2), (0.7, 0), (1, -0.5)],            # 10
            [(0.2, -0.5), (0.7, 0), (1, -0.5)],         # 11
            [(0.2, -0.5), (0.7, 0), (0, 0)],            # 12
            [(0.2, -0.5), (-0.3, -0.4), (0, 0)],        # 13
            [(-1, -0.3), (-0.3, -0.4), (0, 0)],         # 14
            [(-1, -0.3), (-0.3, -0.4), (-1, -0.5)],     # 15
            [(-0.2, -1), (-0.3, -0.4), (-1, -0.5)],     # 16
            [(-0.2, -1), (-0.3, -0.4), (0.2, -0.5)],    # 17
            [(-0.2, -1), (0.5, -1), (0.2, -0.5)]        # 18
        ],
        # Alien
        [
            [(0.5, 0.5), (-0.5, 0.5), (0, 0)],
            [(-0.5, 0.5), (-1, 0), (0, 0)],
            [(-1, 0), (-0.5, -0.25), (0, 0)],
            [(-0.5, -0.25), (-0.4, -0.6), (0, 0)],
            [(-0.4, -0.6), (0.4, -0.6), (0, 0)],
            [(0.4, -0.6), (0.5, -0.25), (0, 0)],
            [(0.5, -0.25), (1, 0), (0, 0)],
            [(1, 0), (0.5, 0.5), (0, 0)]
        ]
    ]

    # Initialize asteroid list with collection of different meshes, random positions, and random velocities
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

        # Variable change for ship and asteroid
        player_ship.frame(button,screen_width,screen_height)
        for asteroid in asteroid_list:
            asteroid.frame(screen_width, screen_height)

        #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(pygame.image.load(background_list[level_num]),(0,0,screen_width,screen_height))
        screen.blit(text_surface, text_surface_rect)

        # Draw Ship
        player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], player_ship.get_ship_coords())
        center = player_ship.get_ship_coords()
        ship_max_dist = player_ship.get_mesh_scaler()

        # Handles all the soft screen wrapping - might add a 4 corner solution if the ship is perfectly in a corner
        if center[0] + ship_max_dist > screen_width:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] - screen_width), center[1]))

        if center[0] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] + screen_width), center[1]))
        if center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], (center[0], (center[1] - screen_height)))
        if center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], (center[0], (center[1] + screen_height)))

        # Corner wrapping
        if center[0] + ship_max_dist > screen_width and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] - screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] + screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] + screen_width), (center[1] + screen_height)))
        if center[0] + ship_max_dist > screen_width and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, (0, 0, 0xFF), lightsource_list[level_num], ((center[0] - screen_width), (center[1] + screen_height)))

        # Draw asteroid and handle screen wrapping for asteroid
        for asteroid in asteroid_list:
            asteroid.draw_asteroid(screen, (128,128,128), lightsource_list[level_num], asteroid.get_coords())
            ast_center = asteroid.get_coords()
            asteroid_max_dist = asteroid.get_mesh_scaler()

            if ast_center[0] + asteroid_max_dist > screen_width:
                asteroid.draw_asteroid(screen, (128, 128, 128), lightsource_list[level_num],((ast_center[0] - screen_width), ast_center[1]))
            if ast_center[0] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, (128, 128, 128), lightsource_list[level_num],((ast_center[0] + screen_width), ast_center[1]))
            if ast_center[1] + asteroid_max_dist > screen_height:
                asteroid.draw_asteroid(screen, (128, 128, 128), lightsource_list[level_num],(ast_center[0], (ast_center[1] - screen_height)))
            if ast_center[1] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, (128, 128, 128), lightsource_list[level_num],(ast_center[0], (ast_center[1] + screen_height)))

        legend.showLegend(screen)
        legend.keyLightUp(button)

        pygame.display.flip()


if __name__ == '__main__':
    main()