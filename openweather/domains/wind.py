from openweather.core import baseItem

class Wind(baseItem.baseDomain):
    def __init__(self, speed = 0, direction = 0.0):
        self.speed = speed
        self.direction = direction
        