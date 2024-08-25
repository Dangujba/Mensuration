import math
import matplotlib.pyplot as plt

def area(side):
    return (3 * math.sqrt(3) / 2) * side ** 2

def perimeter(side):
    return 6 * side

def draw(side):
    fig, ax = plt.subplots()
    angle = math.radians(60)
    points = [(side * math.cos(i * angle), side * math.sin(i * angle)) for i in range(6)]
    hexagon = plt.Polygon(points, fill=None, edgecolor='purple', linewidth=2)
    ax.add_artist(hexagon)
    ax.set_xlim(-side - 1, side + 1)
    ax.set_ylim(-side - 1, side + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Hexagon with side {side}")
    plt.grid(True)
    plt.show()
