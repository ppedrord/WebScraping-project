import pickle
import time
import re


##############################################################################################
#   DATA CLEANING
##############################################################################################


def convert_to_int(num) -> int:
    try:
        return int(num)
    except:
        return None


def convert_to_float(number) -> int:
    try:
        return float(number)
    except:
        return None


def clean_runtime(runtime) -> int:
    runtime = re.findall("\d", runtime)
    runtime = ''.join(runtime)
    if runtime != '':
        return runtime
    else:
        return None


def clean_genre(genres: str) -> list:
    genre = genres[1:-1].upper()
    genre = genre.split(', ')

    return genre


##############################################################################################
#   MAIN
##############################################################################################


def data_cleaning() -> list:
    with open('movies.p', 'rb') as movies_file:
        file = pickle.load(movies_file)
    for i in file:
        i['year'] = convert_to_int(i['year'])
        i['runtime'] = clean_runtime(i['runtime'])
        i['num_votes'] = convert_to_int(i['num_votes'])
        i['collection'] = convert_to_int(i['collection'])
        i['imdb_rating'] = convert_to_float(i['imdb_rating'])
        i['genre'] = clean_genre(i['genre'])

    with open('movie_data_limited_all_updated.p', 'wb') as file_up:
        pickle.dump(file, file_up)

    return file


data_cleaning()

