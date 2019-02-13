"""
Script to build the pywasp_flow

Fortran modules should be added at the top of the package in the config function.
There should be a number of examples.

Python modules are added to the cfg object, as are command line programs.
"""
from setuptools import setup
from numpy.distutils.core import setup, Extension

########################
# Add the WAsP Core code
########################
# Set the name of the wasp core module for building the extensions
adder = Extension('conda_build_fort.adder_mod.adder',
    sources=[
             'module/adder.pyf',
             'module/Types_mod.f90',
             'module/adder.f90'
    ]
)

if __name__ == "__main__":
    metadata = dict(
        name='conda_build_fort',
        version='0.0.1',
        description='Test for building fortran and python',
        long_description='Test for building fortran and python',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: PRIVATE',
            'Programming Language :: Python :: 3.5'],
        packages = ['conda_build_fort', 'conda_build_fort.adder_mod'],
        ext_modules=[adder],
        install_requires=['numpy']
        )

    setup(**metadata)
