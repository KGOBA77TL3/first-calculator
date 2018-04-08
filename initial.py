# This script can compute the area of a circle and triangle
# User will select a shape
# Script will calculate the area of that shape
# Script will print the area


class Area_calculator:
    print("The Area Calculator is now live!")

# Universal definitions:
pi = 3.14159    

# Add more shapes:
option = input("What shape are you calculating the area of? Enter C for Circle, T for Triangle, or E for an Ellipse: ")


# Defining the input
# Making user input the radius into a float function to use for calculations. input() will store the answer as a string
# which can't be used for calculations

if option == "C":
    radius = float(input(
        "Enter the radius of the circle. Do not input units such as ft., meters., etc:  "))
    area_cir = float(pi * radius**2.)
elif option == "T":
    base = float(input(
        "Enter the base of the triangle. Do not input units such as ft., meters., etc:  "))
    height = float(input(
        "Enter the overall height of the triangle. Do not input units such as ft., meters., etc:  "))
    area_tri = float(1 / 2 * (base * height))
elif option == "E":
    
    print ("When finding the area of an Ellipse, the a-variable is the point farthest from the orgin on the x-axis. The b-variable is the point farthest from the orgin on the y-axis.")
    
    a = float(input("Enter the 'a' point. The 'a' point is the point farthest from the orgin on the x-axis. Do not input units such as ft., meters., etc: "))
    b = float(input("Enter the 'b' point. The 'b' point is the point farthest from the orgin on the y-axis. Do not input units such as ft., meters., etc: "))

    area_ellipse = pi * a * b
         
#else:
    #print("Sorry, you have selected a shape not within the calculators parameters. Please use C for circle or T for triangle. You MUST use capital letters.")


# str.format() using {} for variable substitutions
if option == "C":
    print("The area of the circle is: {}".format(area_cir))
if option == "T":
    print("The area of the triangle is: {}".format(area_tri))
if option == "E":
    print("The area of the ellipse is: {}".format(area_ellipse))    

