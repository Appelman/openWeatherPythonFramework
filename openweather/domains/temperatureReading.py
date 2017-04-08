from openweather.core import baseItem
import datetime as datetime
import openweather.domains.wind as wind
import openweather.domains.coordinate as coordinate
import openweather.domains.city as city
import openweather.domains.weatherCondition as weatherCondition

class TemperatureReading(baseItem.baseDomain):
    def __init__(self):
        self.city = city.City()
        self.wind = wind.Wind()
        self.dateTime = datetime.datetime.now()
        self.sunrise =  datetime.datetime.now()
        self.sunset =   datetime.datetime.now()
        self.coordinate = coordinate.Coordinate()
        self.weatherCondition = weatherCondition.WeatherCondition()
        self.cloudiness = 0.0
        self.rainVolume = 0.0
        self.country = ""