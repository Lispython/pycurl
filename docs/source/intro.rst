.. module:: PycURL2

Module Functionality
====================

.. function:: pycurl.global_init(option)
   option is one of the constants pycurl2.GLOBAL_SSL, pycurl2.GLOBAL_WIN32,
   pycurl2.GLOBAL_ALL, pycurl2.GLOBAL_NOTHING, pycurl2.GLOBAL_DEFAULT.
   Corresponds to `curl_global_init`_ in libcurl.

.. function:: pycurl2.global_cleanup()
   Corresponds to `curl_global_cleanup`_ in libcurl.

.. variable:: pycurl2.version
   This is a string with version information on libcurl, corresponding to `curl_version`_ in libcurl.

   Example usage::

       >>> import pycurl2
       >>> pycurl2.version
       'libcurl/7.12.3 OpenSSL/0.9.7e zlib/1.2.2.1 libidn/0.5.12'

.. function:: pycurl2.version_info()

   Corresponds to `curl_version_info`_ in libcurl.
   Returns a tuple of information which is similar to the ``curl_version_info_data``
   struct returned by `curl_version_info`_ in libcurl.

   Example usage::

       >>> import pycurl2
       >>> pycurl2.version_info()
       (2, '7.12.3', 461827, 'i586-pc-linux-gnu', 1565, 'OpenSSL/0.9.7e', 9465951,
       '1.2.2.1', ('ftp', 'gopher', 'telnet', 'dict', 'ldap', 'http', 'file',
       'https', 'ftps'), None, 0, '0.5.12')

.. _curl_version_info: http://curl.haxx.se/libcurl/c/curl_version.html
.. _curl_version: http://curl.haxx.se/libcurl/c/curl_version.html
.. _curl_global_init: http://curl.haxx.se/libcurl/c/curl_global_init.html
.. _curl_global_cleanup: http://curl.haxx.se/libcurl/c/curl_global_cleanup.html
