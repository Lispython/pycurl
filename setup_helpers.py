#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pycurl2.setup_helpers
~~~~~~~~~~~~~~~~~~~~~

Module that store utilites that help create setup

:copyright: (c) 2001-2008 by Kjetil Jacobsen <kjetilja at gmail.com>
:copyright: (c) 2001-2008 by Markus F.X.J. Oberhumer <markus at oberhumer.com>
:copyright: (c) 2012 by Alexandr Lispython <alex at obout.ru, alex at dzone.me>
:license: LGPL/MIT, see COPYING and COPYING2 for more details.
"""

import os
import re
import sys
from subprocess import Popen, PIPE
try:
    from setuptools import Command
except ImportError:
    from distutils.cmd import Command

from distutils.util import split_quoted


__all__ = 'extension_params', 'ParamsPrinter'


# Use optparse to parse options
def parse_args():
    options = {"curl_config": "curl-config",
               "curl_dir": None,
               "openssl_dir": None}

    for option in options:
        for arg in sys.argv[1:]:
            if arg.startswith('--%s' % option.replace("_", "-")):
                try:
                    options[option] = arg.split("=")[1]
                except IndexError:
                    continue

    return options['curl_dir'], options['curl_config'], options['openssl_dir']


curl_dir, curl_config, openssl_dir = parse_args()

def write_and_exit(lines):
    """Write error to stderr and exit

    :param lines: list of strings to print
    """
    for line in lines:
        sys.stderr.write(line)
        sys.stderr.write("\n")
    sys.exit(1)


def get_curl_config_param(flag, curl_config=curl_config):
    """Get curl config compiling parameters

    :param flag: param name
    """
    res = os.popen("'%s' --%s" % (curl_config, flag)).read()
    if res:
        return res.strip()
    return res


def get_extension_params():
    """Processed script arguments and return parameters lists
    :return: dict if parameters
    """
    params = dict(
        include_dirs=[],
        define_macros=[],
        library_dirs=[],
        libraries=[],
        runtime_library_dirs=[],
        extra_objects=[],
        extra_compile_args=[],
        extra_link_args=[])

    if sys.platform == 'win32':
        return make_windows_params(params)
    return make_posix_params(params)

def make_posix_params(params):
    """Make params for POSIX systems

    :param params_dict: parameters dictionary
    :return: updated params_dict
    """
    # Find out the rest the hard way
    if openssl_dir:
        params['include_dirs'].append(os.path.join(openssl_dir, "include"))

    libcurl_version = get_curl_config_param('version')

    if not libcurl_version:
        write_and_exit(["libcurl '%s' not found -- please install the libcurl development files" % curl_config])

    sys.stdout.write("Using %s (%s)\n\n" % (curl_config, libcurl_version))
    sys.stdout.write("Using curl directory: %s\n" % curl_dir)

    for flag in split_quoted(get_curl_config_param('cflags')):
        if flag[:2] == "-I":
            # do not add /usr/include
            if not re.search(r"^\/+usr\/+include\/*$", flag[2:]):
                params['include_dirs'].append(flag[2:])
        else:
            params['extra_compile_args'].append(flag)

    # Run curl-config --libs and --static-libs.  Some platforms may not
    # support one or the other of these curl-config options, so gracefully
    # tolerate failure of either, but not both.
    optbuf = ""
    for option in ["--libs", "--static-libs"]:
        p = Popen("'%s' %s" % (curl_config, option), shell=True,
            stdout=PIPE)
        (stdout, stderr) = p.communicate()
        if p.wait() == 0:
            optbuf += stdout
    if not optbuf:
        write_and_exit(['Neither of curl-config --libs or --static-libs produced output'])

    for flag in split_quoted(optbuf):
        if flag[:2] == "-l":
            params['libraries'].append(flag[2:])
            if flag[2:] == 'ssl':
                params['define_macros'].append(('HAVE_CURL_OPENSSL', 1))
            if flag[2:] == 'gnutls':
                params['define_macros'].append(('HAVE_CURL_GNUTLS', 1))
        elif flag[:2] == "-L":
            params['library_dirs'].append(flag[2:])
        else:
            params['extra_link_args'].append(flag)

    # Check libcurl features
    # curl-config --features
    for feature in split_quoted(get_curl_config_param("features")):
        if feature == 'SSL':
            params['define_macros'].append(('HAVE_CURL_SSL', 1))

    if not params['libraries']:
        params['libraries'].append("curl")

    # Add extra compile flag for MacOS X
    if sys.platform[:-1] == "darwin":
        params['extra_link_args'].append("-flat_namespace")
    return params


def make_windows_params(params):
    """Make params for WINDOWS systems

    Windows users have to configure the --curl-dir path parameter to match
    their cURL source installation.

    :return: updated params_dict
    """

    if not options.curl_dir:
        write_and_exit(['You need specify --curl-dir argument'])

    sys.stdout.write("Using curl directory: %s" % curl_dir)

    if not os.path.isdir(curl_dir):
        write_and_exit(["Please check that %s in setup.py" % curl_dir])


    params['inculde_dirs'].append(os.path.join(curl_dir, "include"))
    params['extra_objects'].append(os.path.join(curl_dir, "lib", "libcurl.lib"))
    params['extra_link_args'].extend(["gdi32.lib", "wldap32.lib", "winmm.lib", "ws2_32.lib"])

    # Add libdirs from env
    add_libdirs(envvar="LIB", sep=";", library_dirs=params['library_dirs'])

    if sys.version.find("MSC") >= 0:
        params['extra_compile_args'].append("-O2")
        params['extra_compile_args'].append("-GF")        # enable read-only string pooling
        params['extra_compile_args'].append("-WX")        # treat warnings as errors
        params['extra_link_args'].append("/opt:nowin98")  # use small section alignment

    return params

def add_libdirs(envvar, sep, library_dirs, fatal=0):
    """Add library dirs from environment

    :param envvar: environment variable
    :param sep: paths separator
    :param library_dirs: point to the list that store library dirs
    :param fatal:
    """
    v = os.environ.get(envvar)
    if not v:
        return
    for directory in v.split(sep):
        directory = directory.strip()
        if not directory:
            continue
        directory = os.path.normpath(directory)
        if os.path.isdir(directory):
            if not directory in library_dirs:
                library_dirs.append(directory)
        elif fatal:
            write_and_exit(["FATAL: bad directory %s in environment variable %s\n" % (directory, envvar)])



# Process only at once
extension_params = get_extension_params()

class ParamsPrinter(Command):
    """Get custom params and print it into stdout
    """
    description = __doc__
    user_options = [('curl-config', None, "Curl config"),
                    ('curl-dir', None, "Curl directory"),
                    ('openssl-dir', None, "Curl openssl directory")]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self, *args, **kwargs):
        sys.stdout.write("Compiling on %s\n" % sys.platform)
        params = extension_params

        for name, value in params.iteritems():
            sys.stdout.write("%s: %s\n" % (name, value))
        sys.stdout.write("-" * 10)
        sys.stdout.write("\n")
        sys.exit(0)
