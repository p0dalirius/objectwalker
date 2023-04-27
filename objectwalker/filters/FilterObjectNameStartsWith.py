#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterObjectNameStartsWith.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter


class FilterObjectNameStartsWith(EmptyFilter):
    """
    Documentation for class FilterObjectNameStartsWith
    """
    values = []
    no_colors = False

    filter_name = "FilterObjectNameStartsWith"

    def __init__(self, values, no_colors=False):
        super(FilterObjectNameStartsWith, self).__init__()
        self.callback = self.print_result
        self.no_colors = no_colors
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False

        if any([(str(path_to_obj[-1]).startswith(value)) for value in self.values]):
            matches_filter = True

        if matches_filter:
            if self.callback is not None:
                self.callback(obj, path_to_obj)

        return matches_filter

    def __repr__(self):
        return "<%s values=%s>" % (self.filter_name, self.values)