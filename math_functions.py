"""
Created By: Phoenix Cushman, Stefano Candiani, Joel Kubinsky, Danush Singla
Date: 11/3/2023 - XX/XX/2023
Project: Project 4: Group Game, "Planettoids"
File: math_functions
"""
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

def tuple_mag(input_tuple):
    running_sum = int(0)
    for i in input_tuple:
        running_sum += i ** 2
    return math.sqrt(running_sum)

#def tuple_normalize(input_tuple):
#    tuple_scaler(input_)

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