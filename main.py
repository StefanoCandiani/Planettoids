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
from userinterface_class import Menu
from asteroid_class import Asteroid
from bullet_class import Bullet

def main():

#Initilaize Game Variables

    #Screen variables
    pygame.init() #Initialize game screen
    screen_width = 800#1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Planettoids Beta v1.1")
    
    #Set level number
    level_num = 0

    #NOTE: For future implementation we should load these images into sprites to speed up the draw commands
    bg1 = pygame.image.load("assets/background1.png")
    background_list = [bg1]
    
    #Light Source Variables
    lightsource_list = [(345,332)] #(screen_width // 2, screen_height // 2)

    #Title text objects
    font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
    #text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    #text_surface_rect = text_surface.get_rect()
    #text_surface_rect.center = (screen_width // 2, screen_height // 5)

    #Initialize Player Ship
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]
    player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh,ship_color=(0xFF,0xFF,0xFF))

    #Initialize asteroid mesh designs #and colors
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
        ],
        #Alien Mesh to implement
        [
            [(0.5, 0.5), (-0.5, 0.5), (0, 0)],
            [(-0.5, 0.5), (-1, 0), (0, 0)],
            [(-1, 0), (-0.5, -0.25), (0, 0)],
            [(-0.5, -0.25), (-0.4, -0.6), (0, 0)],
            [(-0.4, -0.6), (0.4, -0.6), (0, 0)],
            [(0.4, -0.6), (0.5, -0.25), (0, 0)],
            [(0.5, -0.25), (1, 0), (0, 0)],
            [(1, 0), (0.5, 0.5), (0, 0)],
        ]
    ]
    asteroid_colors = [(96, 96, 96),(128, 128, 128),(192, 192, 192),(0x00,192,0x00)]
    
    #Initialize the asteroids list with collection of different meshes, random positions, and random velocities
    asteroid_list = [Asteroid(random.randint(0, screen_width), random.randint(0, screen_height), random.random(),random.random(), asteroid_meshes[i], asteroid_color = asteroid_colors[i]) for i in range(len(asteroid_meshes))] #NOTE:Asteroid list initialization code optimized with list comprehension
    
    #Initialize the bullets list and variables
    bullet_can_spawn = True
    bullets = []

    #Create the UI
    legend = Legend(screen, screen_width, screen_height)
    menu = Menu()

    #Before we enter the gameplay loop we start the menu screen
    menu.set_menu()
#Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        button = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
                running = False
                continue

    #Spawn bullets first and foremost
        if button[pygame.K_LSHIFT] and bullet_can_spawn:
            if len(bullets) < 10:
                coords = player_ship.get_ship_coords()
                angle = player_ship.get_ship_angle()
                bullets.append(Bullet(screen, coords[0], coords[1], angle))
            bullet_can_spawn = False
        elif not(button[pygame.K_LSHIFT]):
            bullet_can_spawn = True

    #Update all objects attributes with physics and ect.
        #Ships first
        player_ship.frame(button,screen_width,screen_height)
        #Then asteroids
        for asteroid in asteroid_list:
            asteroid.frame(screen_width, screen_height)

    #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(background_list[level_num],(0,0,screen_width,screen_height))
        #screen.blit(text_surface, text_surface_rect)

        # Draw Ship
        player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], player_ship.get_ship_coords())
        #Pull ship coords for the wrapping code
        center = player_ship.get_ship_coords()
        ship_max_dist = player_ship.get_mesh_scaler()
        # Handles all the soft screen wrapping - might add a 4 corner solution if the ship is perfectly in a corner
        if center[0] + ship_max_dist > screen_width:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] - screen_width), center[1]))
        if center[0] - ship_max_dist < 0:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] + screen_width), center[1]))
        if center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], (center[0], (center[1] - screen_height)))
        if center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], (center[0], (center[1] + screen_height)))
        #Corner wrapping
        if center[0] + ship_max_dist > screen_width and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] - screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] + ship_max_dist > screen_height:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] + screen_width), (center[1] - screen_height)))
        if center[0] - ship_max_dist < 0 and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] + screen_width), (center[1] + screen_height)))
        if center[0] + ship_max_dist > screen_width and center[1] - ship_max_dist < 0:
            player_ship.draw_ship(screen, player_ship.get_ship_color(), lightsource_list[level_num], ((center[0] - screen_width), (center[1] + screen_height)))

        #Draw bullets
        for bullet in bullets:
            if len(bullets) == 0:
                break
            # print(bullet, end=', ')
            bullet.frame(screen_width, screen_height)
            bullet.draw_bullet()
        # print(len(bullets))

        # Draw asteroid and handle screen wrapping for asteroid
        for asteroid in asteroid_list:
            asteroid.draw_asteroid(screen, asteroid.get_asteroid_color(), lightsource_list[level_num], asteroid.get_coords())
            ast_center = asteroid.get_coords()
            asteroid_max_dist = asteroid.get_mesh_scaler()
            #Screen wrapping code
            if ast_center[0] + asteroid_max_dist > screen_width:
                asteroid.draw_asteroid(screen, asteroid.get_asteroid_color(), lightsource_list[level_num],((ast_center[0] - screen_width), ast_center[1]))
            if ast_center[0] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, asteroid.get_asteroid_color(), lightsource_list[level_num],((ast_center[0] + screen_width), ast_center[1]))
            if ast_center[1] + asteroid_max_dist > screen_height:
                asteroid.draw_asteroid(screen, asteroid.get_asteroid_color(), lightsource_list[level_num],(ast_center[0], (ast_center[1] - screen_height)))
            if ast_center[1] - asteroid_max_dist < 0:
                asteroid.draw_asteroid(screen, asteroid.get_asteroid_color(), lightsource_list[level_num],(ast_center[0], (ast_center[1] + screen_height)))

        # draw the key legend (We draw it last so that the UI shows on top of everything else)
        legend.showLegend(screen)
        legend.keyLightUp(button)

        pygame.display.flip()


if __name__ == '__main__':
    main()