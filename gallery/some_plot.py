"""
Some gallery plot
-----------------

This is a sample gallery plot.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 100)
y = np.sin(x) + 10

plt.figure()
plt.plot(x, y)
plt.tight_layout()
plt.show()
