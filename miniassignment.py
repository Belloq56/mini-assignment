import numpy as np
from math import e
from matplotlib import pyplot as pp

def Ex(x):
    return 10*np.cos((np.pi*x)/2)*e**(-0.4*x)
x = []
y = []
for i in range(201):
    x.append(i*0.1)
    y.append(Ex(x[i]))

pp.plot(x,y)
pp.xlabel('x position (m)')
pp.ylabel('Electric field (V/m)')
