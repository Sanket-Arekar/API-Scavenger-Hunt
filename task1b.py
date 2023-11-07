import requests


api_key = 'f60226237e72c3a9e3e98d97be3cbfbb'


city = 'Tokyo'
units = 'metric'

# Define the API endpoint for the 5-day forecast.
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}'


response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    print(f"5-Day Weather Forecast for {city}:\n")
    for forecast in data['list']:
        date = forecast['dt_txt']
        temperature = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        print(f"Date and Time: {date}")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
