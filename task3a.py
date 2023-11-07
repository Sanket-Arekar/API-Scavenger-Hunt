import requests

url = 'https://restcountries.com/v3.1/name/brazil?fullText=true'

# Make the API request.
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    brazil_info = data[0]

    # Extract and print various details about Brazil.
    print("Additional Information about Brazil:")
    print(f"Common Name: {brazil_info['name']['common']}")
    print(f"Official Name: {brazil_info['name']['official']}")
    print(f"Capital: {brazil_info['capital']}")
    print(f"Region: {brazil_info['region']}")
    print(f"Subregion: {brazil_info['subregion']}")
    print(f"Population: {brazil_info['population']}")
    print(f"Area: {brazil_info['area']} square kilometers")

    # Official Language is within the "languages" dictionary.
    # 'por' is the ISO 639-1 code for Portuguese.
    official_language = brazil_info['languages']['por']
    print(f"Official Language: {official_language}")

    # List of neighboring countries.
    neighboring_countries = brazil_info.get('borders', [])
    if neighboring_countries:
        print("Neighboring Countries:")
        for neighbor in neighboring_countries:
            print(neighbor)
    else:
        print("Brazil has no neighboring countries listed in the API data.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
