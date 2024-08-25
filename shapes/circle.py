import math
import matplotlib.pyplot as plt

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

def draw(radius):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=None, edgecolor='blue', linewidth=2)
    ax.add_artist(circle)
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Circle with radius {radius}")
    plt.grid(True)
    plt.show()
