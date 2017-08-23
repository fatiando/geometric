"""
Geometric primitives
"""
import numpy as np

from .base import WithPhysicalProperties


class Sphere(WithPhysicalProperties):
    """
    A sphere.
    """

    def __init__(self, center, radius, **properties):
        super().__init__(**properties)
        self.center = center
        "Coordinates of the center of the sphere (EW, NS, vertical) in meters"
        self.radius = radius
        "The radius of the sphere in meters"
