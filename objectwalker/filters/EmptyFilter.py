#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : EmptyFilter.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

class EmptyFilter(object):
    """
    class EmptyFilter

    Default filter, matches every path without constraints
    """

    no_colors = False
    filter_name = "EmptyFilter"
    callback = None

    def __init__(self, no_colors=False):
        super(EmptyFilter, self).__init__()
        self.callback = self.print_result
        self.no_colors = no_colors

    def check(self, obj, path_to_obj):
        if self.callback is not None:
            self.callback(obj, path_to_obj)
        return True

    def print_result(self, obj, path_to_obj):
        # Print the found path
        obj_value = str(obj)[:50]
        obj_value = str(bytes(obj_value, 'utf-8'))[2:-1]

        if self.no_colors:
            print("[%s] [type=%s] [value=%s] | %s" % (
                    self.filter_name,
                    str(type(obj)),
                    obj_value,
                    '.'.join(path_to_obj)
                )
            )
        else:
            print("[\x1b[95m%s\x1b[0m] [type=\x1b[1;91m%s\x1b[0m] [value=\x1b[94m%s\x1b[0m] | \x1b[1;92m%s\x1b[0m"  % (
                    self.filter_name,
                    str(type(obj)),
                    obj_value,
                    '.'.join(path_to_obj)
                )
            )

    def __repr__(self):
        return "<%s>" % self.filter_name

    def get_callback(self):
        return self.callback

    def set_callback(self, value):
        self.callback = value
