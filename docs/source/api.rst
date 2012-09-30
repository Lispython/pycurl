API
===

.. module:: PycURL2
    :synopsis: public PycURL2 API

This document describes the API to PycURL2. It will be most userful as reference
for creating application that need access to libcurl methods.

.. autoclass:: pycurl2.Curl
    This function creates a new :class:`Curl` object which corresponds to a CURL handle in libcurl.
    Curl objects automatically set ``CURLOPT_VERBOSE`` to 0, ``CURLOPT_NOPROGRESS`` to 1,
    provide a default ``CURLOPT_USERAGENT`` and setup ``CURLOPT_ERRORBUFFER`` to point
    to a private error buffer

    :members: close, errstr, getinfo, perform, reset, setopt, unsetopt

    .. method:: setopt(option, value)
         Corresponds to `curl_easy_setopt`_ in libcurl, where option is specified
	 with the ``CURLOPT_*`` constants in libcurl, except that the ``CURLOPT\_`` prefix
	 has been removed. The type for value depends on the option,
	 and can be either a string, integer, long integer, file objects, lists,
	 or functions.

	 Example usage:

	 .. sourcecode:: python

	     import pycurl2 as pycurl
	     c = pycurl.Curl()
	     c.setopt(pycurl.URL, "http://www.python.org/")
	     c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	     import StringIO
	     b = StringIO.StringIO()
	     c.setopt(pycurl.WRITEFUNCTION, b.write)
	     c.setopt(pycurl.FOLLOWLOCATION, 1)
	     c.setopt(pycurl.MAXREDIRS, 5)
	     c.perform()
	     print b.getvalue()

    .. method::  close()
         Corresponds to `curl_easy_cleanup`_ in libcurl. This method is automatically
	 called by pycurl when a :class:`~Curl` object no longer has any references to it,
	 but can also be called explicitly.

    .. method:: perform()
         Corresponds to `curl_easy_perform`_ in libcurl.

    .. method:: errstr()
         Returns the internal libcurl error buffer of this handle as a string.

    .. method:: getinfo(option)
         Corresponds to `curl_easy_getinfo`_ in libcurl, where option
	 is the same as the CURLINFO_* constants in libcurl, except
	 that the ``CURLINFO\_`` prefix has been removed. Result contains an integer,
	 float or string, depending on which option is given.
	 The ``getinfo`` method should not be called unless ``perform`` has been called
	 and finished.

	 Example usage:

	 .. sourcecode:: python

	     import pycurl2 as pycurl
	     c = pycurl.Curl()
	     c.setopt(pycurl.URL, "http://sf.net")
	     c.setopt(pycurl.FOLLOWLOCATION, 1)
	     c.perform()
	     print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)

	     200 "http://sourceforge.net/"

.. _curl_easy_setop: http://curl.haxx.se/libcurl/c/curl_easy_setopt.html
.. _curl_easy_cleanup: http://curl.haxx.se/libcurl/c/curl_easy_cleanup.html
.. _curl_easy_perform: http://curl.haxx.se/libcurl/c/curl_easy_perform.html
.. _curl_easy_getinfo: http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html

