from setuptools import setup, find_packages

package_name = 'shapes'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),  # Alt paketleri otomatik olarak bulur
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A package for drawing shapes with ROS2 Turtlesim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shapes = shapes.shapes:main',  # shapes.py dosyasındaki main() fonksiyonuna işaret eder
        ],
    },
   data_files=[
    ('share/ament_index/resource_index/packages', ['resource/shapes']),
    ('share/shapes', ['package.xml']),
    ('share/shapes/launch', ['launch/shapes_launch.py']),  # Launch dosyasını ekledik
],

    # Python bağımlılıkları için ament_python eklenmesi gerekiyor
    options={
        'build': {'build_base': 'build'}
    }
)
