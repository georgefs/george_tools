__all__ = ['check_url',]

from cStringIO import StringIO
import urllib2
import Image


def check_url(url):
    try:
        data = urllib2.urlopen(url).read()
        Image.open(StringIO(data))
    except Exception, e:
        return False
    else:
        return True
