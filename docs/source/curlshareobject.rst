.. module:: PycURL2


CurlShare Object
----------------

CurlShare objects have the following methods:

| setopt(option, value) -> None

Corresponds to curl_share_setopt in libcurl, where option is specified with the CURLSHOPT_* constants in libcurl, except that the CURLSHOPT\_ prefix has been changed to SH\_. Currently, value must be either LOCK_DATA_COOKIE or LOCK\_DATA\_DNS.


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
