#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __init__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

# Generic base filter
from .EmptyFilter import EmptyFilter

# Filters on object
from .FilterObjNameEq import FilterObjNameEq
from .FilterObjNameContains import FilterObjNameContains

# Filters on path
from .FilterPathContains import FilterPathContains
from .FilterPathStartsWith import FilterPathStartsWith
from .FilterPathEndsWith import FilterPathEndsWith

# Filters on type
from .FilterTypeIsModule import FilterTypeIsModule
from .FilterTypeIsMethodWrapper import FilterTypeIsMethodWrapper
from .FilterTypeIsBuiltinFunctionOrMethod import FilterTypeIsBuiltinFunctionOrMethod

