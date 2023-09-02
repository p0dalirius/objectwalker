#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : setup.py
# Author             : Podalirius (@podalirius_)
# Date created       : 17 Jul 2022

import setuptools

long_description = """
<p align="center">
    A python module to explore the object tree to extract paths to interesting objects in memory.
    <br>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/objectwalker">
    <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
    <a href="https://www.youtube.com/c/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/UCF_x5O7CSfr82AfNVTKOv_A?style=social"></a>
    <br>
</p>

## Features

 - [x] Python module to use in pdb after a `breakpoint()`.
 - [x] Standalone tool to explore paths in python modules.
 - [x] Multiple built-in filters.
 - [x] Possibility to implement custom filters and pass them to ObjectWalker().

## Installation

You can now install it from pypi with this command:

```
sudo python3 -m pip install objectwalker
```

## Example commands

 + We want to find all the paths to the `os` module in the module `jinja2`:
    ```
    objectwalker -m jinja2 --filter-object-is-module os --max-depth 15
    ```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.
"""

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [x.strip() for x in f.readlines()]

setuptools.setup(
    name="objectwalker",
    version="2.2.0",
    description="",
    url="https://github.com/p0dalirius/objectwalker",
    author="Podalirius",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="podalirius@protonmail.com",
    packages=["objectwalker", "objectwalker.filters"],
    package_data={'objectwalker': ['objectwalker/', 'objectwalker/filters/', 'objectwalker/utils/', 'objectwalker/tests/']},
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
