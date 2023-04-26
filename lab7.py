# Program To Calc Area,
# Credits: Dhruv , XII-D

import math 

def result_of_shape(shape):
    if shape == "square":
        type_of_calc = str(input("area or peri: "))
        side = int(input("Side: "))
        if type_of_calc == "area":
            print(f"Area of Square : {side**2}")
        elif type_of_calc == "peri":
            print(f"Peri of Square : {side*4}")
    elif shape == "rectangle":
        type_of_calc = str(input("area or peri: "))
        length = int(input("L: "))
        breadth = int(input("B: "))

        if type_of_calc == "area":
            print(f"Area of rectangle : {length*breadth}")
        elif type_of_calc == "peri":
            print(f"Peri of rectangle : {2*(length+breadth)}")
    elif shape == "circle":
        type_of_calc = str(input("area or peri: "))
        radius = int(input("radius: "))
        if type_of_calc == "area":
            print(f"Area of circle : {math.pi*(radius**2)}")
        elif type_of_calc == "peri":
            print(f"Peri of circle : {2*math.pi*(radius**2)}")
    elif shape=="triangle":
        type_of_calc = str(input("area or peri: "))
        height = int(input("H: "))
        breadth = int(input("B: "))
        if type_of_calc == "area":
            print(f"Area of tri : {(1/2)*height*breadth}")
        elif type_of_calc == "peri":
            side = int(input("S: "))
            print(f"Peri of tri : {height+breadth+side}")
    elif shape=="cylinder":
        type_of_calc = str(input("area or peri: "))
        radius = int(input("R: "))
        height = int(input("H: "))
        if type_of_calc == "area":
            # 2πrh +2πr2
            print(f"Area of cylinder: {2*math.pi*radius*height + 2*math.pi*radius*2}")
        elif type_of_calc == "peri":
            print(f"Peri of cylinder : {2*(2*radius+height)}")

shape = str(input("Shape: "))
result_of_shape(shape)