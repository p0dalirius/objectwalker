#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterObjNameEq.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter


class FilterObjNameEq(EmptyFilter):
    """
    Documentation for class FilterObjNameEq
    """
    values = []
    no_colors = False

    def __init__(self, values, no_colors=False):
        super(EmptyFilter, self).__init__()
        self.__filter_name = __name__.split('.')[-1]
        self.no_colors = no_colors
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value == element:
                    matches_filter = True
                    self.print_result(obj, path_to_obj)
                    return matches_filter
        return matches_filter
