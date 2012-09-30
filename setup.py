#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pycurl2
~~~~~~~

PycURL2 is a revised version of PycURL, that not maintained more than 3 years (from 7.19.0 (Sep 9 2008)).

`PycURL`_ is a Python interface to `libcurl`_.
`PycURL`_ can be used to fetch objects identified by a URL
from a Python program, similar to the `urllib`_ Python module.
`PycURL`_ is mature, very fast, and supports a lot of features.


:copyright: (c) 2001-2008 by Kjetil Jacobsen <kjetilja at gmail.com>
:copyright: (c) 2001-2008 by Markus F.X.J. Oberhumer <markus at oberhumer.com>
:copyright: (c) 2012 by Alexandr Lispython <alex at obout.ru, alex at dzone.me>
:license: LGPL/MIT, see COPIYNG and COPYING2 for more details.

.. _PycURL: http://pycurl.sourceforge.net/
.. _libcurl: http://curl.haxx.se/libcurl/
.. _urllib: http://docs.python.org/library/urllib.html
"""

import os
import sys

try:
    from setuptools import setup
    from setuptools import Extension
    from setuptools import Command
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    from distutils.cmd import Command


# Import setup help functions
from src import get_version
from setup_helpers import extension_params, ParamsPrinter

# Setup constants
PACKAGE = "pycurl2"
extensions = []


# Make C extension than we can import as PACKAGE name
# that can imported with pycurl2 name
pycurl2_ext = Extension(
    name=PACKAGE,
    sources=[
        os.path.join("src", "pycurl.c"),
    ],
    **extension_params
)

extensions.append(pycurl2_ext)

# Added test requirement
tests_require = [
    'nose',
    'unittest2',
    'simplejson']

try:
    readme_content = open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "README.rst")).read()
except Exception, e:
    sys.stderr.write(e)
    readme_content = __doc__


setup_args = dict(
    name=PACKAGE,
    version=get_version(),
    url='http://pycurl2.github.com',
    license='LGPL/MIT',
    description='PycURL2 - cURL library module for python',
    author='Alexandr Lispython (2012), Kjetil Jacobsen (2001 - 2008), Markus F.X.J. Oberhumer (2001 - 2008)',
    author_email='alex@obout.ru [kjetilja at gmail.com, markus at oberhumer.com]',
    maintainer='Alexandr Lispython (2012), Kjetil Jacobsen (2001 - 2008), Markus F.X.J. Oberhumer (2001 - 2008)',
    maintainer_email='alex@obout.ru [kjetilja at gmail.com, markus at oberhumer.com]',
    long_description=readme_content,
    zip_safe=False,
    ext_modules=extensions,
    tests_require=tests_require,
    package_data={'': ['COPYING', 'COPYING2', 'INSTALL']},
    ## download_url="http://cloud.github.com/downloads/Lispython/pycurl/pycurl2-%s.tar.gz' % get_version()",
    platforms=['Linux', 'Mac', 'Windows'],
    keywords=['curl','pycurl', 'http library'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'],
    test_suite='tests.suite',
    include_package_data=True,
    cmdclass={'params': ParamsPrinter})


if __name__ == '__main__':
    apply(setup, (), setup_args)
