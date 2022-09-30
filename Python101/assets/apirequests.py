import requests
from time import sleep
response = requests.get('http://api.open-notify/astros.json', timeout=(2,5))
json = response.json

for person in json['people']:
    print(person['name'])