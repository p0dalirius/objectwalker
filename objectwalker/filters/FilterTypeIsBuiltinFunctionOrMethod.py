#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterTypeIsBuiltinFunctionOrMethod.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter


class FilterTypeIsBuiltinFunctionOrMethod(EmptyFilter):
    """
    Documentation for class FilterTypeIsBuiltinFunctionOrMethod
    """

    filter_name = "FilterTypeIsBuiltinFunctionOrMethod"

    def check(self, obj, path_to_obj):
        matches_filter = False
        if str(type(obj)) == "<class 'builtin_function_or_method'>":
            matches_filter = True

        return matches_filter

    def __repr__(self):
        return "<%s>" % self.filter_name