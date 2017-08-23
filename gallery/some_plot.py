"""
Some gallery plot
-----------------

This is a sample gallery plot.
"""
import matplotlib.pyplot as plt
import numpy as np

from geometric import Sphere

sphere = Sphere(center=[1, 2, 3], radius=10)

np.random.seed(42)
x = np.random.uniform(0, 100, 100)
y = np.sin(x) + 10

plt.figure()
plt.plot(x, y)
plt.tight_layout()
plt.show()
