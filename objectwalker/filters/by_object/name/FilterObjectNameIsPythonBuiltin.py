#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterObjectNameIsPythonBuiltin.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from objectwalker.filters.EmptyFilter import EmptyFilter


class DummyEmptyClass(object):
    pass

def DummyEmptyFunction():
    pass

class FilterObjectNameIsPythonBuiltin(EmptyFilter):
    """
    Documentation for class FilterObjectNameIsPythonBuiltin
    """
    values = []

    no_colors = False

    filter_name = "FilterObjectNameIsPythonBuiltin"

    def __init__(self, keep_gadgets=True, no_colors=False):
        super(FilterObjectNameIsPythonBuiltin, self).__init__()
        self.callback = self.print_result
        self.no_colors = no_colors

        # Load builtin python functions
        self.values = []
        for obj in [0, "str", [1, 2, 3], (1, 2, 3), True, None, DummyEmptyClass(), DummyEmptyFunction]:
            self.values += [e for e in dir(obj) if e.startswith('__') and e.endswith('__')]
        self.values = list(sorted(set(self.values)))

        if keep_gadgets:
            gadgets = ["__call__", "__class__", "_init__", "__init_subclass__", "__subclasshook__", "__weakref__", "__self__", "__object__"]
            for g in gadgets:
                while g in self.values:
                    self.values.remove(g)

    def check(self, obj, path_to_obj):
        """

        :param obj:
        :param path_to_obj:
        :return:
        """
        matches_filter = False

        if any([(str(path_to_obj[-1]) == value) for value in self.values]):
            matches_filter = True

        if matches_filter:
            if self.callback is not None:
                self.callback(obj, path_to_obj)

        return matches_filter

    def __repr__(self):
        """

        :return:
        """
        return "<%s values=%s>" % (self.filter_name, self.values)