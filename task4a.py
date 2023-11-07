import requests

# Replace 'YOUR_API_KEY' with your actual Currency Converter API key.
api_key = '90d12c0ee05af335007a7de8'

# Define the amount and currencies to convert.
amount_usd_to_eur = 100
from_currency_usd_to_eur = 'USD'
to_currency_usd_to_eur = 'EUR'

amount_jpy_to_gbp = 1000
from_currency_jpy_to_gbp = 'JPY'
to_currency_jpy_to_gbp = 'GBP'

# Define the API endpoint for currency conversion.
base_url = 'https://v6.exchangerate-api.com/v6'
url_usd_to_eur = f'{base_url}/{api_key}/latest/{from_currency_usd_to_eur}'
url_jpy_to_gbp = f'{base_url}/{api_key}/latest/{from_currency_jpy_to_gbp}'

# Make API requests to convert USD to EUR and JPY to GBP.
response_usd_to_eur = requests.get(url_usd_to_eur)
response_jpy_to_gbp = requests.get(url_jpy_to_gbp)

# Check if the requests were successful.
if response_usd_to_eur.status_code == 200 and response_jpy_to_gbp.status_code == 200:
    data_usd_to_eur = response_usd_to_eur.json()
    data_jpy_to_gbp = response_jpy_to_gbp.json()

    # Check if the currencies are available for conversion.
    if (
        to_currency_usd_to_eur in data_usd_to_eur['conversion_rates']
        and to_currency_jpy_to_gbp in data_jpy_to_gbp['conversion_rates']
    ):
        conversion_rate_usd_to_eur = data_usd_to_eur['conversion_rates'][to_currency_usd_to_eur]
        converted_amount_usd_to_eur = amount_usd_to_eur * conversion_rate_usd_to_eur

        conversion_rate_jpy_to_gbp = data_jpy_to_gbp['conversion_rates'][to_currency_jpy_to_gbp]
        converted_amount_jpy_to_gbp = amount_jpy_to_gbp * conversion_rate_jpy_to_gbp

        print(f"{amount_usd_to_eur} {from_currency_usd_to_eur} is equivalent to {converted_amount_usd_to_eur} {to_currency_usd_to_eur}")
        print(f"{amount_jpy_to_gbp} {from_currency_jpy_to_gbp} is equivalent to {converted_amount_jpy_to_gbp} {to_currency_jpy_to_gbp}")
    else:
        print("One or more of the specified currencies are not available for conversion.")
else:
    print(
        f"Failed to retrieve data. Status code: {response_usd_to_eur.status_code}")
