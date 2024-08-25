import matplotlib.pyplot as plt

def area(base, height):
    return base * height

def perimeter(a, b):
    return 2 * (a + b)

def draw(base, height):
    fig, ax = plt.subplots()
    x = [-base / 2, base / 2, base / 2 + height / 2, -base / 2 + height / 2]
    y = [0, 0, height, height]
    parallelogram = plt.Polygon(list(zip(x, y)), fill=None, edgecolor='purple', linewidth=2)
    ax.add_artist(parallelogram)
    ax.set_xlim(-base, base + height)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Parallelogram (base={base}, height={height})")
    plt.grid(True)
    plt.show()
