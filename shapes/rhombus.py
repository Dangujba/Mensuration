import math
import matplotlib.pyplot as plt

def area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def perimeter(side):
    return 4 * side

def draw(diagonal1, diagonal2):
    fig, ax = plt.subplots()
    x = [-diagonal1 / 2, 0, diagonal1 / 2, 0]
    y = [0, diagonal2 / 2, 0, -diagonal2 / 2]
    rhombus = plt.Polygon(list(zip(x, y)), fill=None, edgecolor='blue', linewidth=2)
    ax.add_artist(rhombus)
    ax.set_xlim(-diagonal1 / 2 - 1, diagonal1 / 2 + 1)
    ax.set_ylim(-diagonal2 / 2 - 1, diagonal2 / 2 + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Rhombus (diagonals={diagonal1}, {diagonal2})")
    plt.grid(True)
    plt.show()
