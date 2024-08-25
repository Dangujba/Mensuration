import math
import matplotlib.pyplot as plt

def area(a, b):
    return math.pi * a * b

def circumference(a, b):
    return math.pi * (3*(a + b) - math.sqrt((3*a + b)*(a + 3*b)))

def draw(a, b):
    fig, ax = plt.subplots()
    ellipse = plt.Ellipse((0, 0), 2*a, 2*b, fill=False, edgecolor='brown', linewidth=2)
    ax.add_artist(ellipse)
    ax.set_xlim(-a - 1, a + 1)
    ax.set_ylim(-b - 1, b + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Ellipse with axes {a}, {b}")
    plt.grid(True)
    plt.show()
