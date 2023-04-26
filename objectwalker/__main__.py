#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __main__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import argparse
import sys
import objectwalker
from objectwalker.filters import *


VERSION = "1.8"


banner = r"""
       ____  __      _           __ _       __      ____            
      / __ \/ /_    (_)__  _____/ /| |     / /___ _/ / /_____  _____
     / / / / __ \  / / _ \/ ___/ __/ | /| / / __ `/ / //_/ _ \/ ___/
    / /_/ / /_/ / / /  __/ /__/ /_ | |/ |/ / /_/ / / ,< /  __/ /      v%s 
    \____/_.___/_/ /\___/\___/\__/ |__/|__/\__,_/_/_/|_|\___/_/       by @podalirius_
              /___/                                                 
""" % VERSION


def parseArgs():
    print(banner)

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='Verbose mode. (default: False)')
    parser.add_argument("-d", "--max-depth", default=5, type=int, help="Maximum recursion depth to explore in objects.")
    parser.add_argument("--no-colors", dest="no_colors", action="store_true", default=False, help="No colors mode.")

    group_source = parser.add_mutually_exclusive_group(required=True)
    group_source.add_argument("-m", "--module", default=None, type=str, help="Python module to explore.")

    # Objects
    group_filters_objects = parser.add_argument_group("Filters on objects")
    group_filters_objects.add_argument("--filter-object-name-equals", default=[], type=str, action="append", help="Show paths from the base object leading to an object name equals to <string>.")
    group_filters_objects.add_argument("--filter-object-name-contains", default=[], type=str, action="append", help="Show paths from the base object leading to an object name containing <string>.")
    group_filters_objects.add_argument("--filter-object-name-startswith", default=[], type=str, action="append", help="Show paths from the base object leading to an object name starting with <string>.")
    group_filters_objects.add_argument("--filter-object-name-endswith", default=[], type=str, action="append", help="Show paths from the base object leading to an object name ending with <string>.")
    group_filters_objects.add_argument("--filter-object-is-module", default=[], type=str, action="append", help="Show paths from the base object leading to a specific module.")

    # Paths
    group_filters_paths = parser.add_argument_group("Filters on paths")
    group_filters_paths.add_argument("--filter-path-contains", default=[], type=str, action="append", help="Show paths from the base object containing <string>.")
    group_filters_paths.add_argument("--filter-path-startswith", default=[], type=str, action="append", help="Show paths from the base object starting with <string>.")
    group_filters_paths.add_argument("--filter-path-endswith", default=[], type=str, action="append", help="Show paths from the base object ending with <string>.")

    # Types
    group_filters_types = parser.add_argument_group("Filters on types")
    group_filters_types.add_argument("--filter-type-module", default=False, action="store_true", help="Show paths from the base object leading to modules.")
    group_filters_types.add_argument("--filter-type-builtin-function-or-method", default=False, action="store_true", help="Show paths from the base object leading to builtin-function-or-method.")
    group_filters_types.add_argument("--filter-type-method-wrapper", default=False, action="store_true", help="Show paths from the base object leading to method-wrapper.")

    return parser.parse_args()


def main():
    options = parseArgs()

    # Disable colored output if stdout is not a TTY
    if not sys.stdout.isatty():
        options.no_colors = True

    filters = []

    # Filters on types
    if len(options.filter_object_is_module) != 0:
        filters.append(FilterTypeIsModule(modules=options.filter_object_is_module, no_colors=options.no_colors))
    if options.filter_type_module:
        filters.append(FilterTypeIsModule(no_colors=options.no_colors))
    if options.filter_type_method_wrapper:
        filters.append(FilterTypeIsMethodWrapper(no_colors=options.no_colors))
    if options.filter_type_builtin_function_or_method:
        filters.append(FilterTypeIsBuiltinFunctionOrMethod(no_colors=options.no_colors))

    # Filters on objects
    if len(options.filter_object_name_equals) != 0:
        filters.append(FilterObjectNameEquals(values=options.filter_object_name_equals, no_colors=options.no_colors))
    if len(options.filter_object_name_contains) != 0:
        filters.append(FilterObjectNameContains(values=options.filter_object_name_contains, no_colors=options.no_colors))
    if len(options.filter_object_name_startswith) != 0:
        filters.append(FilterObjectNameStartsWith(values=options.filter_object_name_startswith, no_colors=options.no_colors))
    if len(options.filter_object_name_endswith) != 0:
        filters.append(FilterObjectNameEndsWith(values=options.filter_object_name_endswith, no_colors=options.no_colors))

    # Filters on paths
    if len(options.filter_path_contains) != 0:
        filters.append(FilterPathContains(values=options.filter_path_contains, no_colors=options.no_colors))
    if len(options.filter_path_startswith) != 0:
        filters.append(FilterPathStartsWith(values=options.filter_path_startswith, no_colors=options.no_colors))
    if len(options.filter_path_endswith) != 0:
        filters.append(FilterPathEndsWith(values=options.filter_path_endswith, no_colors=options.no_colors))

    # No filters yet
    if len(filters) == 0:
        filters = [EmptyFilter(no_colors=options.no_colors)]

    if options.verbose:
        print("[>] Loaded %d filters." % len(filters))
        for filter in filters:
            print("  ├──> %s" % filter.__repr__())

    print("[>] Exploring object tree of module '%s' up to depth %d ..." % (options.module, options.max_depth))
    module = __import__(options.module)
    print("[+] Using %s" % str(module))
    ow = objectwalker.ObjectWalker(filters=filters, verbose=options.verbose, no_colors=options.no_colors)
    ow.walk(module, path=[options.module])
    print("[>] All done!")


if __name__ == '__main__':
    main()