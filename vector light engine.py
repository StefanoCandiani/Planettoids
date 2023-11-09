import pygame
import random
import math

def tuple_adder(tuple_list):
    return_tup = (0,0)
    for tup in tuple_list:
        return_tup = (return_tup[0]+tup[0],return_tup[1]+tup[1])
    return return_tup

def tuple_scaler(input_tuple,scalar):
    return_tuple = tuple()
    for i in range(0,len(input_tuple)):
        return_tuple += tuple([input_tuple[i] * scalar])
    return return_tuple

def tuple_x_reflector(input_tuple):
    return (input_tuple[0],input_tuple[1]*-1)

def ext_atan(input_tuple):
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

def linear_rotate_transform(input_tuple,rotate_angle):
    return (math.cos(rotate_angle)*input_tuple[0]-math.sin(rotate_angle)*input_tuple[1],math.sin(rotate_angle)*input_tuple[0]+math.cos(rotate_angle)*input_tuple[1])

def light_multiplier_calculator(tri_center_tuple,object_center_tuple,light_tuple):
    center_angle = angle_rebounder(ext_atan(tri_center_tuple))
    light_angle = angle_rebounder(ext_atan(tuple_adder([object_center_tuple,tuple_scaler(light_tuple,-1)])))
    difference_angle = angle_rebounder((center_angle - light_angle))
    #return math.fabs(-(math.cos(difference_angle/2)) + 1)
    #return math.fabs( -1*math.fabs(difference_angle/math.pi) + 1)
    return math.fabs(difference_angle/math.pi)

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

class ship():
    def __init__():
        pass

