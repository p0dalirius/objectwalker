#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : class_heritance.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Apr 2023

import threading
import time
import pdb
import objectwalker
from objectwalker.filters import *
import sys

knid = []

def callback(obj, path):
    global knid
    if id(obj) not in knid:
        knid.append(id(obj))
        print("[ids=%03d] \x1b[92m%s : %s\x1b[0m" % (len(knid), '.'.join(path), id(obj)))
    else:
        print("[ids=%03d] \x1b[91m%s : %s\x1b[0m" % (len(knid), '.'.join(path), id(obj)))
        breakpoint()

class Server(object):
    """
    Documentation for class Server
    """

    SECRET = "UEHPAcW3TSaZAl6rVW32wwRTgl9lsVF"

    def __init__(self):
        super(Server, self).__init__()

    def worker(self):

        time.sleep(60)


if __name__ == '__main__':
    s = Server()
    t = threading.Thread(target=s.worker)
    t.start()

    print("[>] Starting to explore ...")
    ow = objectwalker.core.ObjectWalker(
        filters_accept=[
            FilterObjectNameContains(values=["SECRET"]),
            EmptyFilter()
        ],
        filters_reject=[
            FilterObjectNameIsPythonBuiltin(keep_gadgets=True)
        ],
        filters_skip_exploration=[
            FilterObjectNameIsPythonBuiltin(keep_gadgets=True)
        ],
        callback=callback,
        verbose=False
    )
    ow.find_in_threads(maxdepth=10, method="breadth")
    print("[>] All done!")

    t.join()