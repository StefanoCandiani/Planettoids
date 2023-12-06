"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - 12/06/2023
Project: Project 4, "Planettoids"
Group Game: "Blazing Glory"
File: userinterface_class
"""
import pygame
import time

# prints the level
class Level:
    def __init__(self, screen_width, screen_height, screen):
        '''Initializes the screen variables for the Level object.'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        return

    # screen that displays the level
    def level_menu(self, level_number):
        '''Displays the level number screen over the course of 2 seconds and also listens for pygame.QUIT events.'''
        # Level number
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 50)
        for i in range(60):
            button = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thank you for playing!")
                    quit()
            text_surface = font_object_title.render(f'Level {level_number}', True, (255*i/60, 176*i/60, 20*i/60))
            text_surface_rect = text_surface.get_rect()
            text_surface_rect.center = (self.screen_width // 2, self.screen_height // 2)
            self.screen.fill((0,0,0))
            self.screen.blit(text_surface, text_surface_rect)
            pygame.display.flip()
            time.sleep(2/60)
        return

    # Level complete screen
    def level_increment(self, level_num):
        '''Displays the level complete text over the screen.'''
        # Game Over
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
        text_surface = font_object_title.render(f'Level {level_num} Complete!', True, (0, 255, 0))
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (self.screen_width // 2, self.screen_height // 5)
        self.screen.blit(text_surface, text_surface_rect)

        # Move on to next level
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 30)  # menu text to start game
        text_start = font_object_title.render('Press Enter to Play Next Level', True, (255, 255, 255))
        text_start_rect = text_start.get_rect()
        text_start_rect.center = (self.screen_width // 2, self.screen_height - 100)
        self.screen.blit(text_start, text_start_rect)

        # # Or quit by pressing escape
        # font_object_title_end = pygame.font.Font('assets/AmazDooMLeft.ttf', 20)  # menu text to start game
        # text_end = font_object_title_end.render('Press Escape to Quit Game', True, (255, 255, 255))
        # text_end_rect = text_start.get_rect()
        # text_end_rect.center = (self.screen_width - 350, self.screen_height - 50)
        # self.screen.blit(text_end, text_end_rect)
        return

# if the player wins the game
class PlayerWon:
    def __init__(self, screen_width, screen_height, screen):
        '''Initializes the screen variables for the PlayerWon object.'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        return

    # You win screen
    def player_won_menu(self):
        '''Displays the "YOU WIN!" text over the screen. This tells the player that they have beat the game.'''
        # Game Over
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
        text_surface = font_object_title.render('YOU WIN!', True, (0, 255, 0))
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (self.screen_width // 2, self.screen_height // 5)
        self.screen.blit(text_surface, text_surface_rect)

        # Start Game Again
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 30)  # menu text to start game
        text_start = font_object_title.render('Press Enter to Play Again', True, (255, 255, 255))
        text_start_rect = text_start.get_rect()
        text_start_rect.center = (self.screen_width // 2, self.screen_height - 100)
        self.screen.blit(text_start, text_start_rect)

        # Or quit by pressing escape
        font_object_title_end = pygame.font.Font('assets/AmazDooMLeft.ttf', 20)  # menu text to start game
        text_end = font_object_title_end.render('Press Escape to Quit Game', True, (255, 255, 255))
        text_end_rect = text_start.get_rect()
        text_end_rect.center = (self.screen_width - 368, self.screen_height - 50)
        self.screen.blit(text_end, text_end_rect)
        return

# if the game ends when the player hits an asteroid
class GameOver:
    def __init__(self, screen_width, screen_height, screen):
        '''Initializes the screen variables for the GameOver object.'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        return

    # Game Over screen
    def game_over_menu(self):
        '''Displays the "game over" text over the screen.'''
        # Game Over
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)
        text_surface = font_object_title.render('GAME OVER', True, (255, 0, 0))
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (self.screen_width // 2, self.screen_height // 5)
        self.screen.blit(text_surface, text_surface_rect)

        # Start Game Again
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 30)  # menu text to start game
        text_start = font_object_title.render('Press Enter to Play Again', True, (255, 255, 255))
        text_start_rect = text_start.get_rect()
        text_start_rect.center = (self.screen_width // 2, self.screen_height - 100)
        self.screen.blit(text_start, text_start_rect)

        # Or quit by pressing escape
        font_object_title_end = pygame.font.Font('assets/AmazDooMLeft.ttf', 20)  # menu text to start game
        text_end = font_object_title_end.render('Press Escape to Quit Game', True, (255, 255, 255))
        text_end_rect = text_start.get_rect()
        text_end_rect.center = (self.screen_width - 368, self.screen_height - 50)
        self.screen.blit(text_end, text_end_rect)
        return

# Initial menu that is printed first
class Menu:
    def __init__(self, screen_width = 800, screen_height = 600):
        '''Initializes the screen variables for the Menu object.'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # image = Image.open('assets/down_arrow_off.png')     # run one time if image background is not correct size
        # new_image = image.resize((50, 50))
        # new_image.save('assets/down_arrow_off.png')
        # image = Image.open('assets/down_arrow_on.png')  # run one time if image background is not correct size
        # new_image = image.resize((50, 50))
        # new_image.save('assets/down_arrow_on.png')
        return

    # Sets all of the text for the menu
    def set_menu(self):
        '''This function displays the game title menu with the included background and foreground text, as well as waiting for user input to proceed. (Enter starts the game)'''
        bg = pygame.image.load("assets/800x600/menu 800x600.png")

        # Title
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)        # title
        text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (self.screen_width // 2, self.screen_height // 5 - 50)

        # Text to press enter
        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 30)         # menu text to start game
        text_start = font_object_title.render('Press Enter to Start Game', True, (255, 255, 255))
        text_start_rect = text_start.get_rect()
        text_start_rect.center = (self.screen_width // 2, self.screen_height - 100)

        # Copyright text
        font_object_title = pygame.font.Font('assets/arial.ttf', 10)    # copyright text on menu
        text_copyright = font_object_title.render('Copyright© 2023. Phoenix Cushman, Joel Kubinsky, Stefano Candiani, Danush Singla. All rights reserved.', True, (255, 255, 255))
        text_copyright_rect = text_copyright.get_rect()
        text_copyright_rect.center = (self.screen_width // 2, self.screen_height - 10)

        # while loop that displays the menu continuously until enter is pressed to start the game
        running = True  # Main execution boolean
        while running == True:
            button = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thank you for playing!")
                    quit()
                if button[pygame.K_RETURN]:  # stop running the menu when enter is pressed
                    running = False
                    continue

            # run the menu
            self.screen.blit(bg, (0, 0, self.screen_width, self.screen_height))
            self.screen.blit(text_surface, text_surface_rect)       # title
            self.screen.blit(text_start, text_start_rect)       # start game text
            self.screen.blit(text_copyright, text_copyright_rect)       # copyright text

            pygame.display.flip()
        return

# part where the keys light up
class Legend:
    screen = None           # screen properties
    screen_width = None
    screen_height= None
    font = ''

    def __init__(self, screen, screen_width, screen_height, font='AmazDooMLeftOutline.ttf'):     # takes data from main
        '''Initializes the screen variables for the Legend object and loads all the arrow icon pngs into variables.'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.screen = screen

        # image size: 745 by 648, 220 x 263 for arrow and 450x350 for box
        self.offup_image = pygame.image.load('assets/up_arrow_off.png')     # sets up default up arrow key
        # self.offdown_image = pygame.image.load('assets/down_arrow_off.png') # sets up down arrow key - removed
        self.offleft_image = pygame.image.load('assets/left_arrow_off.png')     # sets up default left arrow key
        self.offright_image = pygame.image.load('assets/right_arrow_off.png')     # sets up default right arrow key
        self.offshift_image = pygame.image.load('assets/shift_key_off.png')  # sets up default shift key
        self.onup_image = pygame.image.load('assets/up_arrow_on.png')     # sets up pressed up arrow key
        # self.ondown_image = pygame.image.load('assets/down_arrow_on.png')  # sets down pressed up arrow key - removed
        self.onleft_image = pygame.image.load('assets/left_arrow_on.png')     # sets up pressed left arrow key
        self.onright_image = pygame.image.load('assets/right_arrow_on.png')     # sets up pressed right arrow key
        self.onshift_image = pygame.image.load('assets/shift_key_on.png')  # sets up pressed shift key
        return


    def offUp(self, image):        # if the up key is not being pressed then load that png
        '''Displays an unpressed up arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/up_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 105))
        return

    # def offDown(self, image):        # if the down key is not being pressed then load that png - removed
    #     '''Displays an unpressed down arrow icon.'''
    #     # creates the icon
    #     # image = pygame.image.load('assets/down_arrow_off.png')
    #     # image = pygame.transform.scale(image, (50,50))
    #     self.screen.blit(image, (self.screen_width - 97, self.screen_height - 70))
    #     return

    def offLeft(self, image):        # if the left key is not being pressed then load that png
        '''Displays an unpressed left arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/left_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))
        return

    def offRight(self, image):        # if the right key is not being pressed then load that png
        '''Displays an unpressed right arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 70))
        return

    def offShift(self, image):        # if the shift key is not being pressed then load that png
        '''Displays an unpressed shift key icon.'''
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 250, self.screen_height - 64))
        return

    def onUp(self, image):        # if the up key is being pressed then load that png
        '''Displays a pressed up arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/up_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 105))
        return
        # pygame.display.flip()

    # def onDown(self, image):        # if the down key is being pressed then load that png - removed
    #     '''Displays a pressed down arrow icon.'''
    #     # creates the icon
    #     # image = pygame.image.load('assets/down_arrow_on.png')
    #     # image = pygame.transform.scale(image, (50,50))
    #     self.screen.blit(image, (self.screen_width - 97, self.screen_height - 70))
    #     return

    def onLeft(self, image):        # if the left key is being pressed then load that png
        '''Displays a pressed left arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/left_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))
        return

    def onRight(self, image):        # if the right key is being pressed then load that png
        '''Displays a pressed right arrow icon.'''
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 70))
        return

    def onShift(self, image):        # if the shift key is not being pressed then load that png
        '''Displays a pressed shift key icon.'''
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 250, self.screen_height - 64))
        return

    def showLegend(self, screen):       # shows the legend by calling the respective functions
        '''Displays the off-state icons for all four buttons (Up, Left, Right, LShift).'''
        self.offUp(self.offup_image)
        # self.offDown(self.offdown_image)
        self.offLeft(self.offleft_image)
        self.offRight(self.offright_image)
        self.offShift(self.offshift_image)
        return

    def keyLightUp(self, button):       # if a key is pressed relating to something on the legend, then light it up
        '''This function uses the keyboard input to render all the on-state icons for each button the player can press.'''
        if button[pygame.K_UP]:     # up key
            self.onUp(self.onup_image)
        else:
            self.offUp(self.offup_image)

        # if button[pygame.K_DOWN]:     # down key - removed
        #     self.onDown(self.ondown_image)
        # else:
        #     self.offDown(self.offdown_image)

        if button[pygame.K_LEFT]:       # left key
            self.onLeft(self.onleft_image)
        else:
            self.offLeft(self.offleft_image)

        if button[pygame.K_RIGHT]:      # right key
            self.onRight(self.onright_image)
        else:
            self.offRight(self.offright_image)

        if button[pygame.K_LSHIFT]:      # shift key
            self.onShift(self.onshift_image)
        else:
            self.offShift(self.offshift_image)
        return