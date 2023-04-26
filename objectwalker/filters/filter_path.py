#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : filter_path.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

class FilterPathContains(object):
    """
    Documentation for class FilterPathContains
    """
    values = []
    def __init__(self, values):
        super(FilterPathContains, self).__init__()
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value in element:
                    matches_filter = True
                    return matches_filter
        return matches_filter


class FilterPathStartsWith(object):
    """
    Documentation for class FilterPathStartsWith
    """
    values = []
    def __init__(self, values):
        super(FilterPathStartsWith, self).__init__()
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value in element:
                    matches_filter = True
                    return matches_filter
        return matches_filter


class FilterPathEndsWith(object):
    """
    Documentation for class FilterPathEndsWith
    """
    values = []
    def __init__(self, values):
        super(FilterPathEndsWith, self).__init__()
        self.values = values

    def check(self, obj, path_to_obj):
        matches_filter = False
        for element in path_to_obj:
            for value in self.values:
                if value in element:
                    matches_filter = True
                    return matches_filter
        return matches_filter