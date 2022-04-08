import pickle
import pandas as pd

with open('movie_data_limited_all_updated.p', 'rb') as movies_file:
    data = pickle.load(movies_file)


def data_cleaning_certificate(movies: list) -> list:
    list_of_certificate_categories = list()
    for i in movies:
        if i['certificate'] is not None:
            if i['certificate'] != "Isn't Available":
                list_of_certificate_categories.append(i)

    for i in list_of_certificate_categories:
        if i['certificate'] == "PG":
            i['certificate'] = '10'

        elif i['certificate'] == "PG-13":
            i['certificate'] = '14'

        elif i['certificate'] == "R":
            i['certificate'] = '16'

        elif i['certificate'] == "NC-17":
            i['certificate'] = '18'

        elif i['certificate'] == "L":
            i['certificate'] = 'Livre'

        elif i['certificate'] == "16+":
            i['certificate'] = '16'

        elif i['certificate'] == "M/PG":
            i['certificate'] = '16'

        elif i['certificate'] == "M":
            i['certificate'] = '16'

        elif i['certificate'] == "X":
            i['certificate'] = '18'

        elif i['certificate'] == "GP":
            i['certificate'] = '10'

        elif i['certificate'] == "G":
            i['certificate'] = 'Livre'
        elif i['certificate'] == "(Banned)":
            i['certificate'] = "Banned"

    return list_of_certificate_categories


def count_genres_per_certificate(movies_cleaned: list) -> list:
    map_certificate = {
        'Livre': {},
        '10': {},
        '12': {},
        '14': {},
        '16': {},
        '18': {},
        'Not Rated': {},
        'Passed': {},
        'Unrated': {},
        'Approved': {},
        'Banned': {}
        }
    for i in movies_cleaned:
        for g in i['genre']:
            if g not in map_certificate[i['certificate']]:
                map_certificate[i['certificate']][g] = 1
            else:
                map_certificate[i['certificate']][g] += 1
    print(repr(map_certificate))
    return map_certificate


count_genres_per_certificate(data_cleaning_certificate(data))
