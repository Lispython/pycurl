.. module:: PycURL2


CurlObject
==========

Curl objects have the following methods:

- close() -> None
  Corresponds to curl_easy_cleanup in libcurl. This method is automatically
  called by pycurl when a Curl object no longer has any references to it,
  but can also be called explicitly.

- perform() -> None
  Corresponds to curl_easy_perform in libcurl.

- setopt(option, value) -> None
  Corresponds to curl_easy_setopt in libcurl, where option is specified
  with the CURLOPT_* constants in libcurl, except that the CURLOPT\_ prefix
  has been removed. The type for value depends on the option,
  and can be either a string, integer, long integer, file objects, lists, or functions.

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

- getinfo(option) -> Result
  Corresponds to curl_easy_getinfo in libcurl, where option
  is the same as the CURLINFO_* constants in libcurl, except
  that the CURLINFO\_ prefix has been removed. Result contains an integer,
  float or string, depending on which option is given.
  The getinfo method should not be called unless perform has been called and finished.

  Example usage:

  .. sourcecode:: python

      import pycurl2 as pycurl
      c = pycurl.Curl()
      c.setopt(pycurl.URL, "http://sf.net")
      c.setopt(pycurl.FOLLOWLOCATION, 1)
      c.perform()
      print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)

      200 "http://sourceforge.net/"

- errstr() -> String
  Returns the internal libcurl error buffer of this handle as a string.

