from setuptools import setup
from pathlib import Path

parent_dir = Path(__file__).resolve().parent

setup(
    name='prettymaps',
    version='1.0.0',    
    description='A simple python library to draw pretty maps from OpenStreetMap data',
    url='https://github.com/marceloprates/prettymaps',
    author='Marcelo Prates',
    author_email='marceloorp@gmail.com',
    license='MIT License',
    packages=['prettymaps'],
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),

    classifiers=[
        'Intended Audience :: Science/Research',
    ],
)    
