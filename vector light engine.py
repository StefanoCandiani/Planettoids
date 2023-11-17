"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
"""
#import libraries
import pygame
import random
import math

def tuple_adder(tuple_list): #This function given a list of tuples, adds each of the same index elements together and returns a tuple containing those sums.
    return_tup = (0,0)
    for tup in tuple_list:
        return_tup = (return_tup[0]+tup[0],return_tup[1]+tup[1])
    return return_tup

def tuple_scaler(input_tuple,scalar): #This function given a tuple and scalar, multiplies all the elements of the tuple by that value.
    return_tuple = tuple()
    for i in range(0,len(input_tuple)):
        return_tuple += tuple([input_tuple[i] * scalar])
    return return_tuple

def ext_atan(input_tuple): #Given a point in space this function calculates that points angle respective to the positive x-axis. The result is an angle in the range [-pi,pi)
    return_angle = float(0)
    if input_tuple[0]>0 and input_tuple[1]==0:
        return_angle = 0
    elif input_tuple[0]>0 and input_tuple[1]>0:
        return_angle = math.atan(input_tuple[1]/input_tuple[0])
    elif input_tuple[0]==0 and input_tuple[1]>0:
        return_angle = math.pi/2
    elif input_tuple[0]<0 and input_tuple[1]>0:
        return_angle = math.pi + math.atan(input_tuple[1]/input_tuple[0])
    elif input_tuple[0]<0 and input_tuple[1]==0:
        return_angle = -math.pi
    elif input_tuple[0]<0 and input_tuple[1]<0:
        return_angle = -(math.pi) + math.atan(input_tuple[1]/input_tuple[0])
    elif input_tuple[0]==0 and input_tuple[1]<0:
        return_angle = -(math.pi/2)
    elif input_tuple[0]>0 and input_tuple[1]<0:
        return_angle = math.atan(input_tuple[1]/input_tuple[0])
    return return_angle

def linear_rotate_transform(input_tuple,rotate_angle): #This function given a point about the origin and an angle respective to the positive x-axis, rotates that point about the origin by that angle and returns the new location of the point.
    return (math.cos(rotate_angle)*input_tuple[0]-math.sin(rotate_angle)*input_tuple[1],math.sin(rotate_angle)*input_tuple[0]+math.cos(rotate_angle)*input_tuple[1])

def light_multiplier_calculator(tri_center_tuple,object_center_tuple,light_tuple): #This function takes in the center of a triangle respective to the triangles origin, the center of an object respective to the game screen, and the center of a light source respective to the game screen, and returns a multiplier for the light brightness of that polygon to the light source.
    center_angle = angle_rebounder(ext_atan(tri_center_tuple))
    light_angle = angle_rebounder(ext_atan(tuple_adder([object_center_tuple,tuple_scaler(light_tuple,-1)])))
    difference_angle = angle_rebounder((center_angle - light_angle))
#These lines below, contain different manipulations of the light gradient function. The top two are trigonometric while the bottom two are absolute-value linear.
    #return math.fabs(-(math.cos(difference_angle/2)) + 1) #Old light calc
    #return math.fabs( -1*math.fabs(difference_angle/math.pi) + 1) #Old light calc
    #return math.fabs(difference_angle/math.pi) #Old light calc
    return math.fabs((math.fabs(difference_angle/math.pi)+1)/2) #current light calc

def angle_rebounder(input_angle): #Recaptures a given angle into the range (-pi,pi]
    if math.sin(input_angle) > 0:
        return (input_angle % math.pi)
    if math.sin(input_angle) < 0:
        return (-1*math.pi) + (input_angle % math.pi)
    if math.sin(input_angle) == 0:
        if math.cos(input_angle) > 0:
            return 0
        if math.cos(input_angle) < 0:
            return math.pi
    return

def negative_angle(input_angle):
    return angle_rebounder(input_angle + math.pi)

class ship():
    def __init__(self,center_x=0,center_y=0,poly_mesh=[[(0,0),(1,0),(0,1)]],poly_scale=20,ship_angle=0):
        #Initialize Variables
        self.ship_center_x = center_x
        self.ship_center_y = center_y
        self.ship_angle = ship_angle
        self.base_mesh = poly_mesh
        self.transform_mesh = [[j for j in i] for i in self.base_mesh]
        self.translate_mesh = [[j for j in i] for i in self.base_mesh]
        self.mesh_scale = poly_scale

        self.ship_velocity_x = 0
        self.ship_velocity_y = 0

        self.ship_thrust_multiplier = 7

        return

    def frame(self,button,screen_width,screen_height):
    #Controls and Movement Section
        #Check steering
        if button[pygame.K_LEFT]:
            self.ship_angle -= math.pi/25
        if button[pygame.K_RIGHT]:
            self.ship_angle += math.pi/25
        self.ship_angle = angle_rebounder(self.ship_angle)
        # Check thrust
        if button[pygame.K_UP]:
            self.ship_velocity_x += math.cos(self.ship_angle)
            self.ship_velocity_y += math.sin(self.ship_angle)

        self.ship_velocity_x -= 0.25*math.cos((ext_atan((self.ship_velocity_x,self.ship_velocity_y))))
        self.ship_velocity_y -= 0.25*math.sin((ext_atan((self.ship_velocity_x,self.ship_velocity_y))))

        if round(self.ship_velocity_x,2)==0:
            self.ship_velocity_x = 0
        if round(self.ship_velocity_y,2)==0:
            self.ship_velocity_y = 0

        '''
        else:
            #Reduce velocity when no key pressed
            if self.ship_velocity_x > 0:
                self.ship_velocity_x -= 0.1
            elif self.ship_velocity_x < 0:
                self.ship_velocity_x += 0.1
            if self.ship_velocity_y > 0:
                self.ship_velocity_y -= 0.1
            elif self.ship_velocity_y < 0:
                self.ship_velocity_y += 0.1
            #Truncate off the velocity to get it to zero
            if round(self.ship_velocity_x,1)==0:
                self.ship_velocity_x = 0
            if round(self.ship_velocity_y,1)==0:
                self.ship_velocity_y = 0
        '''

        # Bound velocity
        if math.sqrt(((self.ship_velocity_x)**2)+((self.ship_velocity_y)**2)) > 10:
            ship_velocity_x = tuple_scaler((self.ship_velocity_x, self.ship_velocity_y),
                                           10 / math.sqrt(((self.ship_velocity_x) ** 2) + ((self.ship_velocity_y) ** 2)))[
                0]
            ship_velocity_y = tuple_scaler((self.ship_velocity_x, self.ship_velocity_y),
                                           10 / math.sqrt(((self.ship_velocity_x) ** 2) + ((self.ship_velocity_y) ** 2)))[
                1]

        # Apply velocities
        self.ship_center_x += self.ship_velocity_x
        self.ship_center_y += self.ship_velocity_y

    #Collision Section
        # Wrap ship
        if self.ship_center_x < 0:
            self.ship_center_x = screen_width
        if self.ship_center_x > screen_width:
            self.ship_center_x = 0
        if self.ship_center_y < 0:
            self.ship_center_y = screen_height
        if self.ship_center_y > screen_height:
            self.ship_center_y = 0
    #Math Section
        #Rotate base mesh and store to transform mesh
        for individual_polygon_index in range(0, len(self.base_mesh)):  # individual_polygon in polygon_structure:
            for point_index in range(0, len(self.base_mesh[individual_polygon_index])):
                self.transform_mesh[individual_polygon_index][point_index] = tuple_scaler(
                    linear_rotate_transform(self.base_mesh[individual_polygon_index][point_index], self.ship_angle),
                    self.mesh_scale)
        #Move(translate) transform mesh to the ship coordinates and store to translate mesh
        for individual_polygon_index in range(0, len(self.transform_mesh)):
            for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                self.translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                    [self.transform_mesh[individual_polygon_index][point_index],
                     (self.ship_center_x, self.ship_center_y)])    
        return

    def get_rotate_mesh(self): #Returns the rotated mesh
        return self.transform_mesh

    def get_final_mesh(self): #Returns the translated rotated mesh
        return self.translate_mesh
    
    def get_ship_coords(self): #Returns the ships centerpoint coordinates respective to the game screen
        return (self.ship_center_x,self.ship_center_y)
    
    def get_mesh_scaler(self):
        return self.mesh_scale

    def draw_ship(self,screen,color_tuple,light_source_tuple,location_tuple): #Given the screen, the color of the ship, light source location, and desired screen location, this function draws the ship to the screen with all the necessary light, color, and location calculations.
        if location_tuple != self.get_ship_coords:
            temp_translate_mesh = [[j for j in i] for i in self.base_mesh]
            for individual_polygon_index in range(0, len(self.transform_mesh)):
                for point_index in range(0, len(self.transform_mesh[individual_polygon_index])):
                    temp_translate_mesh[individual_polygon_index][point_index] = tuple_adder(
                        [self.transform_mesh[individual_polygon_index][point_index],
                         location_tuple])
            for single_polygon_index in range(0,len(self.translate_mesh)):
                pygame.draw.polygon(screen,
                    tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),temp_translate_mesh[single_polygon_index])
        else:
            for single_polygon_index in range(0,len(self.translate_mesh)):
                pygame.draw.polygon(screen,
                    tuple_scaler(color_tuple,light_multiplier_calculator(tuple_scaler(tuple_adder(self.transform_mesh[single_polygon_index]), 1 / 3),location_tuple, light_source_tuple)),self.translate_mesh[single_polygon_index])
        return

def main():
    pygame.init() #Initialize game screen

#Initilaize Game Variables
    #Screen variables
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Planettoids Beta v1.1")
    bg = pygame.image.load("background1.png") #NOTE: For future implementation we should load these images into sprites to speed up the draw commands
    #Light Source Variables
    light_source_x = 345 #screen_width // 2
    light_source_y = 332 #screen_height // 2
    #Title text objects
    font_object_title = pygame.font.Font('AmazDooMLeft.ttf', 100)
    text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (screen_width // 2, screen_height // 5)
    #Initialize Player Ship
    ship_mesh = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]
    player_ship = ship(screen_width // 2,screen_height // 2,ship_mesh)

#Main Gameplay Loop
    running = True #Main execution boolean
    while running == True:
        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT:
            running = False
            continue

        button = pygame.key.get_pressed()

        player_ship.frame(button,screen_width,screen_height)

    #Draw Operations
        #screen.fill((0, 0, 0)) #Prolly should have this turned off cause the background image kinda already refreshes the screen
        screen.blit(bg,(0,0))
        screen.blit(text_surface, text_surface_rect)
        # Draw Ship
        player_ship.draw_ship(screen,(0xFF,0,0xFF),(light_source_x, light_source_y),player_ship.get_ship_coords())
        player_ship.draw_ship(screen,(0xFF,0,0xFF),(light_source_x, light_source_y),tuple_adder([player_ship.get_ship_coords(),(70,0)]))

        pygame.time.Clock().tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()
