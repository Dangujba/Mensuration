import math
import matplotlib.pyplot as plt

def area(base, height):
    return 0.5 * base * height

def perimeter(a, b, c):
    return a + b + c

def draw(a, b, c):
    fig, ax = plt.subplots()
    # Use the law of cosines to determine the coordinates of each vertex
    A = (0, 0)
    B = (a, 0)
    Cx = (b**2 + a**2 - c**2) / (2 * a)
    Cy = math.sqrt(b**2 - Cx**2)
    triangle = plt.Polygon([A, B, (Cx, Cy)], fill=None, edgecolor='orange', linewidth=2)
    ax.add_artist(triangle)
    ax.set_xlim(-1, a + 1)
    ax.set_ylim(-1, max(Cy, b) + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Triangle with sides {a}, {b}, {c}")
    plt.grid(True)
    plt.show()
