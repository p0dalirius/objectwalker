#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : RegExMatcher.py
# Author             : Podalirius (@podalirius_)
# Date created       : 29 Apr 2023

import re


class RegExMatcher(object):
    """
    Documentation for class RegExMatcher
    """

    def __init__(self, regular_expressions=[]):
        super(RegExMatcher, self).__init__()
        self.regular_expressions = regular_expressions

    def match(self, data):
        is_matching = False

        for regex in self.regular_expressions:
            # Prepare regex to match type
            if type(data) == bytes and type(regex) == str:
                regex = bytes(regex, "utf-8")
            elif type(data) == str and type(regex) == bytes:
                regex = regex.decode("utf-8")

            if type(data) == type(regex):
                if re.match(pattern=regex, string=data):
                    is_matching = True
                    # For optimization, break at first match to avoid testing
                    # every other regular expression after one did match
                    break

        return is_matching

    def set_all_regex_to_startswith(self):
        new_list_of_regexes = []
        for regex in self.regular_expressions:
            if type(regex) == bytes:
                # Add match for start of string
                if not regex.startswith(b'^'):
                    regex = b'^' + regex
                # Remove match for end of string
                if regex.endswith(b'$') and not regex.endswith(b'\\$'):
                    regex = regex[:-1]
            elif type(regex) == str:
                # Add match for start of string
                if not regex.startswith('^'):
                    regex = '^' + regex
                # Remove match for end of string
                if regex.endswith('$') and not regex.endswith('\\$'):
                    regex = regex[:-1]
            new_list_of_regexes.append(regex)
        self.regular_expressions = new_list_of_regexes[:]

    def set_all_regex_to_endswith(self):
        new_list_of_regexes = []
        for regex in self.regular_expressions:
            if type(regex) == bytes:
                # Remove match for start of string
                if regex.startswith(b'^'):
                    regex = regex[1:]
                # Add match for end of string
                if not regex.endswith(b'$') or regex.endswith(b'\\$'):
                    regex = regex + b'$'
            elif type(regex) == str:
                # Remove match for start of string
                if regex.startswith('^'):
                    regex = regex[1:]
                # Add match for end of string
                if not regex.endswith('$') or regex.endswith('\\$'):
                    regex = regex + '$'
            new_list_of_regexes.append(regex)
        self.regular_expressions = new_list_of_regexes[:]

    def set_all_regex_to_contains(self):
        new_list_of_regexes = []
        for regex in self.regular_expressions:
            if type(regex) == bytes:
                # Remove match for start of string
                if regex.startswith(b'^'):
                    regex = regex[1:]
                # Remove match for end of string
                if regex.endswith(b'$') and not regex.endswith(b'\\$'):
                    regex = regex[:-1]
            elif type(regex) == str:
                # Remove match for start of string
                if regex.startswith('^'):
                    regex = regex[1:]
                # Remove match for end of string
                if regex.endswith('$') and not regex.endswith('\\$'):
                    regex = regex[:-1]
            new_list_of_regexes.append(regex)
        self.regular_expressions = new_list_of_regexes[:]

    def set_all_regex_to_exactmatch(self):
        new_list_of_regexes = []
        for regex in self.regular_expressions:
            if type(regex) == bytes:
                # Add match for start of string
                if not regex.startswith(b'^'):
                    regex = b'^' + regex
                # Add match for end of string
                if not regex.endswith(b'$') or regex.endswith(b'\\$'):
                    regex = regex + b'$'
            elif type(regex) == str:
                # Add match for start of string
                if not regex.startswith('^'):
                    regex = '^' + regex
                # Add match for end of string
                if not regex.endswith('$') or regex.endswith('\\$'):
                    regex = regex + '$'
            new_list_of_regexes.append(regex)
        self.regular_expressions = new_list_of_regexes[:]
