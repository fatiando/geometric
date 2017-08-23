"""
Geometric primitives like prisms, spheres, etc.
"""
import numpy as np


class WithPhysicalProperties():
    """
    Base class for all geometric objects that have physical properties.
    """

    def __init__(self, **properties):
        self._density = None
        self._magnetization = None
        self._induced_magnetization = None
        self._remanent_magnetization = None
        self._susceptibility = None
        self.set_properties(**properties)

    def set_properties(self, **properties):
        """
        Set the physical properties
        """
        for name, value in properties.items():
            setattr(self, name, value)
        return self

    @property
    def volume(self):
        """
        The volume in m^3
        Must be implemented by the child class in order to have access to the
        'mass' property.
        """
        return self._density

    @property
    def density(self):
        "The density in kg/m^3"
        return self._density

    @density.setter
    def density(self, value):
        "Set the density"
        self._density = value

    @property
    def magnetization(self):
        "The total magnetization in A/m"
        return self._magnetization

    @magnetization.setter
    def magnetization(self, value):
        "Set the magnetization"
        value_arr = np.atleast_1d(value)
        assert value_arr.shape == (3, ), \
            "Magnetization must be 3-component vector: {}".format(value)
        self._magnetization = value_arr
