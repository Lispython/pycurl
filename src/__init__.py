#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PycURL2
~~~~~~~

Python binging to c libcurl library.

:copyright: (c) 2012 by Alexandr Lispython (alex@obout.ru, alex@dzone.me).
:license: LGPL/MIT, see COPYING2 and COPYING for more details.
"""

__version__ = '7.20.0.a1'
__build__ = 0x072000
__license__ = 'LGPL/MIT'

def get_version():
    return __version__

version_tuple = tuple(map(str, __version__.split('.')))

__all__ = ('get_verion', '__version__',
           '__build__', '__license__', 'version_tuple')
