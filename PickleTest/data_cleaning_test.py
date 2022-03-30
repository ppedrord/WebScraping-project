"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Data Cleaning - Tests

"""

import pytest
import data_cleaning
import pickle

with open('movie_data_limited_all.p', 'rb') as movies_file:
    object = pickle.load(movies_file)

movies_01 = [([
    {'title': 'Batman',
     'year': '2022',
     'certificate': '14',
     'runtime': '176 min',
     'genre': ' Action, Crime, Drama ',
     'synopsis': " When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.",
     'imdb_rating': '8.3',
     'num_votes': '291613',
     'collection': "Isn't Available",
     'link': 'https://www.imdb.com/title/tt1877830/?ref_=adv_li_tt'
     },
    {'title': 'O Projeto Adam',
     'year': '2022',
     'certificate': '12',
     'runtime': '106 min',
     'genre': ' Action, Adventure, Comedy ',
     'synopsis': ' After accidentally crash - landing in 2022, time - traveling fighter pilot Adam Reed teams up with his 12-year-old self for a mission to save the future.',
     'imdb_rating': '6.7',
     'num_votes': '106770',
     'collection': "Isn't Available",
     'link': 'https://www.imdb.com/title/tt2463208/?ref_=adv_li_tt'
     }]), ([
    {'title': 'Batman',
     'year': 2022,
     'certificate': '14',
     'runtime': 176,
     'genre': [
         'ACTION',
         'CRIME',
         'DRAMA'
         ],
     'synopsis': " When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.",
     'imdb_rating': 8.3,
     'num_votes': 291613,
     'collection': None,
     'link': 'https://www.imdb.com/title/tt1877830/?ref_=adv_li_tt'
     },
    {'title': 'O Projeto Adam',
     'year': 2022,
     'certificate': '12',
     'runtime': 106,
     'genre': [
         'ACTION',
         'ADVENTURE',
         'COMEDY'
         ],
     'synopsis': ' After accidentally crash-landing in 2022, time-traveling fighter pilot Adam Reed teams up with his 12-year-old self for a mission to save the future.',
     'imdb_rating': 6.7,
     'num_votes': 106770,
     'collection': None,
     'link': 'https://www.imdb.com/title/tt2463208/?ref_=adv_li_tt'
     }])]


@pytest.mark.parametrize(["file", "expected"], movies_01)
def test_binary_gap(file, expected):
    assert data_cleaning.data_cleaning(file) == expected
