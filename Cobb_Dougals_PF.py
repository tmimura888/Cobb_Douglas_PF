# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def f(k, l):
    return k**(1/2) * l**(1/2)

k = np.arange(0, 100, 2.5)
l = np.arange(0, 100, 2.5)

K, L = np.meshgrid(k, l)
Y = f(K, L)

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("K")
ax.set_ylabel("L")
ax.set_zlabel("Y")


ax.contour(K, L, Y, 15) 
plt.show()

#wire  frame is one of the other types of graph plotting

import reader
help(reader)

from reader import feed
feed.get_titles
