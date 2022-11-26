from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np


def check_coordinates(long, lat, area_coordinates):
    for coordinates in area_coordinates:
        polygon = Polygon(coordinates)
        point = Point([long, lat])  # create point
        # return service area if found at least one and stop the loop
        if not point.within(polygon):
            continue
        else:
            return True
