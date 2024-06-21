# setup.py
from setuptools import setup

package_name = 'my_camera_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@domain.com',
    description='ROS 2 Camera Node Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = my_camera_package.camera_node:main',
            'camera_subscriber = my_camera_package.camera_subscriber:main',
        ],
    },
)
