import openweather.domains.city as city
import openweather.domains.wind as wind
import openweather.domains.temperatureReading as tempReading

myTempReading = tempReading.TemperatureReading()
myTempReading.city.name = "temp city"

print(myTempReading.city.name)