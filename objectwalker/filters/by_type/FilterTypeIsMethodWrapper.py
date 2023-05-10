#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterTypeIsMethodWrapper.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from objectwalker.filters.EmptyFilter import EmptyFilter


class FilterTypeIsMethodWrapper(EmptyFilter):
    """
    Documentation for class FilterTypeIsMethodWrapper
    """

    filter_name = "FilterTypeIsMethodWrapper"

    def check(self, obj, path_to_obj):
        """

        :param obj:
        :param path_to_obj:
        :return:
        """
        matches_filter = False

        if str(type(obj)) == "<class 'method-wrapper'>":
            matches_filter = True

        if matches_filter:
            if self.callback is not None:
                self.callback(obj, path_to_obj)

        return matches_filter

    def __repr__(self):
        """

        :return:
        """
        return "<%s>" % self.filter_name