.. autoclass:: pycurl2.CurlMulti
    This function creates a new :class:`CurlMulti` object which
    corresponds to a CURLM handle in libcurl.

    :members: add_handle, assign, close, fdset, info_read, perform,
	      remove_handle, select, setopt, socket_action,
	      socket_all, timeout

    :method: close()
        Corresponds to `curl_multi_cleanup`_ in libcurl. This method
	is automatically called by pycurl when a CurlMulti object no
	longer has any references to it, but can also be called explicitly.

    :method: perform()
	Corresponds to `curl_multi_perform`_ in libcurl.

    :method: add_handle(Curl object)
	Corresponds to `curl_multi_add_handle`_ in libcurl. This method
	adds an existing and valid Curl object to the CurlMulti object.

	IMPORTANT NOTE: add_handle does not implicitly add a Python reference to
	the Curl object (and thus does not increase the reference count on the Curl object).

     :method: remove_handle(Curl object)
	Corresponds to `curl_multi_remove_handle`_ in libcurl.
	This method removes an existing and valid Curl object from the CurlMulti object.

	IMPORTANT NOTE: remove_handle does not implicitly remove a Python reference
	from the Curl object (and thus does not decrease the reference count on the Curl object).


     :method: fdset()
	Corresponds to `curl_multi_fdset`_ in libcurl. This method extracts the file descriptor
	information from a CurlMulti object. The returned lists can be used with the select module to poll for events.

	Example usage:

	.. sourcecode:: python

	    import pycurl2 as pycurl
	    c = pycurl.Curl()
	    c.setopt(pycurl.URL, "http://curl.haxx.se")
	    m = pycurl.CurlMulti()
	    m.add_handle(c)
	    while 1:
	        ret, num_handles = m.perform()
		if ret != pycurl.E_CALL_MULTI_PERFORM: break
            while num_handles:
                apply(select.select, m.fdset() + (1,))
            while 1:
                ret, num_handles = m.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM: break

     :method: select(timeout)
	This is a convenience function which simplifies the combined use of fdset() and the select module.

	Example usage:

	.. sourcecode:: python

	    import pycurl2 as pycurl
	    c = pycurl.Curl()
	    c.setopt(pycurl.URL, "http://curl.haxx.se")
	    m = pycurl.CurlMulti()
	    m.add_handle(c)
	    while 1:
                ret, num_handles = m.perform()
		if ret != pycurl.E_CALL_MULTI_PERFORM: break
	    while num_handles:
                ret = m.select(1.0)
		if ret == -1:  continue

		while 1:
		    ret, num_handles = m.perform()
		    if ret != pycurl.E_CALL_MULTI_PERFORM: break

     :method: info_read([max])
         Corresponds to the `curl_multi_info_read`_ function in libcurl. This method extracts
	 at most max messages from the multi stack and returns them in two lists.
	 The first list contains the handles which completed successfully and the second list contains
	 a tuple <curl object, curl error number, curl error message> for each failed curl object.
	 The number of queued messages after this method has been called is also returned.


.. _curl_multi_cleanup: http://curl.haxx.se/libcurl/c/curl_multi_cleanup.html
.. _curl_multi_perform: http://curl.haxx.se/libcurl/c/curl_multi_perform.html
.. _curl_multi_add_handle: http://curl.haxx.se/libcurl/c/curl_multi_add_handle.html
.. _curl_multi_remove_handle: http://curl.haxx.se/libcurl/c/curl_multi_remove_handle.html
.. _curl_multi_fdset: http://curl.haxx.se/libcurl/c/curl_multi_fdset.html
.. _curl_multi_info_read: http://curl.haxx.se/libcurl/c/curl_multi_info_read.html



.. autoclass:: pycurl2.CurlShare
     This function creates a new :class:`CurlShare` object which corresponds
     to a CURLSH handle in libcurl. :class:`CurlShare` objects is what you pass as an
     argument to the SHARE option on :class:`Curl` objects.

    :members: setopt

    :method: setopt(option, value)

     Corresponds to curl_share_setopt in libcurl, where option is specified
     with the ``CURLSHOPT_*`` constants in libcurl, except that the ``CURLSHOPT\_``
     prefix has been changed to ``SH\_``. Currently, value must be either
     ``LOCK_DATA_COOKIE`` or ``LOCK\_DATA\_DNS``.


     .. sourcecode:: python
         import pycurl2 as pycurl
         curl = pycurl.Curl()
         s = pycurl.CurlShare()
         s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_COOKIE)
         s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_DNS)
         curl.setopt(pycurl.URL, 'http://curl.haxx.se')
         curl.setopt(pycurl.SHARE, s)
         curl.perform()
         curl.close()


.. _curl_share_setopt: http://curl.haxx.se/libcurl/c/curl_share_setopt.html
