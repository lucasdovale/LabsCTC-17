import random 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import Axes3D, art3d
import numpy as np

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Plot:
    def __init__(self, function):
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)

        X, Y = np.meshgrid(x, y)
        Z = function(X, Y)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.plot_surface(X, Y, Z, color = 'k')
    
    def add_point(self, point, color):
        p = Circle((point.x, point.y), 0.2, ec=color, fc="none")
        self.ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=point.z, zdir="z")

    def show(self):
        plt.show()

def f(x, y):
    f = 4 * np.exp(-x**2 - y**2 + 2 * (x + y - 1))
    f = f + np.exp(-(x + 3)**2 - (y - 3)**2)
    f = f + np.exp(-(x - 3)**2 - (y + 3)**2)
    f = f + np.exp(-(x - 3)**2 - (y - 3)**2)
    f = f + np.exp(-(x + 3)**2 - (y + 3)**2)

    return f

my_plot = Plot(f)


def simmulated_annealing(search_space, function, T):
    scale = np.sqrt(T)
    start_x = np.random.choice(search_space)
    start_y = np.random.choice(search_space)

    x = start_x * 1
    y = start_y * 1
    z = function(x, y)

    for i in range(10000):
        # next_x = x + np.random.normal() * scale
        # next_y = y + np.random.normal() * scale
        next_x = np.random.uniform(-5, 5)
        next_y = np.random.uniform(-5, 5)
        next_z = function(next_x, next_y)
        if next_x > 5 or next_x < -5 or next_y > 5 or next_y < -5 or np.log(np.random.rand()) * T > (next_z - z):
            next_x = x
            next_y = y
            next_z = z
        x = next_x
        y = next_y
        z = next_z
        T = 0.99 * T # reducing temperature by 1% each iteration
        p = Point(x, y, z)
        my_plot.add_point(p, color='b')
        

    return x, y, z

space_x = np.linspace(-5, 5, 50)
space_y = np.linspace(-5, 5, 50)
x_aux, y_aux, z_aux = simmulated_annealing(space_x, f, T = 100)

q = Point(x_aux, y_aux, z_aux)
my_plot.add_point(q, color='r')

my_plot.show()