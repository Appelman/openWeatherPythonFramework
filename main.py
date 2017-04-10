import openweather.domains.city as city
import openweather.domains.wind as wind
import openweather.domains.temperatureReading as tempReading
import openweather.infrastructure.repositories.openWeatherRepository as openWeatherRepository
import json
import urllib.request 

#request = http.Request("api.openweathermap.org/data/2.5/weather?q=Eden Glen,ZA&appid=b50e52c1dd9315a140918d576959dabe")
#with http.urlopen(req) as response:
#    result = response.readall().decode("utf-8")

req = urllib.request.Request('http://api.openweathermap.org/data/2.5/weather?q=Eden Glen,ZA&appid=b50e52c1dd9315a140918d576959dabe&units=metric')
with urllib.request.urlopen(req) as response:
    result = json.loads(response.readall().decode('utf-8'))

repo = openWeatherRepository.OpenweatherRepository()

print(repo.read())