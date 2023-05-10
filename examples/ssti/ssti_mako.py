#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : ssti_jinja2.py
# Author             : Podalirius (@podalirius_)
# Date created       : 9 May 2023

from mako.template import Template
import objectwalker
from objectwalker.filters import *

# Same idea that I did in 2021, but better!
# https://podalirius.net/en/articles/python-context-free-payloads-in-mako-templates/

def explore_hook(obj):
    ow.walk(obj, path=["self"], maxdepth=10)
    return None

if __name__ == '__main__':
    ow = objectwalker.core.ObjectWalker(
        filters_accept=[FilterTypeIsModule(modules=["os"])],
        filters_reject=[FilterObjectNameIsPythonBuiltin(keep_gadgets=True)],
        filters_skip_exploration=[FilterObjectNameIsPythonBuiltin(keep_gadgets=True)],
        verbose=False
    )

    template_str = 'Hello ${explore_hook(self)}'
    template = Template(template_str)
    output = template.render(explore_hook=explore_hook)
    print(output)


