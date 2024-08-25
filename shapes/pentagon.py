import math
import matplotlib.pyplot as plt

def area(side):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2

def perimeter(side):
    return 5 * side

def draw(side):
    fig, ax = plt.subplots()
    angle = math.radians(72)
    points = [(side * math.cos(i * angle), side * math.sin(i * angle)) for i in range(5)]
    pentagon = plt.Polygon(points, fill=None, edgecolor='green', linewidth=2)
    ax.add_artist(pentagon)
    ax.set_xlim(-side - 1, side + 1)
    ax.set_ylim(-side - 1, side + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Pentagon with side {side}")
    plt.grid(True)
    plt.show()
