#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.
import json
from sympy import Point, Polygon
import os
from . import google

geo_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'twCounty2010.geo.json')
geo_file = open(geo_file_path)
city_geo_datas = json.loads(geo_file.read())['features']


def get_county(lat, lng):
    try:
        data = google.get_address(lat, lng)
        county_info = data[-3]
        county_name = county_info['long_name']
    except Exception:
        county_name = parse_county(lat, lng)
    finally:
        return county_name


def parse_county(lat, lng):
    poi = Point(lng, lat)
    for city_geo_data in city_geo_datas:
        polygons = city_geo_data['geometry']['coordinates']
        polygons = [polygons] if city_geo_data['geometry']['type'] == 'Polygon' else polygons
        for polygon_coordinates in polygons:
            polygon = Polygon(*polygon_coordinates[0])
            if polygon.encloses_point(poi):
                return city_geo_data['properties']['name']

    raise 'not in taiwan'

if __name__ == "__main__":
    print get_county(24.984813, 121.422057)
