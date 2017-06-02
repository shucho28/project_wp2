from setuptools import setup

setup(
    name='wp',
    packages=['wp'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)