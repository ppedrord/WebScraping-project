from bs4 import BeautifulSoup as bs
import re
from imdbGenreSpider import creating_targets
from imdbGenreSpider import advance_pages, sport_genre
import SeleniumRequests
from SeleniumRequests import browser
# import main
import requests
import numpy as np
import random
import time


def sending_requests(advance_pages):
    global movies_list
    global cards
    from requests import get
    cards = sport_genre.find_all('div', {'class': 'lister-item mode-advanced'})
    movies_list = list()
    h3_selector = sport_genre.find_all('h3', {'class': 'lister-item-header'})
    p_selector = sport_genre.find_all('p', {'class': 'text-muted'})
    for i in advance_pages:
        print(i)
        request = get(i)
        print(request.status_code)
        num_p = 0
        num_p_synopsis = 1
        for j, card in enumerate(cards):
            movie_title = h3_selector[j].find('a').text
            title = movie_title

            if h3_selector[j].find('span', {'class': 'lister-item-year text-muted unbold'}) is None:
                movie_year = "Isn't Available"
            else:
                movie_year = h3_selector[j].find('span', {'class': 'lister-item-year text-muted unbold'}).text

            year = movie_year

            if p_selector[num_p].find('span', {'class': 'certificate'}) is None:
                movie_certificate = "Isn't Available"
            else:
                movie_certificate = p_selector[num_p].find('span', {'class': 'certificate'}).text

            certificate = movie_certificate

            if p_selector[num_p].find('span', {'class': 'runtime'}) is None:
                movie_runtime = "Isn't Available"
            else:
                movie_runtime = p_selector[num_p].find('span', {'class': 'runtime'}).text

            runtime = movie_runtime

            if p_selector[num_p].find('span', {'class': 'genre'}) is None:
                movie_genre = "Isn't Available"
            else:
                movie_genre = p_selector[num_p].find('span', {'class': 'genre'}).text

            genre = movie_genre

            if p_selector[num_p_synopsis] is None:
                movie_synopsis = "Isn't Available"
            else:
                movie_synopsis = p_selector[num_p_synopsis].text

            synopsis = movie_synopsis

            movie_data = {
                'title': title,
                'year': year,
                'certificate': certificate,
                'runtime': runtime,
                'genre': genre,
                'synopsis': synopsis
                }
            movies_list.append(movie_data)
            print(j, movie_data)
            num_p += 2
            num_p_synopsis += 2
    return movies_list


print(sending_requests(advance_pages))