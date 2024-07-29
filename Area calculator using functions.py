# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:15:53 2024

@author: Andrew
"""

def tri_area ():
    base = float(input("Input the length of the base: "))

    height = float(input("Input the height of the base: "))
    
    
    area = base * height * 0.5
    print(f"The area of the triangle is {area} units squared.")

def rec_area ():
    length = float(input("Input the length of the rectangle: "))
    width = float(input("Input the width of the rectangle: "))
    
    area = length * width
    print(f"The area of the rectangle is {area} units squared,")

def cir_area ():
    radius = float(input("Input the radius of the circle: "))
    
    import math
    
    area = math.pi * radius * radius
    
    print (f"The area of the circle is {area} units squared")


print("This is a program that calculates the area of a shape")

shape = ""

while shape != 0:
    shape = input("For triangle use 1, for rectangle use 2, for circle use 3 and to quit 0: ")
    if shape == "0":
        break 
    
    elif shape == "1":
        tri_area ()
        
    elif shape == "2":
        rec_area ()
        
    elif shape == "3":
        cir_area ()
               
    else:
        print("invalid input")
       


    
    