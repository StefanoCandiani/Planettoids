import pygame
import math

pygame.init()


def linear_rotate_transform(input_tuple, rotate_angle):
    return math.cos(rotate_angle) * input_tuple[0] - math.sin(rotate_angle) * input_tuple[1], math.sin(rotate_angle) * input_tuple[0] + math.cos(rotate_angle) * input_tuple[1]


screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))  # Sets the screen size

pygame.display.set_caption('Programming Fundamentals')  # Names the game window


x_coordinate = 800  # Starting Coordinates
y_coordinate = 450

running = True
pygame.time.Clock().tick(60)

while running:
    screen.fill('black')  # Keeps the screen background from filling up with after images

    pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, y_coordinate), (x_coordinate, (y_coordinate + 20)), ((x_coordinate - 10), (y_coordinate - 10))))
    # Draws the Left half of the player

    pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, y_coordinate), (x_coordinate, (y_coordinate + 20)), ((x_coordinate + 10), (y_coordinate - 10))))
    # Draws the Right half of the player

    for event in pygame.event.get():
        pass
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()  # Gets key inputs

    if button[pygame.K_LEFT]:  # Moves Left
        x_coordinate -= 1
    if button[pygame.K_RIGHT]:  # Moves Right
        x_coordinate += 1
    if button[pygame.K_UP]:  # Moves Up
        y_coordinate -= 1
    if button[pygame.K_DOWN]:  # Moves Down
        y_coordinate += 1
    if button[pygame.K_ESCAPE]:
        break
    # if button[pygame.K_a]:

    '''This block of code handles the screen wrapping'''

    if x_coordinate < 0:  #
        x_coordinate = screen_width
    if y_coordinate < 0:
        y_coordinate = screen_height
    if x_coordinate > screen_width:
        x_coordinate = 0
    if y_coordinate > screen_height:
        y_coordinate = 0

    '''Draws a copy of the player character on the opposite side of the screen in case the players stops on an edge'''

    if x_coordinate + 10 > screen_width:
        pygame.draw.polygon(screen, (255, 255, 255), (((x_coordinate - screen_width), y_coordinate), (x_coordinate - screen_width, y_coordinate + 20), ((x_coordinate + 10 - screen_width), (y_coordinate - 10))))
    if x_coordinate - 10 < 0:
        pygame.draw.polygon(screen, (255, 255, 255), (((x_coordinate + screen_width), y_coordinate), ((x_coordinate + screen_width), (y_coordinate + 20)), ((x_coordinate - 10 + screen_width), (y_coordinate - 10))))
    if y_coordinate + 20 > screen_height:
        pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, y_coordinate - screen_height), (x_coordinate, (y_coordinate + 20 - screen_height)), ((x_coordinate + 10), (y_coordinate - 10 - screen_height))))
        pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, y_coordinate - screen_height), (x_coordinate, (y_coordinate + 20 - screen_height)), ((x_coordinate - 10), (y_coordinate - 10 - screen_height))))
    if y_coordinate - 10 < 0:
        pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, (y_coordinate + screen_height)), (x_coordinate, (y_coordinate + 20 + screen_height)), ((x_coordinate + 10), (y_coordinate - 10 + screen_height))))
        pygame.draw.polygon(screen, (255, 255, 255), ((x_coordinate, (y_coordinate + screen_height)), (x_coordinate, (y_coordinate + 20 + screen_height)), ((x_coordinate - 10), (y_coordinate - 10 + screen_height))))

    print(x_coordinate, y_coordinate)  # Prints the current coordinates of the center if the player shape

    pygame.display.flip()
