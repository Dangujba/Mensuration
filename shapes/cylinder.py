import math
import matplotlib.pyplot as plt

def volume(radius, height):
    return math.pi * radius ** 2 * height

def surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def draw(radius, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot_surface(x, y, z, color='cyan', edgecolor='black')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Height')
    plt.title(f"Cylinder with radius {radius} and height {height}")
    plt.show()
