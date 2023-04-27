#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : core.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

from .filters.EmptyFilter import EmptyFilter


class ObjectWalker(object):
    """
    Documentation for class ObjectWalker
    """

    def __init__(self, filters_accept=[], filters_reject=[], callback=None, verbose=False, no_colors=False):
        super(ObjectWalker, self).__init__()
        self.verbose = verbose
        self.no_colors = no_colors

        # Filters
        self.filters_accept = filters_accept
        self.filters_reject = filters_reject
        if len(self.filters_accept) == 0 and len(self.filters_reject) == 0:
            self.filters_accept = [EmptyFilter()]
        self.knownids = [id(self)] + [id(f) for f in filters_accept] + [id(f) for f in filters_reject]

        # Callback
        if callback is not None:
            self.set_callback(callback)

    def walk(self, obj, path=[], depth=0, maxdepth=3, verbose=False, method="breadth"):
        if "breadth" in method.strip().lower():
            return self.walk_breadth_first(obj, path=path, depth=depth, maxdepth=maxdepth, verbose=verbose)
        if "depth" in method.strip().lower():
            return self.walk_depth_first(obj, path=path, depth=depth, maxdepth=maxdepth, verbose=verbose)
        else:
            print("[!] Unknown method.")
            return None

    def walk_depth_first(self, obj, found=[], path=[], depth=0, maxdepth=3, verbose=False):
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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path[:]
                        if type(subkey) == int:
                            path_to_obj[-1] += '[%d]' % subkey
                        elif type(subkey) == str:
                            path_to_obj[-1] += '["%s"]' % subkey
                        else:
                            path_to_obj[-1] += '["%s"]' % subkey

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk_depth_first(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path[:]
                        path_to_obj[-1] += "[%d]" % index

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk_depth_first(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path + [subkey]

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            found = self.walk_depth_first(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                    except AttributeError as e:
                        pass
        return found

    def walk_breadth_first(self, obj, found=[], path=[], depth=0, maxdepth=3, verbose=False):
        to_explore = []
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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path[:]
                        if type(subkey) == int:
                            path_to_obj[-1] += '[%d]' % subkey
                        elif type(subkey) == str:
                            path_to_obj[-1] += '["%s"]' % subkey
                        else:
                            path_to_obj[-1] += '["%s"]' % subkey

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            to_explore.append((subobj, path_to_obj, depth))

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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path[:]
                        path_to_obj[-1] += "[%d]" % index

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            to_explore.append((subobj, path_to_obj, depth))

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
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        path_to_obj = path + [subkey]

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)

                        # Explore further
                        if id(subobj) not in self.knownids:
                            self.knownids.append(id(subobj))
                            to_explore.append((subobj, path_to_obj, depth))

                    except AttributeError as e:
                        pass

        if depth == 0:
            # Explore one more in depth, but only in top level function
            while len([e for e in to_explore if e[2] <= maxdepth]) != 0:
                next_to_explore = []
                for _subobj, _path_to_obj, _depth in to_explore:
                    next_to_explore += self.walk_breadth_first(
                        obj=_subobj,
                        found=found,
                        path=_path_to_obj,
                        depth=(_depth + 1),
                        maxdepth=maxdepth,
                        verbose=verbose
                    )
                to_explore = next_to_explore[:]
        return to_explore
    
    
    def get_verbose(self):
        return self.verbose
    
    def set_verbose(self, value):
        self.verbose = value

    def get_callback(self):
        return self.callback
    
    def set_callback(self, fcallback):
        self.callback = fcallback
        for f in self.filters_accept:
            f.set_callback(fcallback)
        for f in self.filters_reject:
            f.set_callback(None)
    