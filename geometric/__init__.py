"""
Create, manipulate, and visualize geometric objects with physical properties
"""
from ._version import get_versions
from .primitives import Sphere


# Set the version number using versioneer
__version__ = get_versions()['version']
del get_versions


def test(verbose=True, coverage=False):
    """
    Run the test suite.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests. If you
    haven't already, you can install it with `conda
    <http://conda.pydata.org/>`__ or `pip <https://pip.pypa.io/en/stable/>`__.

    Parameters
    ----------

    verbose : bool
        If ``True``, will print extra information during the test run.
    coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.

    Raises
    ------

    ValueError
        If pytest returns a non-zero error code indicating that some tests have
        failed.

    """
    import pytest
    args = []
    if verbose:
        args.append('-vv')
    if coverage:
        args.append('--cov=gmt')
        args.append('--cov-report=term-missing')
    args.append('--doctest-modules')
    args.append('--mpl')
    args.append('--pyargs')
    args.append('geometric')
    status = pytest.main(args)
    if status != 0:
        raise ValueError("Some tests have failed.")
