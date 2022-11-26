from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np


def check_coordinates(long, lat, coordinates):
    polygon = Polygon(coordinates)
    point = Point([long, lat])  # create point
    return point.within(polygon)
