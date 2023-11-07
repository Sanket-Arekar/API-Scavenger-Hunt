import requests

# Define the API endpoint to get a list of countries in Africa.
url = 'https://restcountries.com/v3.1/all'


response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    # Filter countries to only include those in Africa.
    countries_in_africa = [
        country for country in data if 'Africa' in country.get('region', [])]

    if countries_in_africa:
        print("Countries in Africa:")
        for country in countries_in_africa:
            print(country['name']['common'])
    else:
        print("No countries in Africa found in the API data.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
