#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.

import urllib2
import urllib
import json

__all__ = ['get_latlng', 'get_address']

api = "http://maps.googleapis.com/maps/api/geocode/json"

def get_latlng(address):
    params = dict()
    params['address'] = address

    result = query(params)['results'][0]['geometry']
    return result

def get_address(lat, lng):
    params = dict()
    params['latlng'] = "{},{}".format(lat, lng)

    result = query(params)['results'][0]['address_components']
    return result

def query(params):
    headers = dict()
    headers['Accept-Language'] = 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4'

    params['sensor'] = "true"

    params = urllib.urlencode(params)
    url = "{}?{}".format(api, params)
    print url

    request = urllib2.Request(url, None, headers)
    return json.loads(urllib2.urlopen(request).read())

if __name__ == "__main__":
    print get_latlng('taiwan')
    print get_address(25, 121)
