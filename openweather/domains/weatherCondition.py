from openweather.core import baseItem

class WeatherCondition(baseItem.baseDomain):
    def __init__(self, id = 0, name = "", description = "", icon = ""):
        self.name = name
        self.description = description
        self.icon = icon