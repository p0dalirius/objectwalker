#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : core.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023
import sys

import objectwalker
from .filters.EmptyFilter import EmptyFilter


class ObjectWalker(object):
    """
    Documentation for class ObjectWalker
    """

    def __init__(self, filters_accept=[], filters_reject=[], filters_skip_exploration=[], matchmode_accept="any", matchmode_reject="any", matchmode_skip_exploration="any", callback=None, verbose=False, no_colors=False):
        """

        :param filters_accept:
        :param filters_reject:
        :param filters_skip_exploration:
        :param matchmode_accept:
        :param matchmode_reject:
        :param matchmode_skip_exploration:
        :param callback:
        :param verbose:
        :param no_colors:
        """
        super(ObjectWalker, self).__init__()
        self.verbose = verbose
        self.no_colors = no_colors

        # Matchmode
        self.filter_matchmode_accept = any
        self.set_filter_matchmode_accept(matchmode_accept)
        self.filter_matchmode_reject = any
        self.set_filter_matchmode_reject(matchmode_reject)
        self.filter_matchmode_skip_exploration = any
        self.set_filter_matchmode_skip_exploration(matchmode_skip_exploration)

        # Filters
        self.filters_accept = filters_accept
        self.filters_reject = filters_reject
        self.filters_skip_exploration = filters_skip_exploration
        if len(self.filters_accept) == 0 and len(self.filters_reject) == 0:
            self.filters_accept = [EmptyFilter()]

        # Known objects
        self.knownids = []
        # First ignore internal modules
        __to_ignore = [
            objectwalker,
            objectwalker.core,
            objectwalker.filters,
            objectwalker.filters.by_object,
            objectwalker.filters.by_object.name,
            objectwalker.filters.by_object.name.FilterObjectNameContains,
            objectwalker.filters.by_object.name.FilterObjectNameEndsWith,
            objectwalker.filters.by_object.name.FilterObjectNameEquals,
            objectwalker.filters.by_object.name.FilterObjectNameIsPythonBuiltin,
            objectwalker.filters.by_object.name.FilterObjectNameStartsWith,
            objectwalker.filters.by_object.value,
            objectwalker.filters.by_object.value.FilterObjectValueContains,
            objectwalker.filters.by_object.value.FilterObjectValueEndsWith,
            objectwalker.filters.by_object.value.FilterObjectValueEquals,
            objectwalker.filters.by_object.value.FilterObjectValueStartsWith,
            objectwalker.filters.by_path,
            objectwalker.filters.by_path.FilterPathContains,
            objectwalker.filters.by_path.FilterPathEndsWith,
            objectwalker.filters.by_path.FilterPathStartsWith,
            objectwalker.filters.by_type,
            objectwalker.filters.by_type.FilterTypeIsBuiltinFunctionOrMethod,
            objectwalker.filters.by_type.FilterTypeIsMethodWrapper,
            objectwalker.filters.by_type.FilterTypeIsModule,
            objectwalker.filters.EmptyFilter,
            objectwalker.__main__,
            objectwalker.utils,
            objectwalker.utils.RegExMatcher,
            objectwalker.utils.Reporter
        ]
        __to_ignore += filters_accept
        __to_ignore += filters_reject
        __to_ignore += filters_skip_exploration
        __to_ignore += [self]

        # Add imported objectwalker modules from sys.modules
        for modulename, module in sys.modules.items():
            if modulename == "objectwalker" or modulename.startswith("objectwalker."):
                print("Adding ", modulename)
                __to_ignore.append(id(module))

        for e in __to_ignore:
            self.knownids.append(id(e))

        print(self.knownids)

        # Callbacks
        for f in self.filters_reject:
            f.set_callback(None)
        for f in self.filters_skip_exploration:
            f.set_callback(None)
        if callback is not None:
            self.set_callback(callback)

    def walk(self, obj, path=[], depth=0, maxdepth=3, verbose=False, method="breadth"):
        """

        :param obj:
        :param path:
        :param depth:
        :param maxdepth:
        :param verbose:
        :param method:
        :return:
        """
        if "breadth" in method.strip().lower():
            return self.walk_breadth_first(obj, path=path, depth=depth, maxdepth=maxdepth, verbose=verbose)
        if "depth" in method.strip().lower():
            return self.walk_depth_first(obj, path=path, depth=depth, maxdepth=maxdepth, verbose=verbose)
        else:
            print("[!] Unknown method.")
            return None

    def find_in_threads(self, maxdepth=3, verbose=False, skip_threads_name=["MainThread"], method="breadth"):
        """

        :param maxdepth:
        :param verbose:
        :param skip_threads_name:
        :param method:
        :return:
        """
        import threading
        results = []
        for thread_id, thread in threading._active.items():
            if threading._active[thread_id]._name not in skip_threads_name:
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
        """

        :param obj:
        :param found:
        :param path:
        :param depth:
        :param maxdepth:
        :param verbose:
        :return:
        """
        if depth == 0 and len(path) == 0:
            path = ["obj"]

        if depth < maxdepth:
            # Prepare objects for exploration
            objtree = self.__prepare_objtree(obj)

            # Exploring objects
            for subkey, subobj in objtree.items():
                if type(subobj) in [bool]:
                    continue
                try:
                    if int(id(subobj)) not in self.knownids:
                        # Format the subkey
                        path_to_obj = path[:]
                        # Object is a dict
                        if type(obj) == dict:
                            if type(subkey) == int:
                                path_to_obj[-1] += '[%d]' % subkey
                            elif type(subkey) == str:
                                path_to_obj[-1] += '["%s"]' % subkey
                            else:
                                path_to_obj[-1] += '["%s"]' % str(subkey)
                        # Object is a list
                        elif type(obj) == list:
                            path_to_obj.append("[%d]" % subkey)
                        # All other types
                        else:
                            path_to_obj.append(subkey)

                        # Save the found path if it matches filters (accept, and not reject)
                        if not self.filter_matchmode_accept([f.check(subobj, path_to_obj) for f in self.filters_accept]):
                            if self.filter_matchmode_reject([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                                found.append(path_to_obj)
                        else:
                            # Save id of explored object
                            if int(id(subobj)) not in self.knownids:
                                self.knownids.append(int(id(subobj)))

                        # Explore further if filters allow it
                        if not self.filter_matchmode_skip_exploration([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
                            found = self.walk_depth_first(obj=subobj, found=found, path=path_to_obj, depth=(depth+1), maxdepth=maxdepth, verbose=verbose)

                except AttributeError as e:
                    pass

        return found

    def walk_breadth_first(self, obj, found=[], path=[], depth=0, maxdepth=3, verbose=False):
        """

        :param obj:
        :param found:
        :param path:
        :param depth:
        :param maxdepth:
        :param verbose:
        :return:
        """
        to_explore = []

        if depth == 0 and len(path) == 0:
            path = ["obj"]

        if depth < maxdepth:
            # Prepare objects for exploration
            objtree = self.__prepare_objtree(obj)

            # Exploring objects
            for subkey, subobj in objtree.items():
                if type(subobj) in [bool]:
                    continue
                try:
                    if int(id(subobj)) not in self.knownids:
                        # Format the subkey
                        path_to_obj = path[:]
                        # Object is a dict
                        if type(obj) == dict:
                            if type(subkey) == int:
                                path_to_obj[-1] += '[%d]' % subkey
                            elif type(subkey) == str:
                                path_to_obj[-1] += '["%s"]' % subkey
                            else:
                                path_to_obj[-1] += '["%s"]' % str(subkey)
                        # Object is a list
                        elif type(obj) == list:
                            path_to_obj.append("[%d]" % subkey)
                        # All other types
                        else:
                            path_to_obj.append(subkey)

                        # Save the found path if it matches filters (accept, and not reject)
                        if not self.filter_matchmode_accept([f.check(subobj, path_to_obj) for f in self.filters_accept]):
                            if self.filter_matchmode_reject([f.check(subobj, path_to_obj) for f in self.filters_reject]):
                                found.append(path_to_obj)
                        else:
                            # Save id of explored object
                            if int(id(subobj)) not in self.knownids:
                                self.knownids.append(int(id(subobj)))

                        # Explore further if filters allow it
                        if not self.filter_matchmode_skip_exploration([f.check(subobj, path_to_obj) for f in self.filters_skip_exploration]):
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

    def __prepare_objtree(self, obj):
        """

        :param obj: object
        :return: objtree: dict
        """
        objtree = {}
        if type(obj) == dict:
            objtree = obj
        elif type(obj) in [list, tuple]:
            objtree = {
                index: obj[index]
                for index in range(len(obj))
            }
        else:
            objtree = {}
            for _property in sorted(dir(obj)):
                try:
                    objtree[_property] = eval("obj.%s" % _property, {"obj": obj})
                except (Exception) as e:
                    continue
        return objtree
    
    def get_verbose(self):
        """

        :return:
        """
        return self.verbose
    
    def set_verbose(self, value):
        """

        :param value:
        :return:
        """
        self.verbose = value

    def get_callback(self):
        """

        :return:
        """
        return self.callback
    
    def set_callback(self, fcallback):
        """

        :param fcallback:
        :return:
        """
        self.callback = fcallback
        for f in self.filters_accept:
            f.set_callback(fcallback)


    def get_filter_matchmode_accept(self):
        """

        :return:
        """
        return self.filter_matchmode_accept

    def set_filter_matchmode_accept(self, matchmode):
        """

        :param matchmode:
        :return:
        """
        if matchmode == "any":
            self.filter_matchmode_accept = any
        elif matchmode == "all":
            self.filter_matchmode_accept = all
        else:
            self.filter_matchmode_accept = any

    def get_filter_matchmode_reject(self):
        """

        :return:
        """
        return self.filter_matchmode_reject

    def set_filter_matchmode_reject(self, matchmode):
        """

        :param matchmode:
        :return:
        """
        if matchmode == "any":
            self.filter_matchmode_reject = any
        elif matchmode == "all":
            self.filter_matchmode_reject = all
        else:
            self.filter_matchmode_reject = any

    def get_filter_matchmode_skip_exploration(self):
        """

        :return:
        """
        return self.filter_matchmode_skip_exploration

    def set_filter_matchmode_skip_exploration(self, matchmode):
        """

        :param matchmode:
        :return:
        """
        if matchmode == "any":
            self.filter_matchmode_skip_exploration = any
        elif matchmode == "all":
            self.filter_matchmode_skip_exploration = all
        else:
            self.filter_matchmode_skip_exploration = any

    def set_no_print(self):
        """

        :param value:
        :return:
        """
        for f in self.filters_accept:
            f.set_callback(None)
        for f in self.filters_reject:
            f.set_callback(None)
        for f in self.filters_skip_exploration:
            f.set_callback(None)
