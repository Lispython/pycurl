#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
pycurl2.tests
~~~~~~~~~~~~~

Unittests for pycurl

:copyright: (c) 2012 by Alexandr Lispython (alex@obout.ru, alex@dzone.me).
:license: LGPL/MIT, see LICENSING for more details.
"""
from __future__ import with_statement

import os
import urllib
import pycurl2 as pycurl
from random import choice
from string import ascii_letters, digits
import logging
from urlparse import urljoin
import unittest
from StringIO import StringIO

try:
    import simplejson as json
except ImportError:
    import json


logger = logging.getLogger("pycurl2.tests")

# Use https://github.com/Lispython/httphq
if 'HTTP_TEST_URL' not in os.environ:
    os.environ['HTTP_TEST_URL'] = 'http://h.wrttn.me'

if 'HTTPS_TEST_URL' not in os.environ:
    os.environ['HTTPS_TEST_URL'] = 'https://h.wrttn.me'

HTTP_TEST_URL = os.environ.get('HTTP_TEST_URL')
HTTPS_TEST_URL = os.environ.get('HTTPS_TEST_URL')

def build_url(*parts):
    return urljoin(HTTP_TEST_URL, "/".join(parts))

def build_url_secure(*parts):
    return urljoin(HTTPS_TEST_URL, "/".join(parts))

TEST_SERVERS = (build_url, build_url_secure)

def random_string(num=10):
    return ''.join([choice(ascii_letters + digits) for x in xrange(num)])

def stdout_debug(debug_type, debug_msg):
    """Print messages
    """
    debug_types = ('I', '<', '>', '<', '>')
    if debug_type == 0:
        print('%s' % debug_msg.strip())
    elif debug_type in (1, 2):
        for line in debug_msg.splitlines():
            print('%s %s' % (debug_types[debug_type], line))
    elif debug_type == 4:
        print('%s %r' % (debug_types[debug_type], debug_msg))



class BaseTestCase(unittest.TestCase):

    def test_build_url(self):
        self.assertEquals(build_url("get"), HTTP_TEST_URL + "/" + "get")
        self.assertEquals(build_url("post"), HTTP_TEST_URL + "/" + "post")
        self.assertEquals(build_url("redirect", "3"), HTTP_TEST_URL + "/" + "redirect" + "/" + "3")

    @staticmethod
    def random_string(num=10):
        return random_string(10)

    def random_dict(self, num=10):
        return dict([(self.random_string(10), self.random_string(10))for x in xrange(10)])

    def request_params(self):
        data = self.random_dict(10)
        data['url'] = build_url("get")
        data['method'] = 'get'
        return data

class CurlTestCase(BaseTestCase):

    def test_get(self):
        c =  pycurl.Curl()
        body_output = StringIO()
        headers_output = StringIO()
        url = build_url('get')
        c.setopt(pycurl.URL, build_url('get'))
        c.setopt(pycurl.WRITEFUNCTION, body_output.write)
        c.setopt(pycurl.HEADERFUNCTION, headers_output.write)

        c.perform()
        self.assertEquals(200, c.getinfo(pycurl.RESPONSE_CODE))

        c.close()
        json_body = json.loads(body_output.getvalue())
        self.assertEquals(json_body['url'], url)
        self.assertEquals(json_body['headers']['User-Agent'], "PycURL/%s" % pycurl.version_info()[1])

    def test_head(self):
        c =  pycurl.Curl()
        body_output = StringIO()
        headers_output = StringIO()
        url = build_url('head')
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.NOBODY, True)
        c.setopt(pycurl.WRITEFUNCTION, body_output.write)
        c.setopt(pycurl.HEADERFUNCTION, headers_output.write)

        c.perform()

        self.assertEquals(200, c.getinfo(pycurl.RESPONSE_CODE))
        self.assertEquals(url, c.getinfo(pycurl.EFFECTIVE_URL))
        c.close()
        self.assertEquals(len(body_output.getvalue()), 0)
        headers_list = headers_output.getvalue().split("\r\n")
        self.assertEquals(headers_list[0], "HTTP/1.1 200 OK")


class MultiCurlTestCase(BaseTestCase):
    pass

class CurlSharetTestCase(BaseTestCase):
    pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BaseTestCase))
    suite.addTest(unittest.makeSuite(CurlTestCase))
    suite.addTest(unittest.makeSuite(MultiCurlTestCase))
    suite.addTest(unittest.makeSuite(CurlSharetTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
