import matplotlib.pyplot as plt

def area(side):
    return side ** 2

def perimeter(side):
    return 4 * side

def draw(side):
    fig, ax = plt.subplots()
    square = plt.Polygon([[-side/2, -side/2], [-side/2, side/2], [side/2, side/2], [side/2, -side/2]], 
                         fill=None, edgecolor='red', linewidth=2)
    ax.add_artist(square)
    ax.set_xlim(-side/2 - 1, side/2 + 1)
    ax.set_ylim(-side/2 - 1, side/2 + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Square with side {side}")
    plt.grid(True)
    plt.show()

draw(4)