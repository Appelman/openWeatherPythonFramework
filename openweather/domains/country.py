from openweather.core import baseItem

class Country(baseItem.baseDomain):
    def __init__(self, name = "", code = ""):
        self.name = name
        self.code = code

    def __str__(self):
        return self.name