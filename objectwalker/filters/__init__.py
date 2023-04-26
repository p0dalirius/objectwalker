#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __init__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

# Generic base filter
from .EmptyFilter import EmptyFilter

# Filters on object names
from .FilterObjectNameEquals import FilterObjectNameEquals
from .FilterObjectNameContains import FilterObjectNameContains
from .FilterObjectNameStartsWith import FilterObjectNameStartsWith
from .FilterObjectNameEndsWith import FilterObjectNameEndsWith

# Filters on object values
from .FilterObjectValueEquals import FilterObjectValueEquals
from .FilterObjectValueContains import FilterObjectValueContains
from .FilterObjectValueStartsWith import FilterObjectValueStartsWith
from .FilterObjectValueEndsWith import FilterObjectValueEndsWith

# Filters on path
from .FilterPathContains import FilterPathContains
from .FilterPathStartsWith import FilterPathStartsWith
from .FilterPathEndsWith import FilterPathEndsWith

# Filters on type
from .FilterTypeIsModule import FilterTypeIsModule
from .FilterTypeIsMethodWrapper import FilterTypeIsMethodWrapper
from .FilterTypeIsBuiltinFunctionOrMethod import FilterTypeIsBuiltinFunctionOrMethod

