#!/usr/bin/env python3
# coding: utf-8

import io
from setuptools import setup, find_packages


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="tfg_big_data_algorithms",
    version="0.1",
    description="Python's Tensorflow Graph Library",
    author="garciparedes",
    author_email="sergio@garciparedes.me",
    url="http://tfg_big_data_algorithms.readthedocs.io/en/latest/",
    download_url="https://github.com/garciparedes/tfg_big_data_algorithms",
    keywords=[
      "tfg", "bigdata", "tensorflow",
      "graph theory", "pagerank", "university of valladolid",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "matplotlib",
    ],
    tests_require=[
        "pytest"
    ],
    packages=find_packages('tfg_big_data_algorithms'),
    package_dir={'': 'tfg_big_data_algorithms'},
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Science/Research",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.5",
      "Programming Language :: Python :: Implementation :: CPython",
      "Topic :: Scientific/Engineering",
      "Topic :: Scientific/Engineering :: Physics",
    ],
    long_description=io.open('README.rst', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
)