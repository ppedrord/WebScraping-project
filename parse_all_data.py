import sys, getopt
import time
import requests
import pickle
import re
from bs4 import BeautifulSoup as bs
from threading import Thread
import os
import random
import numpy as np

with open('all_urls_file.p', 'rb') as all_urls_file:
    list_urls = pickle.load(all_urls_file)

small_list = list_urls[0:100]


def execute():
    start = time.time()
    movies_list = list()
    for i in small_list:
        movie_data = parse_data(i)
        movies_list.extend(movie_data)
        print(movie_data)
    print("main method:", time.time() - start)
    return movies_list


def parse_data(url: str):
    response = requests.get(url)
    parser = bs(response.text, "html.parser")

    data = parser.find_all("div", {"class": "lister-item mode-advanced"})

    h3_selector = parser.find_all('h3', {'class': 'lister-item-header'})
    p_selector = parser.find_all('p', {'class': 'text-muted'})
    list_content_selector = parser.find_all('div', {'class': 'lister-item-content'})

    num_p = 0
    num_p_synopsis = 1

    movies_list = list()
    for i, card in enumerate(data):

        movie_title = h3_selector[i].find('a').text

        movie_url = h3_selector[i].find('a').get("href")

        title = movie_title

        if h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}) is None or '':
            movie_year = "Isn't Available"
        else:
            movie_year = h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}).text

        year = movie_year[1:-1]

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

        span_selector = list_content_selector[i].find('p', {'class': 'sort-num_votes-visible'})
        if span_selector is not None:
            if span_selector.find('span', {'name': 'nv'}) is False:
                movie_num_votes = "Isn't Available"
            else:
                movie_num_votes = span_selector.find('span', {'name': 'nv'}).get('data-value')
        else:
            movie_num_votes = "Isn't Available"

        num_votes = movie_num_votes

        if span_selector is not None and len(span_selector.find_all('span', {'name': 'nv'})) > 1:
            if span_selector.find_all('span', {'name': 'nv'})[1] is False:
                movie_collection = "Isn't Available"
            else:
                movie_collection = span_selector.find_all('span', {'name': 'nv'})[1].get('data-value')
        else:
            movie_collection = "Isn't Available"

        if movie_collection != "Isn't Available":
            collection = movie_collection
            collection = re.findall("\d", collection)
            collection = ''.join(collection)
        else:
            collection = movie_collection


        if list_content_selector[i].find('div', {'class': 'ratings-bar'}) is None:
            movie_imdb_rating = "Isn't Available"
        else:
            rating_bars_selector = list_content_selector[i].find('div', {'class': 'ratings-bar'})
            if rating_bars_selector.find('div', {'class': 'inline-block ratings-imdb-rating'}) is not None:
                movie_imdb_rating = rating_bars_selector.find('div', {'class': 'inline-block ratings-imdb-rating'}).get('data-value')
            else:
                movie_imdb_rating = "Isn't Available"
        imdb_rating = movie_imdb_rating

        movie_data = {
            'title': clean_data(title),
            'year': year,
            'certificate': clean_data(certificate),
            'runtime': clean_data(runtime),
            'genre': clean_data(genre),
            'synopsis': clean_data(synopsis),
            'imdb_rating': imdb_rating,
            'num_votes': num_votes,
            'collection': collection,
            'link': f"https://www.imdb.com{movie_url}"
            }

        movies_list.append(movie_data)

        num_p += 2
        num_p_synopsis += 2
    return movies_list


def clean_data(value: str):
    new_value = re.sub("/(\r\n|\n|\r)/gm", "", value)
    new_value = re.sub("\s+", " ", new_value)
    new_value = re.sub('\"', "", new_value)

    return new_value


execute()
