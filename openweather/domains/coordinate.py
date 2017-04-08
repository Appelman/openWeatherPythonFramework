from openweather.core import baseItem

class Coordinate(baseItem.baseDomain):
    def __init__(self, longitude = 0.0, latitude = 0.0):
        self.longitude = longitude
        self.latitude = latitude