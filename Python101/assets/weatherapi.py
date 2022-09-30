import requests

api_key = "e8494f437764df28b694ee264ba2cdc6"
city = "Dallas"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json
#print(request.json())

description = json().get("weather")[0].get("description")
print("Today's forecast is", description)

temp_min = json().get("main").get("temp_min")
print("The minimum temperature is", temp_min)

temp_max = json().get("main").get("temp_max")
print("The maximum temperature is", temp_max)
