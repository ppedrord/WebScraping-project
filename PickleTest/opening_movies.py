import pickle
import pandas as pd

with open('movie_data_limited_all_updated.p', 'rb') as movies_file:
    data = pickle.load(movies_file)

number_of_releases_1910 = 0
number_of_releases_1920 = 0
number_of_releases_1930 = 0
number_of_releases_1940 = 0
number_of_releases_1950 = 0
number_of_releases_1960 = 0
number_of_releases_1970 = 0
number_of_releases_1980 = 0
number_of_releases_1990 = 0
number_of_releases_2000 = 0
number_of_releases_2010 = 0
number_of_releases_2020 = 0
number_of_releases_2030 = 0
for i in data:
    if i['year'] is not None and 1900 < i['year'] < 1911:
        number_of_releases_1910 += 1
    if i['year'] is not None and 1910 < i['year'] < 1921:
        number_of_releases_1920 += 1
    if i['year'] is not None and 1920 < i['year'] < 1931:
        number_of_releases_1930 += 1
    if i['year'] is not None and 1930 < i['year'] < 1941:
        number_of_releases_1940 += 1
    if i['year'] is not None and 1940 < i['year'] < 1951:
        number_of_releases_1950 += 1
    if i['year'] is not None and 1950 < i['year'] < 1961:
        number_of_releases_1960 += 1
    if i['year'] is not None and 1960 < i['year'] < 1971:
        number_of_releases_1970 += 1
    if i['year'] is not None and 1970 < i['year'] < 1981:
        number_of_releases_1980 += 1
    if i['year'] is not None and 1980 < i['year'] < 1991:
        number_of_releases_1990 += 1
    if i['year'] is not None and 1990 < i['year'] < 2001:
        number_of_releases_2000 += 1
    if i['year'] is not None and 2000 < i['year'] < 2011:
        number_of_releases_2010 += 1
    if i['year'] is not None and 2010 < i['year'] < 2021:
        number_of_releases_2020 += 1
    if i['year'] is not None and 2020 < i['year'] < 2031:
        number_of_releases_2030 += 1

group_by_decade = [
    {
        'years': "1900's",
        'number_of_releases': number_of_releases_1910
        },
    {
        'years': "10's",
        'number_of_releases': number_of_releases_1920
        },
    {
        'years': "20's",
        'number_of_releases': number_of_releases_1930
        },
    {
        'years': "30's",
        'number_of_releases': number_of_releases_1940
        },
    {
        'years': "40's",
        'number_of_releases': number_of_releases_1950
        },
    {
        'years': "50's",
        'number_of_releases': number_of_releases_1960
        },
    {
        'years': "60's",
        'number_of_releases': number_of_releases_1970
        },
    {
        'years': "70's",
        'number_of_releases': number_of_releases_1980
        },
    {
        'years': "80's",
        'number_of_releases': number_of_releases_1990
        },
    {
        'years': "90's",
        'number_of_releases': number_of_releases_2000
        },
    {
        'years': "2000's",
        'number_of_releases': number_of_releases_2010
        },
    {
        'years': "2010's",
        'number_of_releases': number_of_releases_2020
        },
    {
        'years': "2020's",
        'number_of_releases': number_of_releases_2030
        }
    ]
print(len(group_by_decade))
