#!/usr/bin/python

import os
from mapbox import Directions, Surface, MapMatcher


ACCESS_TOKEN = os.environ['MAPBOX_ACCESS_TOKEN']

def get_directions(mode, start, end):
    curl "https://api.mapbox.com/directions/v5/mapbox/walking/"
