#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : __main__.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import argparse
import objectwalker

VERSION = "1.1"


def parseArgs():
    print("objectwalker v%s - by @podalirius_\n" % VERSION)

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='Verbose mode. (default: False)')
    parser.add_argument("-d", "--max-depth", default=5, type=int, help="Maximum recursion depth to explore in objects.")

    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("-m", "--module", default=None, type=str, help="Python module to explore")

    return parser.parse_args()


def main():
    options = parseArgs()

    print("[>] Starting to explore ...")
    module = __import__(options.module)
    ow = objectwalker.core.ObjectWalker(filters=[FilterObjIsBuiltinFunctionOrMethod()], verbose=False)
    ow.walk(module, path=[options.module])
    print("[>] all done!")


if __name__ == '__main__':
    main()