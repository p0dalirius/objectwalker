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

    def __init__(self, filters_accept=[], filters_reject=[], filters_skip_exploration=[], callback=None, verbose=False, no_colors=False):
        super(ObjectWalker, self).__init__()
        self.verbose = verbose
        self.no_colors = no_colors

        # Filters
        self.filters_accept = filters_accept
        self.filters_reject = filters_reject
        self.filters_skip_exploration = filters_skip_exploration
        if len(self.filters_accept) == 0 and len(self.filters_reject) == 0:
            self.filters_accept = [EmptyFilter()]

        # Known objects
        self.knownids = []
        self.knownids.append(id(self))
        for f in filters_accept:
            self.knownids.append(id(f))
        for f in filters_reject:
            self.knownids.append(id(f))
        for f in filters_skip_exploration:
            self.knownids.append(id(f))

        # Callbacks
        for f in self.filters_reject:
            f.set_callback(None)
        for f in self.filters_skip_exploration:
            f.set_callback(None)
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

    def find_in_threads(self, maxdepth=3, verbose=False, method="breadth"):
        import threading
        results = []
        for thread_id, thread in threading._active.items():
            path = ["threading._active[%d]._target" % thread_id]
            print("[>] Exploring Thread %s" % thread)
            if "breadth" in method.strip().lower():
                results += self.walk_breadth_first(thread._target, path=path, depth=0, maxdepth=maxdepth, verbose=verbose)
            elif "depth" in method.strip().lower():
                results += self.walk_depth_first(thread._target, path=path, depth=0, maxdepth=maxdepth, verbose=verbose)
            else:
                print("[!] Unknown method.")
        return results

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
                            path_to_obj = path[:]
                            if type(subkey) == int:
                                path_to_obj[-1] += '[%d]' % subkey
                                subobj = eval('obj[%d]' % subkey, {"obj": obj})
                            elif type(subkey) == str:
                                path_to_obj[-1] += '["%s"]' % subkey
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                            else:
                                path_to_obj[-1] += '["%s"]' % subkey
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)
                            input()

                        # Explore further
                        if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                            if int(id(subobj)) not in self.knownids and False:
                                self.knownids.append(int(id(subobj)))
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
                            path_to_obj = path[:]
                            path_to_obj[-1] += "[%d]" % index
                            subobj = eval("obj[%d]" % index, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)
                            input()

                        # Explore further
                        if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                            if int(id(subobj)) not in self.knownids and False:
                                self.knownids.append(int(id(subobj)))
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
                            path_to_obj = path + [subkey]
                            subobj = eval("obj.%s" % subkey, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if any([f.check(subobj, path_to_obj) for f in self.filters_accept]) and not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                            # Save the found path
                            found.append(path_to_obj)
                            input()

                        # Explore further
                        if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                            if int(id(subobj)) not in self.knownids and False:
                                self.knownids.append(int(id(subobj)))
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
                            path_to_obj = path[:]
                            if type(subkey) == int:
                                path_to_obj[-1] += '[%d]' % subkey
                                subobj = eval('obj[%d]' % subkey, {"obj": obj})
                            elif type(subkey) == str:
                                path_to_obj[-1] += '["%s"]' % subkey
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                            else:
                                path_to_obj[-1] += '["%s"]' % subkey
                                subobj = eval('obj["%s"]' % subkey, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if int(id(subobj)) not in self.knownids:
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                                if any([f.check(subobj, path_to_obj) for f in self.filters_accept]):
                                    # Save the found path
                                    found.append(path_to_obj)

                            # Explore further if filters allow it
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                                to_explore.append((subobj, path_to_obj, depth))

                            # Save id of explored object
                            if int(id(subobj)) not in self.knownids:
                                self.knownids.append(int(id(subobj)))

                    except AttributeError as e:
                        pass

            # Exploring list objects
            elif type(obj) == list:
                for index in range(len(obj)):
                    if type(obj[index]) in [bool]:
                        continue
                    try:
                        try:
                            path_to_obj = path[:]
                            path_to_obj[-1] += "[%d]" % index
                            subobj = eval("obj[%d]" % index, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if int(id(subobj)) not in self.knownids:
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                                if any([f.check(subobj, path_to_obj) for f in self.filters_accept]):
                                    # Save the found path
                                    found.append(path_to_obj)

                            # Explore further if filters allow it
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                                to_explore.append((subobj, path_to_obj, depth))

                            # Save id of explored object
                            if int(id(subobj)) not in self.knownids:
                                self.knownids.append(int(id(subobj)))

                    except AttributeError as e:
                        pass

            # Other objects
            else:
                for subkey in dir(obj):
                    if type(subkey) in [bool]:
                        continue
                    try:
                        try:
                            path_to_obj = path + [subkey]
                            subobj = eval("obj.%s" % subkey, {"obj": obj})
                        except (SyntaxError, ValueError, KeyError, TypeError) as e:
                            continue

                        if int(id(subobj)) not in self.knownids:
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                                if any([f.check(subobj, path_to_obj) for f in self.filters_accept]):
                                    # Save the found path
                                    found.append(path_to_obj)

                            # Explore further if filters allow it
                            if not any([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                                to_explore.append((subobj, path_to_obj, depth))

                            # Save id of explored object
                            if int(id(subobj)) not in self.knownids:
                                self.knownids.append(int(id(subobj)))

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
