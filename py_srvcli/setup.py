from setuptools import setup, find_packages

package_name = 'py_srvcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Python service and client example with custom interface',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'server = py_srvcli.server:main',
            'client = py_srvcli.client:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/py_srvcli']),
        ('share/py_srvcli', ['package.xml']),
        ('share/py_srvcli/launch', ['launch/launch_all.py']),  # Launch dosyasını buraya ekledik
    ],
)
