"""
Build and install the project.

Uses versioneer to manage version numbers using git tags.
"""
from setuptools import setup, find_packages

import versioneer


with open("README.rst") as f:
    readme = ''.join(f.readlines())

with open("requirements.txt") as f:
    requirements = [line.strip() for line in f.readlines()]

setup_args = dict(
    name='geometric',
    fullname='geometric',
    description='Geometric objects with physical properties',
    long_description=readme,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Leonardo Uieda',
    author_email='leouieda@gmail.com',
    license='BSD License',
    url='https://github.com/fatiando/geometric',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
    ],
    keywords='',
    platforms='Any',
    install_requires=requirements,
    scripts=[],
    packages=find_packages(exclude=['doc', 'ci']),
    package_data={
        'geometric.tests': ['data/*', 'baseline/*'],
    },
)

if __name__ == '__main__':
    setup(**setup_args)
