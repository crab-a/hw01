from math import ceil
from Data import print_details as print_data


def sum(values):
    total = 0
    for num in values:
        total += num
    return total


def mean(values):
    total = sum(values)
    length = len(values)
    return total / length


def median(values):
    length = len(values)
    sorted_values = sorted(values)
    med = 0
    if length % 2:
        return sorted_values[int(length / 2)]  # #for not negative numbers works like floor so we can use whatever
    return (sorted_values[length / 2] + sorted_values[(length / 2) + 1]) / 2


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    :param: feature_description, data, treatment, target, threshold, is_above, statistic_functions

    """
    above, below = filter_by_treatment(data, treatment, threshold)
    data_clean = above if is_above else below
    print_details(feature_description, data_clean, target, statistic_functions)


def filter_by_treatment(data, treatment, threshold):
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for index, value in enumerate(data[treatment]):
        if value > threshold:
            for key in data1.keys():
                data1[key].append(data[key][index])
        else:
            for key in data2.keys():
                data2[key].append(data[key][index])
    return data1, data2


def print_details(feature_description, data, target, statistic_functions):
    print(feature_description + ":", end="")
    temp_features = [target]
    print_data(data, temp_features, statistic_functions)
