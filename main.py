"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - 12/06/2023
Project: Project 4, "Planettoids"
Group Game: "Blazing Glory"
File: main
"""
#import all libraries and modules
import pygame
import math
import random
from math_functions import *
from ship_class import ship
from userinterface_class import Legend
from userinterface_class import Menu
from userinterface_class import GameOver
from userinterface_class import PlayerWon
from userinterface_class import Level
from asteroid_class import Asteroid
from bullet_class import Bullet

def main():
    #Initialize crucial pre-game variables
    pygame.init() #Initialize game screen
    
    #Screen variables
    screen_width = 800#1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Planettoids Beta v1.1")

    #Load all the background images
    bg1 = pygame.image.load("assets/800x600/Lev1 800x600.png")
    bg2 = pygame.image.load("assets/800x600/Lev2 800x600.png")
    bg3 = pygame.image.load("assets/800x600/Lev3 800x600.png")
    bg4 = pygame.image.load("assets/800x600/Lev4 800x600.png")
    bg5 = pygame.image.load("assets/800x600/Lev5 800x600.png")
    bg6 = pygame.image.load("assets/800x600/Lev6 800x600.png")
    bg7 = pygame.image.load("assets/800x600/Lev7 800x600.png")
    bg8 = pygame.image.load("assets/800x600/Lev8 800x600.png")
    bg9 = pygame.image.load("assets/800x600/Lev9 800x600.png")
    bg10 = pygame.image.load("assets/800x600/Lev10 800x600.png")
    background_list = [bg1,bg2,bg3,bg4,bg5,bg6,bg7,bg8,bg9,bg10]
    
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
        (345, 332),     # Level 10
        (screen_width // 2, screen_height // 2) #Just in case
    ]

    #Initilaize Game Status Variables
    level_num = 0 #Set level number
    max_level = 10-1 # minus one because level number is indexed from 0 but we still have total 10 levels
    level_asteroid_count = [(3,0),(3,1),(4,0),(4,1),(5,0),(5,1),(5,1),(5,2),(6,1),(6,2)] #Contains tuples with the number of asteroids in a level, and the number of UFOs in a level

    #Initialize player ship mesh design
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]

    #Initialize asteroid mesh designs and colors
    asteroid_meshes = [
        [ # Peanut
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
        [ # Cookie
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
            [(-0.2, -0.3), (-0.5, -0.75), (-0.75, -0.5)],    # 13
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
        [ # Jester Hat
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
        [ # Mushroom
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
        [ # Weird Looking Pacman
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
        [ # Kaiju
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
        [ # Alien
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
    #Colors: Dark Grey, Mid Grey, Light Grey, Ice, Faded Brown, Green
    asteroid_colors = [(96, 96, 96),(128, 128, 128),(192, 192, 192),(172,233,255),(56,52,44),(0x00,192,0x00)]

    #Initialize Screens/Menu/Legend
    game_over = GameOver(screen_width, screen_height, screen)
    player_won = PlayerWon(screen_width, screen_height, screen)
    level_menu = Level(screen_width, screen_height, screen)
    menu = Menu(screen_width,screen_height)
    legend = Legend(screen, screen_width, screen_height)
    #Render the menu before the main game loop
    menu.set_menu()

    while True: #Level Loop. This loop allows the inner game play loop to repeat for each level of the game. All the variables for that level must be reset with each interation of the outer level loop.
        
        #Initialize Player Ship
        player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh,ship_color=(0xFF,0xFF,0xFF))

        #Initialize the asteroids list with collection of different meshes, random positions, and random velocities. The positions are randomly calculated for each asteroid and UFO but must lie on the screen
        asteroid_list = []
        for i in range(level_asteroid_count[level_num][0]): #Loop through and instantiate the number of asteroids dedicated to the current level.
            choice = random.choice(
                [(random.randint(0, screen_width), 0),
                  (random.randint(0, screen_width), screen_height),
                    (0, random.randint(0, screen_height)),
                      (screen_width, random.randint(0, screen_height))]
                )
            mesh_choice = random.randint(0,len(asteroid_meshes)-1-1)
            asteroid_list += [Asteroid(choice[0], choice[1], random.random() * math.pi * 2 - math.pi, asteroid_meshes[mesh_choice], asteroid_colors[random.randint(0,len(asteroid_colors)-1-1)], 2)]
        for i in range(level_asteroid_count[level_num][1]): #Loop through and instantiate the number of UFOs dedicated to the current level.
            choice = random.choice(
                [(random.randint(0, screen_width), 0),
                  (random.randint(0, screen_width), screen_height),
                    (0, random.randint(0, screen_height)),
                      (screen_width, random.randint(0, screen_height))]
                )
            asteroid_list += [Asteroid(choice[0], choice[1], ext_atan(tuple_adder([player_ship.get_ship_coords(),tuple_scaler(choice,-1)])), asteroid_meshes[-1], asteroid_colors[-1], 3)]

        #Initialize the bullets list and variables
        bullet_can_spawn = True
        bullets = []

        #Death Cond
        death_flag = False

        #Prints the level of the game
        level_menu.level_menu(level_num+1)

    #Main Gameplay Loop
        running = True #Gameplay loop flag
        while running == True:
            #Take keyboard input
            button = pygame.key.get_pressed()

            #Check through the pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or button[pygame.K_ESCAPE]:
                    print("Thank you for playing!")
                    quit()

            #Spawn bullets first and foremost
            if not death_flag:
                if button[pygame.K_LSHIFT] and bullet_can_spawn:
                    if len(bullets) < 10 - level_num // 2:
                        coords = player_ship.get_ship_coords()
                        angle = player_ship.get_ship_angle()
                        bullets.append(Bullet(screen, coords[0], coords[1], angle))
                    bullet_can_spawn = False
                elif not (button[pygame.K_LSHIFT]):
                    bullet_can_spawn = True

            #Update all objects attributes with physics and ect.
            if not death_flag: #Ships first
                player_ship.frame(button,screen_width,screen_height)
            for asteroid in asteroid_list: #Then asteroids
                asteroid.frame(screen_width, screen_height)
            for bullet in bullets: #And lastly bullets
                bullet.frame(screen_width, screen_height)

            # Collision Detection
            i = 0
            i_bool = True
            while i < len(bullets): #loop through all the bullets
                j = 0
                while j < len(asteroid_list) and len(bullets) != 0 and i < len(bullets): #loop through all the asteroids. (The extra two conditionals in the while loop keep the loop from trying to do asteroid-bullet collision checking if there are no more bullets)

                    if tuple_mag(tuple_adder([bullets[i].get_coords(), tuple_scaler(asteroid_list[j].get_coords(), -1)])) <= bullets[i].radius + asteroid_list[j].get_mesh_scaler(): #If the asteroid collides with a bullet we add two new asteroids of the next size down to the end of the asteroid list and remove that bullet and that asteroid from their lists.
                        
                        if asteroid_list[j].get_asteroid_size() > 0: #This splitting feature only applies for the larger sized asteroids but not for the smallest size. The smallest size asteroid just gets deleted and not split.
                            
                            asteroid_list += [
                                Asteroid(asteroid_list[j].get_coords()[0], asteroid_list[j].get_coords()[1],
                                         bullets[i].get_angle() - math.pi/4,
                                         asteroid_meshes[random.randint(0,len(asteroid_meshes)-1-1)],
                                         asteroid_colors[random.randint(0,len(asteroid_colors)-1-1)],
                                         asteroid_list[j].get_asteroid_size() - 1)]
                            asteroid_list += [
                                Asteroid(asteroid_list[j].get_coords()[0], asteroid_list[j].get_coords()[1],
                                         bullets[i].get_angle() + math.pi/4,
                                         asteroid_meshes[random.randint(0,len(asteroid_meshes)-1-1)],
                                         asteroid_colors[random.randint(0,len(asteroid_colors)-1-1)],
                                         asteroid_list[j].get_asteroid_size() - 1)]

                        bullets = bullets[:i] + bullets[i+1:] #Remove the bullet
                        asteroid_list = asteroid_list[:j] + asteroid_list[j+1:] #Remove the asteroid
                        i_bool = False
                    else:
                        j += 1
                if i_bool:
                    i += 1
                else:
                    i_bool = True

            #Check for asteroid collision with player. (We check this after asteroid-bullet collision to give the player some split second leeway)
            for roid in asteroid_list:
                if tuple_mag(tuple_adder([player_ship.get_ship_coords(), tuple_scaler(roid.get_coords(), -1)])) <= player_ship.get_mesh_scaler() + roid.get_mesh_scaler():
                    death_flag = True

            #Draw Operations
            screen.blit(background_list[level_num],(0,0,screen_width,screen_height)) #Draw the background behind everything

            #Draw the Ship if the player isn't dead
            if not death_flag:
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
                #if len(bullets) == 0:
                #    break
                bullet.draw_bullet()

            #Draw asteroid and handle screen wrapping for asteroid
            for asteroid in reversed(asteroid_list):
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

            # Check for game win or lose conditions
            if len(asteroid_list) == 0 and not death_flag: # If the player destroys all of the asteroids then they win. (If the plater dies before all the asteroids are destroyed but the asteroids do all get destroyed, the player still loses and we don't draw the win screen)

                if level_num+1 > max_level: # check if the level is the last one then print win screen
                    player_won.player_won_menu()
                    if button[pygame.K_RETURN]: # check if Enter is pressed
                        level_num = 0 #Allow the player to reset the game back to level 1
                        running = False
                        continue
                else:
                    level_menu.level_increment(level_num+1) # otherwise continue to next level if enter is pressed
                    death_flag = False
                    if button[pygame.K_RETURN]: # check if Enter is pressed
                        level_num += 1
                        running = False
                        continue

            if death_flag: #If the player dies 
                game_over.game_over_menu()
                if button[pygame.K_RETURN]: # check if Enter is pressed
                    running = False
                    continue

            pygame.display.flip()
            pygame.time.Clock().tick(100)

    return #End of main (this is never reach)

if __name__ == '__main__':
    main()