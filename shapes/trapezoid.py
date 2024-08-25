import matplotlib.pyplot as plt

def area(a, b, height):
    return 0.5 * (a + b) * height

def perimeter(a, b, c, d):
    return a + b + c + d

def draw(a, b, height):
    fig, ax = plt.subplots()
    x = [-a/2, a/2, b/2, -b/2]
    y = [0, 0, height, height]
    trapezoid = plt.Polygon(list(zip(x, y)), fill=None, edgecolor='blue', linewidth=2)
    ax.add_artist(trapezoid)
    ax.set_xlim(-max(a, b) / 2 - 1, max(a, b) / 2 + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    plt.title(f"Trapezoid with bases {a}, {b} and height {height}")
    plt.grid(True)
    plt.show()
