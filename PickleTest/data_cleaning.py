import pickle
import time
import re


def data_cleaning(file: list) -> list:
    print(file)
    for i, v in enumerate(file):
        try:
            year = file[i]['year']
            file[i].update({'year': int(year)})
        except:
            year = None
            file[i].update({'year': year})

    for i, v in enumerate(file):
        runtime = file[i]['runtime']
        runtime = re.findall("\d", runtime)
        runtime = ''.join(runtime)
        if runtime != '':
            file[i].update({'runtime': int(runtime)})
        else:
            runtime = None
            file[i].update({'runtime': runtime})

    for i, v in enumerate(file):
        try:
            collection = file[i]['collection']
            file[i].update({'collection': int(collection)})
        except:
            collection = None
            file[i].update({'collection': collection})

    for i, v in enumerate(file):
        try:
            num_votes = file[i]['num_votes']
            file[i].update({'num_votes': int(num_votes)})
        except:
            num_votes = None
            file[i].update({'num_votes': num_votes})

    for i, v in enumerate(file):
        try:
            imdb_rating = file[i]['imdb_rating']
            file[i].update({'imdb_rating': float(imdb_rating)})
        except:
            imdb_rating = None
            file[i].update({'imdb_rating': imdb_rating})

    for i, v in enumerate(file):
        genre = file[i]['genre'][1:-1].upper()
        genre = genre.split(', ')
        file[i].update({'genre': genre})

    with open('movie_data_limited_all_updated.p', 'wb') as file_up:
        pickle.dump(file, file_up)

    return file


