#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : find_in_a_thread.py
# Author             : Podalirius (@podalirius_)
# Date created       : 28 Apr 2023


import threading
import time
import objectwalker
from objectwalker.filters import *


class Server(object):
    """
    Documentation for class Server
    """

    SECRET = "UEHPAcW3TSaZAl6rVW32wwRTgl9lsVF"

    def __init__(self):
        super(Server, self).__init__()

    def worker(self):
        time.sleep(600)


if __name__ == '__main__':
    s = Server()
    t = threading.Thread(target=s.worker)
    t.start()

    print("[>] Starting to explore ...")
    ow = objectwalker.core.ObjectWalker(
        filters_accept=[FilterObjectNameContains(values=["SECRET"])],
        filters_reject=[FilterObjectNameIsPythonBuiltin(keep_gadgets=True)],
        filters_skip_exploration=[FilterObjectNameIsPythonBuiltin(keep_gadgets=True)],
        verbose=False
    )
    ow.find_in_threads(maxdepth=10)
    print("[>] All done!")

    t.join()