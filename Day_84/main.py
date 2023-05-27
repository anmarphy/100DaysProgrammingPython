"""This is a program to figure out the shortest path to visit all the cities."""

import pandas as pd
from cities import *
from tsp_functions import *


def tsp():
    city_names = [
        "New York City",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
    ]

    df = geo_cities(city_names)
    points = df[["City", "Latitude", "Longitude"]].values.tolist()
    best_order, min_distance = tsp_brute_force(points)
    print("Best order:")
    for index in best_order:
        print(points[index][0])
    print("Minimum distance:", min_distance)


if __name__ == "__main__":
    tsp()
