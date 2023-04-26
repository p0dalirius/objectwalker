#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : filter_object.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

class FilterObjNameEq(object):
    """
    Documentation for class FilterObjNameEq
    """
    values = []
    def __init__(self, values):
        super(FilterObjNameEq, self).__init__()
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value == element:
                    matches_filter = True
                    return matches_filter
        return matches_filter


class FilterObjNameContains(object):
    """
    Documentation for class FilterObjNameContains
    """
    values = []
    def __init__(self, values):
        super(FilterObjNameContains, self).__init__()
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value in element:
                    matches_filter = True
                    return matches_filter
        return matches_filter
