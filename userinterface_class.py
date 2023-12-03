"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: userinterface_class
"""
import pygame
#from PIL import Image #Not needed for normal execution

class Menu:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # image = Image.open('assets/down_arrow_off.png')     # run one time if image background is not correct size
        # new_image = image.resize((50, 50))
        # new_image.save('assets/down_arrow_off.png')
        # image = Image.open('assets/down_arrow_on.png')  # run one time if image background is not correct size
        # new_image = image.resize((50, 50))
        # new_image.save('assets/down_arrow_on.png')

    def set_menu(self):
        bg = pygame.image.load("assets/pluto_background.png")

        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 100)        # title
        text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = (self.screen_width // 2, self.screen_height // 5 - 50)

        font_object_title = pygame.font.Font('assets/AmazDooMLeft.ttf', 30)         # menu text to start game
        text_start = font_object_title.render('Press Enter to Start Game', True, (255, 255, 255))
        text_start_rect = text_start.get_rect()
        text_start_rect.center = (self.screen_width // 2, self.screen_height - 100)

        font_object_title = pygame.font.Font('assets/arial.ttf', 10)    # copyright text on menu
        text_copyright = font_object_title.render('Copyright© 2023. Phoenix Cushman, Joel Kubinsky, Stefano Candiani, Danush Singla. All rights reserved.', True, (255, 255, 255))
        text_copyright_rect = text_copyright.get_rect()
        text_copyright_rect.center = (self.screen_width // 2, self.screen_height - 10)

        running = True  # Main execution boolean
        while running == True:
            button = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or button[pygame.K_RETURN]:  # stop running the menu when enter is pressed
                    running = False
                    continue

            # run the menu
            self.screen.blit(bg, (0, 0, self.screen_width, self.screen_height))
            self.screen.blit(text_surface, text_surface_rect)       # title
            self.screen.blit(text_start, text_start_rect)       # start game text
            self.screen.blit(text_copyright, text_copyright_rect)       # copyright text

            pygame.display.flip()

class Legend:
    screen = None           # screen properties
    screen_width = None
    screen_height= None
    font = ''

    def __init__(self, screen, screen_width, screen_height, font='AmazDooMLeftOutline.ttf'):     # takes data from main
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


    def offUp(self, image):        # if the up key is not being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/up_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 105))


    # def offDown(self, image):        # if the down key is not being pressed then load that png - removed
    #     # creates the icon
    #     # image = pygame.image.load('assets/down_arrow_off.png')
    #     # image = pygame.transform.scale(image, (50,50))
    #     self.screen.blit(image, (self.screen_width - 97, self.screen_height - 70))


    def offLeft(self, image):        # if the left key is not being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/left_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))

    def offRight(self, image):        # if the right key is not being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 70))

    def offShift(self, image):        # if the shift key is not being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 250, self.screen_height - 64))

    def onUp(self, image):        # if the up key is being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/up_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 105))
        # pygame.display.flip()

    # def onDown(self, image):        # if the down key is being pressed then load that png - removed
    #     # creates the icon
    #     # image = pygame.image.load('assets/down_arrow_on.png')
    #     # image = pygame.transform.scale(image, (50,50))
    #     self.screen.blit(image, (self.screen_width - 97, self.screen_height - 70))

    def onLeft(self, image):        # if the left key is being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/left_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))

    def onRight(self, image):        # if the right key is being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_on.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 70))

    def onShift(self, image):        # if the shift key is not being pressed then load that png
        # creates the icon
        # image = pygame.image.load('assets/right_arrow_off.png')
        # image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 250, self.screen_height - 64))

    def showLegend(self, screen):       # shows the legend by calling the respective functions
        self.offUp(self.offup_image)
        # self.offDown(self.offdown_image)
        self.offLeft(self.offleft_image)
        self.offRight(self.offright_image)
        self.offShift(self.offshift_image)

    def keyLightUp(self, button):       # if a key is pressed relating to something on the legend, then light it up
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