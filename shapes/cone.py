import math

def volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

def surface_area(radius, slant_height):
    return math.pi * radius * (radius + slant_height)
