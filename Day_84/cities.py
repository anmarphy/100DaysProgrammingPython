import pandas as pd
from geopy.geocoders import Nominatim
from tsp_functions import *


def geo_cities(city_names):
    # Initialize geocoder
    geolocator = Nominatim(user_agent="my_app")

    # Empty lists to store latitude and longitude
    latitudes = []
    longitudes = []

    # Retrieve latitude and longitude for each city
    for city in city_names:
        location = geolocator.geocode(city)
        if location:
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)
        else:
            latitudes.append(None)
            longitudes.append(None)

    # Create dataframe
    data = {"City": city_names, "Latitude": latitudes, "Longitude": longitudes}

    return pd.DataFrame(data)
