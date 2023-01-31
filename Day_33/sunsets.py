import requests
from datetime import datetime

'''
https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP
'''

parameters={
    'lat' : 4.442510,
    'lng' : -74.044160,
    'formatted' : 0

}

response = requests.get('https://api.sunrise-sunset.org/json',
                        params=parameters
                        )

sunset = response.json()['results']['sunset'].split('T')[1].split(':')[0]
sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
