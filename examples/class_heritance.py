#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : class_heritance.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import objectwalker
from objectwalker.filters import *

SECRET = "UEHPAcW3TSaZAl6rVW32wwRTgl9lsVF"

class A(object):
    def __init__(self):
        super(A, self).__init__()

class B(A):
    def __init__(self):
        super(B, self).__init__()


B_obj = B()

print("[>] Starting to explore ...")
ow = objectwalker.core.ObjectWalker(filters=[FilterTypeIsBuiltinFunctionOrMethod()], verbose=False)
ow.walk(B_obj, path=["B_obj"])
print("[>] all done!")