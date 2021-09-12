import math 
from random import *

def function(x, y):
    f = 4 * math.exp(-math.pow(x, 2) - math.pow(y, 2) + 2 * (x + y - 1))
    f = f + math.exp(-math.pow(x - 3, 2) - math.pow(y - 3, 2))
    f = f + math.exp(-math.pow(x + 3, 2) - math.pow(y - 3, 2))
    f = f + math.exp(-math.pow(x - 3, 2) - math.pow(y + 3, 2))
    f = f + math.exp(-math.pow(x + 3, 2) - math.pow(y + 3, 2))

    return f


def maior(x, y):
    if x > y: 
        return x
    else: 
        return y


def find_prox(x, y, z_ini):
    z1 = function(x - 0.01, y - 0.01)
    prox = maior(z1, z_ini)
    z2 = function(x + 0.01, y - 0.01)
    prox = maior(z2, prox)
    z3 = function(x - 0.01, y + 0.01)
    prox = maior(z3, prox)
    z4 = function(x + 0.01, y + 0.01)
    prox = maior(z4, prox)

    return prox


def find_max_local(max):
    for i in range(0, 4000):    
        x = uniform(-10, 10)
        y = uniform(-10, 10)
        z = find_prox(x, y, max)
        if z > max:
            max = z
    return max


x = uniform(-10, 10)
y = uniform(-10, 10)
max_global = function(x, y)

for i in range(0, 10):
    max_global = maior(max_global, find_max_local(max_global))
    print("--" + str(max_global))
    
# print(max_global) 