def main():
    pygame.init() #Initialize game screen

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Programming fundamentals")

    #light_source_x = screen_width // 2
    light_source_x = 345
    #light_source_y = screen_height // 2
    light_source_y = 332

    font_object_title = pygame.font.Font('AmazDooMLeft.ttf', 100)
    text_surface = font_object_title.render('PLANETTOIDS', True, (255, 255, 255))
    text_surface_rect = text_surface.get_rect()
    text_surface_rect.center = (screen_width // 2, screen_height // 5)

    font_object_debug = pygame.font.Font('TI-83P Font.ttf', 32)
    text_surface_debug = font_object_debug.render("0", True, (255, 255, 255))
    text_surface_rect_debug = text_surface_debug.get_rect()
    text_surface_rect_debug.center = (50, 20)

    character_x_pos = screen_width // 2  # 100
    character_y_pos = screen_height // 2  # 100
    character_width = 50
    character_height = 50

    ball_angle_x = 0
    ball_angle_z = 0
    ball_traject_radius = 100

    polygon_center_x = screen_width // 2
    polygon_center_y = screen_height // 2

    # polygon_structure = [[(0,0),(1,0),(0,1)],[(0,0),(-1,0),(0,-1)],[(0,0),(1,0),(0,-1)],[(0,0),(-1,0),(0,1)]]
    # polygon_structure = [[(0,0),(2,-1),(2,1)],[(0,0),(2,1),(1,2)],[(0,0),(0,2),(1,2)],[(0,0),(1,2),(-1,2)],[(0,0),(-1,2),(-2,1)],[(0,0),(-2,1),(-2,-1)],[(0,0),(-2,-1),(-1,-2)],[(0,0),(-1,-2),(1,-2)],[(0,0),(1,-2),(2,-1)]]
    #polygon_structure = [[(0, 0), linear_rotate_transform((1, 0), 2 * math.pi * (i / 16)),linear_rotate_transform((1, 0), 2 * math.pi * ((i + 1) / 16))] for i in range(1, 16 + 1)]
    # polygon_structure = [[(0,0),linear_rotate_transform((1,0),2*math.pi*(i/32)),linear_rotate_transform((1,0),2*math.pi*((i+1)/32))] for i in range(1,32+1)]
    polygon_structure = [[(-0.5,0),(-math.sqrt(2)/2,math.sqrt(2)/2),(1,0)],[(-0.5,0),(-math.sqrt(2)/2,-math.sqrt(2)/2),(1,0)]]

    polygon_current_transform = [[j for j in i] for i in polygon_structure]
    polygon_current_instantiation = [[j for j in i] for i in polygon_structure]
    polygon_angle = 0
    polygon_scale = 20
    polygon_velocity = 0
    polygon_angular_velocity = 0

    bg = pygame.image.load("background1.png")

    running = True
    while running == True:
        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT:
            running = False
            continue

        button = pygame.key.get_pressed()

 # Angle Moving
        if button[pygame.K_LEFT]:
            #polygon_angular_velocity -= math.pi / 50
            polygon_angular_velocity = -math.pi/25
        if button[pygame.K_RIGHT]:
            #polygon_angular_velocity += math.pi / 50
            polygon_angular_velocity = math.pi/25

        # Angle Rollover
        if polygon_angular_velocity > 0:
            polygon_angular_velocity -= math.pi / 400
        if polygon_angular_velocity < 0:
            polygon_angular_velocity += math.pi / 400
            
        if round(polygon_angular_velocity,2)==0:
            polygon_angular_velocity = 0

        if polygon_angular_velocity > math.pi/25:
            polygon_angular_velocity = math.pi/25
        if polygon_angular_velocity < -math.pi/25:
            polygon_angular_velocity = -math.pi/25
        
        if button[pygame.K_UP]:
            polygon_velocity += 0.3
        else:
            polygon_velocity -= 0.1
        if polygon_velocity > 6:
            polygon_velocity = 5
        if polygon_velocity < 0:
            polygon_velocity = 0

        #if button[pygame.K_LEFT]:
        #    character_x_pos -= 1
        #if button[pygame.K_RIGHT]:
        #    character_x_pos += 1
        #if button[pygame.K_UP]:
        #    character_y_pos -= 1
        #if button[pygame.K_DOWN]:
        #    character_y_pos += 1

        ball_angle_x += math.pi / 100 / 4
        if ball_angle_x > 2 * math.pi:
            ball_angle_x = -2 * math.pi
        ball_angle_z += math.pi / 100 / 4
        if ball_angle_z > math.pi:
            ball_angle_z = -math.pi

        polygon_angle += polygon_angular_velocity
        polygon_angle = angle_rebounder(polygon_angle)
        character_x_pos += polygon_velocity*math.cos(polygon_angle)
        character_y_pos += polygon_velocity*math.sin(polygon_angle)

        if character_x_pos - polygon_scale < 0:
            character_x_pos = 0 + polygon_scale
        if character_y_pos - polygon_scale < 0:
            character_y_pos = 0 + polygon_scale
        if character_x_pos + polygon_scale > screen_width:
            character_x_pos = screen_width - polygon_scale
        if character_y_pos + polygon_scale > screen_height:
            character_y_pos = screen_height - polygon_scale

        for individual_polygon_index in range(0, len(polygon_structure)):  # individual_polygon in polygon_structure:
            for point_index in range(0, len(polygon_structure[individual_polygon_index])):
                polygon_current_transform[individual_polygon_index][point_index] = tuple_scaler(
                    linear_rotate_transform(polygon_structure[individual_polygon_index][point_index], polygon_angle),
                    polygon_scale)

        polygon_center_x = character_x_pos
        polygon_center_y = character_y_pos

        for individual_polygon_index in range(0, len(polygon_current_transform)):
            for point_index in range(0, len(polygon_current_transform[individual_polygon_index])):
                polygon_current_instantiation[individual_polygon_index][point_index] = tuple_adder(
                    [polygon_current_transform[individual_polygon_index][point_index],
                     (polygon_center_x, polygon_center_y)])

        # Draw Commands
        #screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        screen.blit(text_surface, text_surface_rect)
        text_surface_debug = font_object_debug.render(str(polygon_angle) + " " + str((ext_atan(
            tuple_adder([(polygon_center_x, polygon_center_y), tuple_scaler((light_source_x, light_source_y), -1)])))),
                                                      True, (255, 255, 255))
        screen.blit(text_surface_debug, text_surface_rect_debug)
        #pygame.draw.circle(screen, (0x00, 0x00, 0xFF), (screen_width // 2, screen_height // 2), 90)
        #if ball_angle_z > 0:
        #    pygame.draw.circle(screen, (0xFF * math.fabs(math.sin(ball_angle_z)), 255 * math.fabs(math.sin(ball_angle_z)),255 * math.fabs(math.sin(ball_angle_z))),(screen_width // 2 + ball_traject_radius * math.cos(ball_angle_x), screen_height // 2),10 * (1 + math.sin(ball_angle_z)))
        #pygame.draw.rect(screen,tuple([random.randint(0, 255) for i in range(0, 3)]),(character_x_pos, character_y_pos, character_width, character_height))

        # Draw Polygon
        for single_polygon_index in range(0,len(polygon_current_instantiation)):
            pygame.draw.polygon(screen,
                tuple_scaler((0,0,0xFF),light_multiplier_calculator(tuple_scaler(tuple_adder(polygon_current_transform[single_polygon_index]), 1 / 3),(polygon_center_x, polygon_center_y), (light_source_x, light_source_y))),
                polygon_current_instantiation[single_polygon_index])

            # pygame.draw.circle(screen,[(0xFF,0,0),(0,0xFF,0),(0,0,0xFF),(0,0xFF,0xFF),(0xFF,0,0xFF),(0xFF,0xFF,0),(0x7F,0x7F,0x7F),(0xFF,0x7F,0),(0xFF,0x7F,0),(0,0,0xFF)][1-single_polygon_index],tuple_adder([tuple_scaler(tuple_adder(polygon_current_transform[single_polygon_index]),1/3),(polygon_center_x,polygon_center_y)]),5)

        #pygame.time.Clock().tick(60)
        pygame.display.flip()

        # (255*math.floor(math.sin(ball_angle_z))


if __name__ == "__main__":
    main()