import itertools
import sys
import pandas as pd


def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        start_point = points[order[i]][1:]
        end_point = points[order[i + 1]][1:]
        distance = (
            (end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2
        ) ** 0.5
        total_distance += distance
    return total_distance


def tsp_brute_force(points):
    num_points = len(points)
    min_distance = sys.maxsize
    best_order = None
    all_orders = list(itertools.permutations(range(num_points)))

    for order in all_orders:
        distance = calculate_distance(points, order)
        if distance < min_distance:
            min_distance = distance
            best_order = order

    return best_order, min_distance
