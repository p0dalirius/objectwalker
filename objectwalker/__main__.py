#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __main__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import argparse
import objectwalker
from objectwalker.filters import *

VERSION = "1.1"


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
    group_filters.add_argument("--filter-object-is-module", default=False, action="store_true", help="Show paths from the base object leading to modules.")
    group_filters.add_argument("--filter-object-is-builtin-function-or-method", default=False, action="store_true", help="Show paths from the base object leading to builtin-function-or-method.")
    group_filters.add_argument("--filter-object-is-method-wrapper", default=False, action="store_true", help="Show paths from the base object leading to method-wrapper.")

    return parser.parse_args()


def main():
    options = parseArgs()

    filters = []
    if options.filter_object_is_module:
        filters.append(FilterObjIsModule())
    if options.filter_object_is_module:
        filters.append(FilterObjIsModule())
    if options.filter_object_is_module:
        filters.append(FilterObjIsModule())

    print("[>] Exploring object tree of module '%s' up to depth %d ..." % (options.module, options.max_depth))
    module = __import__(options.module)
    ow = objectwalker.core.ObjectWalker(filters=filters, verbose=options.verbose, no_colors=options.no_colors)
    ow.walk(module, path=[options.module])
    print("[>] All done!")


if __name__ == '__main__':
    main()