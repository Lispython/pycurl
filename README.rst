PycCURL2: Python interface to libcurl
=====================================


.. image:: https://secure.travis-ci.org/Lispython/pycurl.png
	   :target: https://secure.travis-ci.org/Lispython/pycurl

PycURL2 is a fork from original `PycURL`_ library that no maintained from 7.19.0 (Sep 9 2008).

PycURL2 is a Python interface to `libcurl`_. PycURL2 can be used to fetch objects
identified by a URL from a Python program, similar to the `urllib`_ Python module.
PycURL2 is mature, very fast, and supports a lot of features.


Overview
--------

- libcurl is a free and easy-to-use client-side URL transfer library, supporting
  FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
  SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT,
  FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication
  (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer resume,
  http proxy tunneling and more!

- libcurl is highly portable, it builds and works identically on numerous platforms,
  including Solaris, NetBSD, FreeBSD, OpenBSD, Darwin, HPUX, IRIX, AIX, Tru64, Linux,
  UnixWare, HURD, Windows, Amiga, OS/2, BeOs, Mac OS X, Ultrix, QNX, OpenVMS, RISC OS,
  Novell NetWare, DOS and more...

- libcurl is `free`_, `thread-safe`_, `IPv6 compatible`_, `feature rich`_, `well supported`_, `fast`_,
  `thoroughly documented`_ and is already used by many known, big and successful `companies`_
  and numerous `applications`_.

.. _free: http://curl.haxx.se/docs/copyright.html
.. _thread-safe: http://curl.haxx.se/libcurl/features.html#thread
.. _`IPv6 compatible`: http://curl.haxx.se/libcurl/features.html#ipv6
.. _`feature rich`: http://curl.haxx.se/libcurl/features.html#features
.. _`well supported`: http://curl.haxx.se/libcurl/features.html#support
.. _`fast`: http://curl.haxx.se/libcurl/features.html#fast
.. _`thoroughly documented`: http://curl.haxx.se/libcurl/features.html#docs
.. _companies: http://curl.haxx.se/docs/companies.html
.. _applications: http://curl.haxx.se/libcurl/using/apps.html


Installation
------------

You can install the most recent PycURL2 version using `easy_install`_::

    easy_install pycurl2

or `pip`_::

    pip install pycurl2


.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip


Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
   There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published.


Why I start my own pycurl fork?
-------------------------------
Original pycurl last updated at version 7.19.0  on Sep 9 2008. Then I working on `human_curl`_ library,
I faced with the problems of pycurl. Pycurl need more beautiful rst docs, clean examples, sources and package data.
I try to solve this problems on my fork.


.. include:: docs/source/TODO.rst


License
-------

- Copyright (C) 2001-2008 Kjetil Jacobsen
- Copyright (C) 2001-2008 Markus F.X.J. Oberhumer
- Copyright (C) 2012 Alexandr Lispython

All rights reserved.

PycURL is dual licensed under the LGPL and an MIT/X derivative license
based on the cURL license.  A full copy of the LGPL license is included
in the file COPYING.  A full copy of the MIT/X derivative license is
included in the file COPYING2.  You can redistribute and/or modify PycURL
according to the terms of either license.


.. _PycURL: http://pycurl.sourceforge.net/
.. _libcurl: http://curl.haxx.se/libcurl/
.. _urllib: http://docs.python.org/library/urllib.html
.. _`the repository`: https://github.com/Lispython/pycurl/
.. _human_curl: https://github.com/Lispython/human_curl
