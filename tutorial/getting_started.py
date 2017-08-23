"""
Getting started
---------------

This is a sample tutorial page.
"""

###############################################################################
# Start by importing stuff.

import matplotlib.pyplot as plt
import numpy as np


###############################################################################
# Create some random data.

np.random.seed(42)
x = np.random.uniform(0, 100, 100)
y = np.sin(x) + 10
print(x, y)

###############################################################################
# Make the plot.

plt.figure()
plt.plot(x, y)
plt.tight_layout()
plt.show()
