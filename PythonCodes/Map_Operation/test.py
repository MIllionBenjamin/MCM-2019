#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:50:58 2019

@author: apple
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:17:13 2015

@author: Eddy_zheng
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)

X, Y = np.meshgrid(X, Y)
print(X, Y)
R = np.sqrt(X**2 + Y**2)
print(R)
print(type(R))
Z = np.sin(R)
print(Z)
print(type(Z))

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
