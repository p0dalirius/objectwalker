#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : Test_Search.py
# Author             : Podalirius (@podalirius_)
# Date created       : 10 May 2023


import objectwalker
from objectwalker.filters import *
import unittest


base = {
    "a": {
        "aa": {
            "aaa": {
                "aaaa": 17,
                "aaab": 17
            },
            "aab": {
                "aaba": 17,
                "aabb": 17
            },
            "aac": {
                "aaca": 17,
                "aacb": 17
            }
        },
        "ab": {
            "aba": {
                "abaa": 17,
                "abab": 17
            },
            "abb": {
                "abba": 17,
                "abbb": 17
            },
            "abc": {
                "abca": 17,
                "abcb": 17
            }
        },
        "ac": {
            "aca": {
                "acaa": 17,
                "acab": 17
            },
            "acb": {
                "acba": 17,
                "acbb": 17
            },
            "acc": {
                "acca": 17,
                "accb": {
                    "accba": 17
                }
            }
        }
    },
    "b": {
        "ba": {
            "baa": {
                "baaa": 17,
                "baab": 17
            },
            "bab": {
                "baba": 17,
                "babb": 17
            },
            "bac": {
                "baca": 17,
                "bacb": 17
            }
        },
        "bb": {
            "bba": {
                "bbaa": 17,
                "bbab": 17
            },
            "bbb": {
                "bbba": 17,
                "bbbb": 17
            },
            "bbc": {
                "bbca": 17,
                "bbcb": 17
            }
        },
        "bc": {
            "bca": {
                "bcaa": 17,
                "bcab": 17
            },
            "bcb": {
                "bcba": 17,
                "bcbb": 17
            },
            "bcc": {
                "bcca": 17,
                "bccb": 17
            }
        }
    },
    "c": {
        "ca": {
            "caa": {
                "caaa": 17,
                "caab": 17
            },
            "cab": {
                "caba": 17,
                "cabb": 17
            },
            "cac": {
                "caca": 17,
                "cacb": 17
            }
        },
        "cb": {
            "cba": {
                "cbaa": 17,
                "cbab": 17
            },
            "cbb": {
                "cbba": 17,
                "cbbb": 17
            },
            "cbc": {
                "cbca": 17,
                "cbcb": 17
            }
        },
        "cc": {
            "cca": {
                "ccaa": 17,
                "ccab": 17
            },
            "ccb": {
                "ccba": 17,
                "ccbb": 17
            },
            "ccc": {
                "ccca": 17,
                "cccb": 17
            }
        }
    }
}

class Test_Search(unittest.TestCase):

    def test_dfs(self):
        expected = []
        ow = objectwalker.core.ObjectWalker(
            filters_accept=[FilterPathEndsWith(values=["\"]"])],
            verbose=False
        )
        ow.set_no_print()
        found = ow.walk(base, path=["base"], maxdepth=5, method="depth")
        self.assertEqual(expected, found)

    def test_bfs(self):
        expected = []
        ow = objectwalker.core.ObjectWalker(
            filters_accept=[FilterPathEndsWith(values=["\"]"])],
            verbose=False
        )
        ow.set_no_print()
        found = ow.walk(base, path=["base"], maxdepth=5, method="breadth")
        self.assertEqual(expected, found)
