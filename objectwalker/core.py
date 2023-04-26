#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : core.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

class ObjectWalker(object):
    """
    Documentation for class ObjectWalker
    """

    def __init__(self, filters=[], verbose=False, no_colors=False):
        super(ObjectWalker, self).__init__()
        self.verbose = verbose
        self.no_colors = no_colors
        self.filters = filters
        self.knownids = [id(self)] + [id(f) for f in filters]

    def walk(self, obj, found=[], path=[], depth=0, maxdepth=3, verbose=False):
        if depth == 0 and len(path) == 0:
            path = ["obj"]
        if depth < maxdepth:
            for subkey in dir(obj):
                if type(subkey) in [bool]:
                    continue
                try:
                    try:
                        subobj = eval("obj.%s" % subkey, {'obj': obj})
                    except SyntaxError as e:
                        continue

                    path_to_obj = path+[subkey]

                    if any([f.check(subobj, path_to_obj) for f in self.filters]):
                        # Print the found path
                        if self.no_colors:
                            print("[%-50s] [type=%s] | %s" % (str(subobj)[:50], str(type(subobj)), '.'.join(path_to_obj)))
                        else:
                            print("[\x1b[94m%-50s\x1b[0m] [\x1b[95mtype=%s\x1b[0m] | \x1b[93m%s\x1b[0m" % (str(subobj)[:50], str(type(subobj)), '.'.join(path_to_obj)))
                        # Save the found path
                        found.append(path_to_obj)
                    elif self.verbose:
                        print("[SKIPPED] %s" % ('.'.join(path_to_obj)))

                    # Explore further
                    if id(subobj) not in self.knownids:
                        self.knownids.append(id(subobj))
                        found = self.walk(obj=subobj, found=found, path=path+[subkey], depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                except AttributeError as e:
                    pass

        return found
