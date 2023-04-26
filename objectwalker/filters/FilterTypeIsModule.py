#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterTypeIsModule.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import re
from .EmptyFilter import EmptyFilter


class FilterTypeIsModule(EmptyFilter):
    """
    Documentation for class FilterTypeIsModule
    """

    modules = []
    no_colors = False

    def __init__(self, modules=[], no_colors=False):
        super(FilterTypeIsModule, self).__init__()
        self.__filter_name = __name__.split('.')[-1]
        self.no_colors = no_colors
        self.modules = modules

    def check(self, obj, path_to_obj):
        matches_filter = False
        if str(type(obj)) == "<class 'module'>":
            if len(self.modules) == 0:
                matches_filter = True
            else:
                module_name, module_type, module_source_file = self.parse_module_name(str(obj))
                if module_name in self.modules:
                    matches_filter = True

        if matches_filter:
            self.print_result(obj, path_to_obj)
        return matches_filter

    def print_result(self, obj, path_to_obj):
        # Print the found path
        module_name, module_type, module_source_file = self.parse_module_name(str(obj))

        if self.no_colors:
            print("[%s] [module=%s] [module_type=%s] | %s" % (
                    self.__filter_name,
                    module_name,
                    module_type,
                    '.'.join(path_to_obj)
                )
            )
        else:
            print("[\x1b[95m%s\x1b[0m] [module=\x1b[1;91m%s\x1b[0m] [module_type=\x1b[94m%s\x1b[0m] | \x1b[1;92m%s\x1b[0m"  % (
                    self.__filter_name,
                    module_name,
                    module_type,
                    '.'.join(path_to_obj)
                )
            )

    def parse_module_name(self, module_str):
        module_name, module_type, module_source_file = None, None, None
        matched = re.search("(<module '([^']+)' (\(built-in\)|\(frozen\)|from '([^']+)')>)", module_str)
        if matched is not None:
            _, module_name, module_type, module_source_file = matched.groups()
            if module_type.startswith("from"):
                module_type = "package"
            else:
                module_type = module_type.strip("()")
        return module_name, module_type, module_source_file
