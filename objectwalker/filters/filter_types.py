#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : filter_types.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

class FilterObjIsModule(object):
    """
    Documentation for class FilterObjIsModule
    """

    def __init__(self):
        super(FilterObjIsModule, self).__init__()

    def check(self, obj, path_to_obj):
        matches_filter = False
        str_obj = str(obj)
        print(str(type(obj)))
        if str(type(obj)) == "<class 'module'>":
            matches_filter = True
            return matches_filter
        return matches_filter


class FilterObjIsMethodWrapper(object):
    """
    Documentation for class FilterObjIsMethodWrapper
    """

    def __init__(self):
        super(FilterObjIsMethodWrapper, self).__init__()

    def check(self, obj, path_to_obj):
        matches_filter = False
        str_obj = str(obj)
        print(str(type(obj)))
        if str(type(obj)) == "<class 'method-wrapper'>":
            matches_filter = True
            return matches_filter
        return matches_filter


class FilterObjIsBuiltinFunctionOrMethod(object):
    """
    Documentation for class FilterObjIsBuiltinFunctionOrMethod
    """

    def __init__(self):
        super(FilterObjIsBuiltinFunctionOrMethod, self).__init__()

    def check(self, obj, path_to_obj):
        matches_filter = False
        str_obj = str(obj)
        print(str(type(obj)))
        if str(type(obj)) == "<class 'builtin_function_or_method'>":
            matches_filter = True
            return matches_filter
        return matches_filter