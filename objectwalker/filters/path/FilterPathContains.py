#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterPathContains.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from objectwalker.filters.EmptyFilter import EmptyFilter


class FilterPathContains(EmptyFilter):
    """
    Documentation for class FilterPathContains
    """
    values = []
    regular_expressions = []
    no_colors = False

    filter_name = "FilterPathContains"

    def __init__(self, values=[], regular_expressions=[], no_colors=False):
        super(EmptyFilter, self).__init__()
        self.callback = self.print_result
        self.no_colors = no_colors
        self.values = values
        self.regular_expressions = regular_expressions

    def check(self, obj, path_to_obj):
        matches_filter = False

        regexmatcher = RegExMatcher(regular_expressions=self.regular_expressions)
        regexmatcher.set_all_regex_to_contains()

        if any([value in '.'.join(path_to_obj) for value in self.values]) or (regexmatcher.match(path_to_obj[-1])):
            matches_filter = True

        if matches_filter:
            if self.callback is not None:
                self.callback(obj, path_to_obj)

        return matches_filter

    def __repr__(self):
        return "<%s values=%s regular_expressions=%s>" % (self.filter_name, self.values, self.regular_expressions)