import os
import requests

API_ID = os.getenv('API_ID')
url = "https://openexchangerates.org/api"
response = requests.get(f"{url}/latest.json?app_id={API_ID}").json()
print(response['rates'])