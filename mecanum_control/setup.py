from setuptools import setup
from setuptools import find_packages
package_name = 'mecanum_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','odrive'],
    zip_safe=True,
    maintainer='mert',
    maintainer_email='mertsaadetcs@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=[],
    entry_points={
        'console_scripts': ['mecanum_control = mecanum_control.mecanum_control:main','serial_com = mecanum_control.serial_com:main'
        ],
    },
)
