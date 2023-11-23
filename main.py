"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: main
"""
import pygame
import math
from math_functions import *
from ship_class import ship

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

    #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(bg,(0,0,screen_width,screen_height))
        screen.blit(text_surface, text_surface_rect)
        # Draw Ship
        player_ship.draw_ship(screen,(0,0,0xFF),(light_source_x, light_source_y),player_ship.get_ship_coords())

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

        pygame.display.flip()


if __name__ == '__main__':
    main()