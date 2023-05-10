#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : class_heritance.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import objectwalker
from objectwalker.filters import *

base = {
    "a": 17,
    "b": 17,
    "c": "aaaa",
    "d": 17,
    "e": 17,
    "f": {
        "zep": "eeee",
        "d": {
            "SECRET": "GyMgL3AfRGvaZwkQDgX+63zUDGaoEoq7S1rdd0"
        }
    }
}

print("[>] Starting to explore ...")

ow = objectwalker.core.ObjectWalker(filters_accept=[FilterObjectNameContains(values=["SECRET"])], verbose=False)
ow.walk(base, path=["base"], maxdepth=5)

print("[>] All done!")