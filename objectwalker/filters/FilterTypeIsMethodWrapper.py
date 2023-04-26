#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterTypeIsMethodWrapper.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .EmptyFilter import EmptyFilter

class FilterTypeIsMethodWrapper(EmptyFilter):
    """
    Documentation for class FilterTypeIsMethodWrapper
    """

    filter_name = "FilterTypeIsMethodWrapper"

    def check(self, obj, path_to_obj):
        matches_filter = False
        if str(type(obj)) == "<class 'method-wrapper'>":
            matches_filter = True

        return matches_filter

    def __repr__(self):
        return "<%s>" % self.filter_name