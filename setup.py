#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages
import george_tools as distmeta

setup(
    version="0.0.2",
    description="",
    author="george",
    author_email="goblin.george@gmail.com",
    url="http://georgeli.tk",
    name='george_tools',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sympy']
)
