#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : class_heritance.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import objectwalker
from objectwalker.filters import *

import sys

print("[>] Starting to explore ...")

ow = objectwalker.core.ObjectWalker(verbose=False)
ow.walk(sys, path=["sys"], maxdepth=5)

print("[>] All done!")