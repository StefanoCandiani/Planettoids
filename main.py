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
from userinterface_class import GameOver
from asteroid_class import Asteroid
from bullet_class import Bullet

def main():
#Initilaize Game Variables

    #Screen variables
    # pygame.init() #Initialize game screen
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


    #Initialize Player Ship
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]
    player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh,ship_color=(0xFF,0xFF,0xFF))

    #Initialize Game Over Screen
    game_over = GameOver(screen_width, screen_height, screen)

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

    #Death Cond
    death_flag = False

#Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        button = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
                running = False
                continue

    #Spawn bullets first and foremost
        if not death_flag:
            if button[pygame.K_LSHIFT] and bullet_can_spawn:
                if len(bullets) < 10:
                    coords = player_ship.get_ship_coords()
                    angle = player_ship.get_ship_angle()
                    bullets.append(Bullet(screen, coords[0], coords[1], angle))
                bullet_can_spawn = False
            elif not (button[pygame.K_LSHIFT]):
                bullet_can_spawn = True

    #Update all objects attributes with physics and ect.
        #Ships first
        player_ship.frame(button,screen_width,screen_height)
        #Then asteroids
        for asteroid in asteroid_list:
            asteroid.frame(screen_width, screen_height)

    # Collision Detection
        i = 0
        i_bool = True
        while i < len(bullets):
            j = 0

            while j < len(asteroid_list):
                if len(bullets) == 0 or i >= len(bullets):
                    break

                if tuple_mag(tuple_adder([bullets[i].get_coords(), tuple_scaler(asteroid_list[j].get_coords(), -1)])) <= bullets[i].radius + asteroid_list[j].get_mesh_scaler():

                    # FIXME : add cond for smallest asteroid
                    asteroid_list += [Asteroid(asteroid_list[j].get_coords()[0], asteroid_list[j].get_coords()[1], (asteroid_list[j].get_asteroid_velo()[0] * -1), asteroid_list[j].get_asteroid_velo()[1], asteroid_list[j].get_asteroid_mesh(), asteroid_list[j].mesh_scale//2, asteroid_list[j].get_asteroid_color())]
                    asteroid_list += [Asteroid(asteroid_list[j].get_coords()[0], asteroid_list[j].get_coords()[1], asteroid_list[j].get_asteroid_velo()[0], (asteroid_list[j].get_asteroid_velo()[1] * -1), asteroid_list[j].get_asteroid_mesh(), asteroid_list[j].mesh_scale // 2, asteroid_list[j].get_asteroid_color())]

                    bullets = bullets[:i] + bullets[i+1:]
                    asteroid_list = asteroid_list[:j] + asteroid_list[j+1:]
                    i_bool = False
                else:
                    j += 1
            if i_bool:
                i += 1
            else:
                i_bool = True

        for roid in asteroid_list:
            if tuple_mag(tuple_adder([player_ship.get_ship_coords(), tuple_scaler(roid.get_coords(), -1)])) <= player_ship.get_mesh_scaler() + roid.get_mesh_scaler():
                death_flag = True

    #Draw Operations

        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(background_list[level_num],(0,0,screen_width,screen_height))

        if not death_flag:
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

        if death_flag:
            game_over.game_over_menu()
            if button[pygame.K_RETURN]:  # check if Enter is pressed
                print("Enter is Pressed")
                death_flag = False
                continue

        pygame.display.flip()
        pygame.time.Clock().tick(100)


if __name__ == '__main__':
    pygame.init()
    menu = Menu()
    menu.set_menu()
    main()    # only temporarily

