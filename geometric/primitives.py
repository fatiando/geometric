# pylint: skip-file
"""
Geometric primitives
"""


class GeometricObject():
    """
    Something.

    Parameters
    ----------
    bounds : list
        Boundaries
    other : array
        Something else

    Attributes
    ----------
    density : float
        A physical property.

    """

    def some_method(self, bla):
        """
        Some documentation

        Parameters
        ----------
        bla : str
            Some parameter

        """
        return bla*2

    def other_method(self, value):
        """
        Some other documentation

        Parameters
        ----------
        value : str
            Some parameter

        """
        return value/2


def some_function(value):
    """
    A sample function.

    Parameters
    ----------
    value : array
        A value.


    Examples
    --------

    >>> some_function(30)
    60

    """
    return value*2
