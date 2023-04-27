#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterObjectNameIsPythonBuiltin.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter


class FilterObjectNameIsPythonBuiltin(EmptyFilter):
    """
    Documentation for class FilterObjectNameIsPythonBuiltin
    """
    values = []

    no_colors = False

    filter_name = "FilterObjectNameIsPythonBuiltin"

    def __init__(self, no_colors=False):
        super(FilterObjectNameIsPythonBuiltin, self).__init__()
        self.no_colors = no_colors

        # Load builtin python functions
        self.values = []
        for obj in [0, "str", [1, 2, 3], (1, 2, 3), True, None]:
            self.values += [e for e in dir(obj) if e.startswith('__') and e.endswith('__')]
        self.values = list(sorted(set(self.values)))

    def check(self, obj, path_to_obj):
        matches_filter = False

        if any([(str(path_to_obj[-1]) == value) for value in self.values]):
            matches_filter = True

        if matches_filter:
            self.print_result(obj, path_to_obj)
        return matches_filter

    def __repr__(self):
        return "<%s values=%s>" % (self.filter_name, self.values)