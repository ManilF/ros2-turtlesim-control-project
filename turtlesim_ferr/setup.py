from setuptools import find_packages, setup

package_name = 'turtlesim_ferr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Manil Ferr',
    maintainer_email='ferrm1@mcmaster.ca',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_teleop_key = turtlesim_ferr.turtle_teleop_key:main',
            'turtle_repeater = turtlesim_ferr.turtle_repeater:main',
        ],
    },
)
