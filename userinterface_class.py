import pygame

# legend = Legend(screen, screen_width, screen_height)
# legend.keyLightUp(button)

class Legend:
    screen = None
    screen_width = None
    screen_height= None
    font = ''

    def __init__(self, screen, screen_width, screen_height, font='AmazDooMLeftOutline.ttf'):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.screen = screen

    def offUp(self):
        # creates the icon
        image = pygame.image.load('assets/up_arrow_off.png')
        image = pygame.transform.scale(image, (50,50)) # image size: 745 by 648, 220 x 263 for arrow and 450x350 for box
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 69))

    def offDown(self):
        # creates the icon
        image = pygame.image.load('assets/down_arrow_off.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 97, self.screen_height - 73))

    def offLeft(self):
        # creates the icon
        image = pygame.image.load('assets/left_arrow_off.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))

    def offRight(self):
        # creates the icon
        image = pygame.image.load('assets/right_arrow_off.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 71))

    def onUp(self):
        # creates the icon
        image = pygame.image.load('assets/up_arrow_on.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 100, self.screen_height - 69))
        # pygame.display.flip()

    def onDown(self):
        # creates the icon
        image = pygame.image.load('assets/down_arrow_on.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 97, self.screen_height - 70))

    def onLeft(self):
        # creates the icon
        image = pygame.image.load('assets/left_arrow_on.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 130, self.screen_height - 66))

    def onRight(self):
        # creates the icon
        image = pygame.image.load('assets/right_arrow_on.png')
        image = pygame.transform.scale(image, (50,50))
        self.screen.blit(image, (self.screen_width - 57, self.screen_height - 71))

    def showLegend(self, screen):
        self.offUp()
        # self.offDown()
        self.offLeft()
        self.offRight()

    def keyLightUp(self, button):
        if button[pygame.K_UP]:
            self.onUp()
        else:
            self.offUp()

        # if button[pygame.K_DOWN]:
        #     self.onDown()
        # else:
        #     self.offDown()

        if button[pygame.K_LEFT]:
            self.onLeft()
        else:
            self.offLeft()

        if button[pygame.K_RIGHT]:
            self.onRight()
        else:
            self.offRight()