import math
import matplotlib.pyplot as plt

def area(side):
    return 2 * (1 + math.sqrt(2)) * side ** 2

def perimeter(side):
    return 8 * side

def draw(side):
    fig, ax = plt.subplots()
    angle = math.radians(45)
    points = [(side * math.cos(i * angle), side * math.sin(i * angle)) for i in range(8)]
    octagon = plt.Polygon(points, fill=None, edgecolor='brown', linewidth=2)
    ax.add_artist(octagon)
    ax.set_xlim(-side - 1, side + 1)
    ax.set_ylim(-side - 1, side + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Octagon with side {side}")
    plt.grid(True)
    plt.show()
