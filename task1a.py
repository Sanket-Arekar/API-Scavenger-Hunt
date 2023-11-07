import requests
import json


api_key = 'f60226237e72c3a9e3e98d97be3cbfbb'

url = f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
