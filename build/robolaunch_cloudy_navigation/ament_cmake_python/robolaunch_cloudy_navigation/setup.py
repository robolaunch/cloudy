from setuptools import find_packages
from setuptools import setup

setup(
    name='robolaunch_cloudy_navigation',
    version='0.0.0',
    packages=find_packages(
        include=('robolaunch_cloudy_navigation', 'robolaunch_cloudy_navigation.*')),
)
