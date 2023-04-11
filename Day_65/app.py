from libs.openexchange import OpenExchangeClient
import os

api_id = os.getenv('API_ID')

client = OpenExchangeClient(api_id )

usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f"USD{usd_amount} is GBP{gbp_amount}")