#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __main__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import argparse
import sys
import objectwalker
from objectwalker.filters import *


VERSION = "1.2"


def parseArgs():
    print("objectwalker v%s - by @podalirius_\n" % VERSION)

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='Verbose mode. (default: False)')
    parser.add_argument("-d", "--max-depth", default=5, type=int, help="Maximum recursion depth to explore in objects.")
    parser.add_argument("--no-colors", dest="no_colors", action="store_true", default=False, help="No colors mode.")

    group_source = parser.add_mutually_exclusive_group(required=True)
    group_source.add_argument("-m", "--module", default=None, type=str, help="Python module to explore.")

    group_filters = parser.add_argument_group("Filters")
    group_filters.add_argument("--filter-object-name", default=None, type=str, help="Show paths from the base object leading object named <name>.")
    group_filters.add_argument("--filter-object-is-module", default=[], type=str, action='append', help="Show paths from the base object leading to a specific module.")
    group_filters.add_argument("--filter-object-is-type-module", default=False, action="store_true", help="Show paths from the base object leading to modules.")
    group_filters.add_argument("--filter-object-is-type-builtin-function-or-method", default=False, action="store_true", help="Show paths from the base object leading to builtin-function-or-method.")
    group_filters.add_argument("--filter-object-is-type-method-wrapper", default=False, action="store_true", help="Show paths from the base object leading to method-wrapper.")

    return parser.parse_args()


def main():
    options = parseArgs()

    # Disable colored output if stdout is not a TTY
    if not sys.stdout.isatty():
        options.no_colors = True

    filters = []

    if len(options.filter_object_is_module) != 0:
        filters.append(FilterTypeIsModule(modules=options.filter_object_is_module, no_colors=options.no_colors))
    if options.filter_object_is_type_module:
        filters.append(FilterTypeIsModule(no_colors=options.no_colors))
    if options.filter_object_is_type_method_wrapper:
        filters.append(FilterTypeIsMethodWrapper(no_colors=options.no_colors))
    if options.filter_object_is_type_builtin_function_or_method:
        filters.append(FilterTypeIsBuiltinFunctionOrMethod(no_colors=options.no_colors))
    if len(filters) == 0:
        filters = [EmptyFilter(no_colors=options.no_colors)]

    print("[>] Exploring object tree of module '%s' up to depth %d ..." % (options.module, options.max_depth))
    module = __import__(options.module)
    print("[+] Using %s" % str(module))
    ow = objectwalker.core.ObjectWalker(filters=filters, verbose=options.verbose, no_colors=options.no_colors)
    ow.walk(module, path=[options.module])
    print("[>] All done!")


if __name__ == '__main__':
    main()