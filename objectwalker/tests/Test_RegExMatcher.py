#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : test_RegExMatcher.py
# Author             : Podalirius (@podalirius_)
# Date created       : 29 Apr 2023


import unittest
from objectwalker.utils import RegExMatcher

class Test_RegExMatcher(unittest.TestCase):

    def test_set_all_regex_to_startswith(self):
        regexes = [
            "^podalirius$",
            "^podalirius",
            "podalirius$",
            "podalirius"
        ]

        expected = [
            "^podalirius",
            "^podalirius",
            "^podalirius",
            "^podalirius"
        ]

        r = RegExMatcher(regular_expressions=regexes)
        r.set_all_regex_to_startswith()

        self.assertEqual(expected, r.regular_expressions)

    def test_set_all_regex_to_endswith(self):
        regexes = [
            "^podalirius$",
            "^podalirius",
            "podalirius$",
            "podalirius"
        ]

        expected = [
            "podalirius$",
            "podalirius$",
            "podalirius$",
            "podalirius$"
        ]

        r = RegExMatcher(regular_expressions=regexes)
        r.set_all_regex_to_endswith()

        self.assertEqual(expected, r.regular_expressions)

    def test_set_all_regex_to_contains(self):
        regexes = [
            "^podalirius$",
            "^podalirius",
            "podalirius$",
            "podalirius"
        ]

        expected = [
            "podalirius",
            "podalirius",
            "podalirius",
            "podalirius"
        ]

        r = RegExMatcher(regular_expressions=regexes)
        r.set_all_regex_to_contains()

        self.assertEqual(expected, r.regular_expressions)

    def test_set_all_regex_to_exactmatch(self):
        regexes = [
            "^podalirius$",
            "^podalirius",
            "podalirius$",
            "podalirius"
        ]

        expected = [
            "^podalirius$",
            "^podalirius$",
            "^podalirius$",
            "^podalirius$"
        ]

        r = RegExMatcher(regular_expressions=regexes)
        r.set_all_regex_to_exactmatch()

        self.assertEqual(expected, r.regular_expressions)
