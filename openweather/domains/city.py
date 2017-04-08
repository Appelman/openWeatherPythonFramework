from openweather.core import baseItem

class City(baseItem.baseDomain):
    def __init__(self, name = ""):
        self.name = name

    def __str__(self):
        return self.name