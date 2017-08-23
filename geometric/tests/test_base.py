"""
Test the base classes.
"""
import numpy.testing as npt

from ..base import WithPhysicalProperties


def test_properties_as_attributes():
    "Set physical properties as attributes"
    obj = WithPhysicalProperties()
    obj.density = 10
    assert obj.density == 10
    obj.magnetization = [1, 2, 3]
    npt.assert_allclose(obj.magnetization, [1, 2, 3])


def test_properties_init():
    "Set physical properties through init"
    obj = WithPhysicalProperties(density=10, magnetization=[1, 2, 3])
    assert obj.density == 10
    npt.assert_allclose(obj.magnetization, [1, 2, 3])


def test_properties_method():
    "Set physical properties through the set_properties method"
    obj = WithPhysicalProperties().set_properties(
        density=10, magnetization=[1, 2, 3])
    assert obj.density == 10
    npt.assert_allclose(obj.magnetization, [1, 2, 3])
