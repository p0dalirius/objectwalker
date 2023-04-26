#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : setup.py
# Author             : Podalirius (@podalirius_)
# Date created       : 17 Jul 2022

import setuptools

long_description = """e"""

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [x.strip() for x in f.readlines()]

setuptools.setup(
    name="objectwalker",
    version="1.9",
    description="",
    url="https://github.com/p0dalirius/objectwalker",
    author="Podalirius",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="podalirius@protonmail.com",
    packages=["objectwalker", "objectwalker.filters"],
    package_data={'objectwalker': ['objectwalker/', 'objectwalker/filters/']},
    include_package_data=True,
    license="GPL2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': ['objectwalker=objectwalker.__main__:main']
    }
)
