"""
Some gallery plot
-----------------

This is a sample gallery plot.
"""
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.uniform(0, 100, 100)
y = np.sin(x) + 10

plt.figure()
plt.plot(x, y)
plt.tight_layout()
plt.show()

from geometric.primitives import GeometricObject, some_function

obj = GeometricObject()
print(some_function(10))
