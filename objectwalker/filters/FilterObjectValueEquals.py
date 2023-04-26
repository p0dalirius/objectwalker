#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterObjectValueEquals.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter


class FilterObjectValueEquals(EmptyFilter):
    """
    Documentation for class FilterObjectValueEquals
    """
    values = []
    no_colors = False

    filter_name = "FilterObjectValueEquals"

    def __init__(self, values, no_colors=False):
        super(FilterObjectValueEquals, self).__init__()
        self.no_colors = no_colors
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False

        if any([(str(obj) == value) for value in self.values]):
            matches_filter = True

        if matches_filter:
            self.print_result(obj, path_to_obj)
        return matches_filter

    def __repr__(self):
        return "<%s values=%s>" % (self.filter_name, self.values)