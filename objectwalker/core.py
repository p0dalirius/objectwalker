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

            # Exploring dict objects
            if type(obj) == dict:
                for subkey in obj.keys():
                    if type(obj[subkey]) in [bool]:
                        continue
                    try:
                        try:
                            if type(subkey) == int:
                                subobj = eval('obj[%d]' % subkey, {"obj": obj})
                            elif type(subkey) == str:
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                            else:
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                        except SyntaxError as e:
                            continue

                        path_to_obj = path[:]
                        if type(subkey) == int:
                            path_to_obj[-1] += '[%d]' % subkey
                        elif type(subkey) == str:
                            path_to_obj[-1] += '["%s"]' % subkey
                        else:
                            path_to_obj[-1] += '["%s"]' % subkey

                        if any([f.check(subobj, path_to_obj) for f in self.filters]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                    except AttributeError as e:
                        pass

            # Exploring list objects
            elif type(obj) == list:
                for index in range(len(obj)):
                    if type(obj[index]) in [bool]:
                        continue
                    try:
                        try:
                            subobj = eval("obj[%d]" % index, {"obj": obj})
                        except SyntaxError as e:
                            continue

                        path_to_obj = path[:]
                        path_to_obj[-1] += "[%d]" % index

                        if any([f.check(subobj, path_to_obj) for f in self.filters]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                    except AttributeError as e:
                        pass

            # Other objects
            else:
                for subkey in dir(obj):
                    if type(subkey) in [bool]:
                        continue
                    try:
                        try:
                            subobj = eval("obj.%s" % subkey, {"obj": obj})
                        except SyntaxError as e:
                            continue

                        path_to_obj = path + [subkey]

                        if any([f.check(subobj, path_to_obj) for f in self.filters]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                    except AttributeError as e:
                        pass
        return found
