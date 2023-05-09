#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : class_heritance.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import objectwalker
from objectwalker.filters import *

base = [0, 1, 2, 32, 4, 84, {"SECRET": "UEHPAcW3TSaZAl6rVW32wwRTgl9lsVF"}, "ee", [0, {"SECRET": "UEHPAcW3TSaZAl6rVW32wwRTgl9lsVF"}]]

class A(object):
    def __init__(self):
        super(A, self).__init__()

A_obj = A()

print("[>] Starting to explore ...")

ow = objectwalker.core.ObjectWalker(filters_accept=[FilterObjectNameContains(values=["SECRET"])], verbose=False)
ow.walk(base, path=["base"], maxdepth=5)

print("[>] All done!")