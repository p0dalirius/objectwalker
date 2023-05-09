#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : ssti_jinja2.py
# Author             : Podalirius (@podalirius_)
# Date created       : 9 May 2023

import jinja2
import objectwalker
from objectwalker.filters import *

# Same idea that I did in 2021, but better!
# https://podalirius.net/en/publications/grehack-2021-optimizing-ssti-payloads-for-jinja2/

if __name__ == '__main__':
    ow = objectwalker.core.ObjectWalker(filters_accept=[EmptyFilter()], verbose=False)

    template_str = 'Hello {{ow.walk(self,path=["self"],maxdepth=5)}}'
    template = jinja2.Template(template_str)
    output = template.render(ow=ow)
    print(output)


