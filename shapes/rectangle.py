import matplotlib.pyplot as plt

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

def draw(length, width):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((-length/2, -width/2), length, width, fill=None, edgecolor='red', linewidth=2)
    ax.add_artist(rectangle)
    ax.set_xlim(-length, length)
    ax.set_ylim(-width, width)
    ax.set_aspect('equal', 'box')
    plt.title(f"Rectangle (length={length}, width={width})")
    plt.grid(True)
    plt.show()
